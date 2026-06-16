# Generic DA14531 Dev Board Toolchain and Access Paths

## Purpose

This note is a generic orientation guide for working with a Renesas/Dialog
DA14531 development board from a Windows PC. It describes the common tools used
to build firmware, program SPI flash, reset the device, and run PC-side tests.

It intentionally does not assume a particular product firmware architecture.
Your project may boot as:

- a single bootable image at `0x00000000`
- a boot manager plus one or more application slots
- a vendor SUOTA layout
- a custom recovery-loader layout
- a RAM-loaded debug image

Before programming a board, confirm the image format and flash map for the
specific project.

## Typical Hardware Pieces

| Item | Role |
| --- | --- |
| DA14531 USB development kit or custom board | Device under test. |
| DA14531 / DA14531MOD MCU | BLE microcontroller running the firmware. |
| SEGGER J-Link or on-board J-Link | SWD/JTAG debug and programming bridge. |
| USB CDC UART, if present | Optional serial/log/control interface. Not all projects use it. |
| External SPI flash, if present | Nonvolatile boot/storage medium for many DA14531 projects. |
| Sensors, peripherals, or application hardware | Project-specific; do not assume buses or power domains until checked. |

## Common Windows Tools

| Tool | Typical purpose |
| --- | --- |
| Keil uVision 5 | Opens/builds DA14531 SDK projects that use `.uvprojx`. |
| Arm Compiler 6 / ARMCLANG | Compiles and links firmware when configured by Keil. |
| `fromelf` | Converts Keil `.axf` output into `.bin` or `.hex`. |
| DA14531 SDK | Provides BLE stack, drivers, scatter files, boot tools, and examples. |
| SmartSnippets Toolbox | Erases, writes, reads, and verifies DA14531 SPI flash through J-Link. |
| SmartSnippets DA1453x JTAG programmer firmware | Temporary RAM program used by SmartSnippets to access SPI flash. |
| SEGGER J-Link tools | Enumerates probes, resets/halt/runs target, and can support debug workflows. |
| Python PC tools | Project-specific test scripts, BLE tools, UART tools, dashboards, or regression runners. |
| BLE host stack / Bleak | Optional PC BLE control path when the firmware exposes a BLE command interface. |

## First Questions For Any DA14531 Project

Answer these before building or flashing:

1. Which folder is the authoritative project root?
2. Does the Keil project rely on relative paths into a DA14531 SDK tree?
3. Which Keil target should be built?
4. Is the output image raw, bootable, encrypted, signed, compressed, or slot-wrapped?
5. Does the board boot from external SPI flash, OTP, UART, or RAM?
6. What is the SPI flash size?
7. What is the expected flash map?
8. Is there a boot manager, secondary bootloader, SUOTA flow, or recovery app?
9. Which interface is used for testing: BLE, UART, RTT, SWD, USB CDC, log-only, or a vendor tool?
10. What manual reset or power-cycle step is required after programming?

## Detecting The Dev Board

Use SmartSnippets Toolbox GUI:

1. Open SmartSnippets Toolbox.
2. Select the board/chip family if needed.
3. Use `Board -> Detect device`.
4. Confirm the J-Link/debug interface and any CDC UART port.

Use SEGGER J-Link from PowerShell:

```powershell
$script = Join-Path $env:TEMP 'jlink_showemu.jlink'
Set-Content -LiteralPath $script -Value @('ShowEmuList','exit') -Encoding ASCII
& 'C:\Program Files\SEGGER\JLink_V856\JLink.exe' -CommanderScript $script
```

Use Windows serial-port enumeration:

```powershell
Get-CimInstance Win32_SerialPort | Select-Object DeviceID,Description,PNPDeviceID
```

Record the J-Link serial number and any COM port used by the project. Do not
hard-code another engineer's serial number unless you know it matches the
attached board.

## Building Firmware With Keil

Typical GUI flow:

1. Open the project `.uvprojx` in Keil uVision.
2. Select the intended target.
3. Build or rebuild.
4. Confirm the expected `.axf`, `.bin`, or `.hex` output was generated.
5. Check the build log for warnings, image size, RAM usage, and post-build
   conversion output.

Typical command-line pattern:

```powershell
cd '<project-root>\Keil'
& '<path-to-keil>\UV4\UV4.exe' -b '<project>.uvprojx' -t '<target-name>' -j0 -o '<build-log>.log'
```

Common output files:

```text
*.axf    Linked firmware image with symbols.
*.map    Linker map file, useful for RAM/flash size analysis.
*.bin    Binary image, often produced by fromelf.
*.hex    Intel HEX image, if enabled.
```

For memory-constrained DA14531 work, preserve the `.map` file and build log for
every candidate image.

## Programming With SmartSnippets Toolbox

SmartSnippets normally uses this sequence internally:

1. Connect to DA14531 through J-Link/SWD.
2. Download a temporary DA1453x SPI programmer into DA14531 RAM.
3. Use that RAM program to access external SPI flash.
4. Erase, write, read, or verify flash.
5. Optionally add a DA14531 bootable-image header.
6. Reset the device after programming.

Typical variables:

```powershell
$tool = 'C:\Program Files\SmartSnippetsToolbox\SmartSnippetsToolbox5.0.26\SmartSnippetsToolbox.exe'
$sdk  = '<path-to-DA14531-SDK>'
$fw   = '<path-to-DA14531-SDK>\config\toolbox_resources\DA1453x\common\jtag_programmer.bin'
$jtag = '<detected-J-Link-serial>'
```

Full flash erase:

```powershell
& $tool -sdk $sdk -type spi -chip DA14531 -jtag $jtag -cmd erase -firmware $fw -y
```

Write a normal bootable SPI image at `0x00000000`:

```powershell
& $tool -sdk $sdk -type spi -chip DA14531 -jtag $jtag -cmd write -file '<image.bin>' -bootable -verify -max <flash-size> -firmware $fw -y
```

Write a raw binary blob at a fixed flash offset:

```powershell
& $tool -sdk $sdk -type spi -chip DA14531 -jtag $jtag -cmd write -file '<raw.bin>' -offset <offset> -verify -max <flash-size> -firmware $fw -y
```

Read flash back for verification:

```powershell
& $tool -sdk $sdk -type spi -chip DA14531 -jtag $jtag -cmd read -file '<readback.bin>' -offset <offset> -length <length> -max <flash-size> -firmware $fw -y
```

Important: use `-bootable` only when the file should be converted/programmed as
a DA14531 bootable SPI image. Do not use `-bootable` for already wrapped slot
images, metadata blocks, calibration sectors, logs, or arbitrary raw data.

## Image Architecture Checklist

Before writing any image, classify it:

| Image type | Typical programming mode |
| --- | --- |
| Plain application intended to boot directly from SPI offset `0x00000000` | SmartSnippets `-bootable` write. |
| Raw application body that a custom boot manager will wrap or copy | Project-specific; do not flash blindly. |
| Slot-wrapped application image | Raw write to the slot offset specified by the project flash map. |
| Boot manager / stage-1 loader | Often bootable at `0x00000000`, but confirm project design. |
| Recovery application | Often raw slot write, but confirm project design. |
| Calibration/config/log data | Raw sector write/read; normally not bootable. |
| RAM-only debug image | Loaded by debugger or vendor script; does not persist in SPI flash. |

If you are unsure whether a `.bin` is raw or wrapped, inspect the first bytes
and compare them to the project's documented image header. Vector-table-looking
bytes are not the same thing as a project slot header.

## Reset And Boot Expectations

After a SmartSnippets write, the device may be:

- running the temporary SmartSnippets RAM programmer
- reset into the newly programmed SPI image
- halted by the debugger
- waiting for a manual power cycle
- advertising over BLE
- silent because the programmed image is not valid for the selected boot path

If the application does not start after programming:

1. Confirm the write and verify succeeded.
2. Confirm the image was programmed at the correct offset.
3. Confirm the file was written in the correct mode (`-bootable` vs raw).
4. Reset through SmartSnippets/J-Link.
5. If still needed, power-cycle or replug the board.
6. Re-read the relevant flash header and compare with the expected bytes.

## PC-Side Test Interfaces

The test/control interface is project-specific. Common options:

| Interface | Notes |
| --- | --- |
| BLE GATT command protocol | Typical for DA14531 BLE products. Requires scan/connect/subscribe/write flow. |
| UART shell or binary protocol | Useful during bring-up; may use USB CDC or external USB-UART. |
| RTT/SWD logging | Requires debugger connection and project support. |
| Vendor SUOTA tooling | Used by projects that keep the SDK SUOTA architecture. |
| Custom PC tools | Python, C#, browser dashboard, or other host utilities. |
| Log-only output | Some first-board tests only expose status through logs or LEDs. |

For BLE tests, record:

- advertised name
- service UUID
- RX/control characteristic UUID
- TX/notify characteristic UUID
- expected MTU
- write type expectations
- command framing and CRC rules
- reset/reconnect behavior

For UART tests, record:

- COM port
- baud rate
- line ending
- shell prompt or binary framing
- reset behavior

## Regression Test Guidance

For any project, define at least three levels:

| Level | Purpose |
| --- | --- |
| Smoke | Confirms the device boots and the control link responds. |
| Normal regression | Exercises non-destructive commands and common measurement paths. |
| Disruptive regression | Exercises reboot, sleep, image update, recovery, flash erase, or destructive write paths. |

For image-update architectures, test:

1. Clean update from production.
2. Reboot into updated production image.
3. Bad or interrupted update.
4. Recovery/fallback behavior.
5. Recovery repair back to production, if supported.
6. Final smoke/regression after repair.

Keep destructive image-update tests separate from ordinary ICD/command
regression unless the flash layout has been prepared and verified first.

## Common Pitfalls

- Building from a copied folder while the Keil project expects SDK-relative
  paths.
- Programming a raw image where a bootable image is required.
- Programming a bootable image where a raw slot image is required.
- Assuming another DA14531 project uses the same flash layout.
- Assuming BLE, UART, SPI, I2C, or a shell exists before inspecting the project.
- Forgetting to verify the J-Link serial number on the current PC.
- Forgetting that SmartSnippets may leave its RAM programmer running until a
  final reset or power cycle.
- Treating a BLE reconnect failure as firmware failure before checking whether
  the device is advertising a different mode/name.
- Running destructive image-update tests without first verifying the recovery
  path.

## Minimal Handoff Template

When handing a DA14531 project to another engineer or test agent, provide:

```text
Project root:
Keil project:
Keil target:
SDK path:
Build command:
Main output image:
SmartSnippets path:
J-Link serial:
SPI flash size:
Flash map:
Programming commands:
Expected boot/advertising/log output:
PC test command:
Known warnings:
Recovery/reset procedure:
```
