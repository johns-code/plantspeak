# Acceptance Test Plan

Project: PlantSpeak

Generated: 2026-06-16T05:38:54+00:00

| Test ID | Requirement | Status | Objective |
| --- | --- | --- | --- |
| AT-001 | SW-001 | Planned | Verify: The software shall implement: a single bootable image at `0x00000000` |
| AT-002 | SW-002 | Planned | Verify: The software shall implement: a boot manager plus one or more application slots |
| AT-003 | SW-003 | Planned | Verify: The software shall implement: a vendor SUOTA layout |
| AT-004 | SW-004 | Planned | Verify: The software shall implement: a custom recovery-loader layout |
| AT-005 | SW-005 | Planned | Verify: The software shall implement: a RAM-loaded debug image |
| AT-006 | SW-006 | Planned | Verify: The software shall implement: which folder is the authoritative project root? |
| AT-007 | SW-007 | Planned | Verify: The software shall implement: does the Keil project rely on relative paths into a DA14531 SDK tree? |
| AT-008 | SW-008 | Planned | Verify: The software shall implement: which Keil target should be built? |
| AT-009 | SW-009 | Planned | Verify: The software shall implement: is the output image raw, bootable, encrypted, signed, compressed, or slot-wrapped? |
| AT-010 | SW-010 | Planned | Verify: The software shall implement: does the board boot from external SPI flash, OTP, UART, or RAM? |
| AT-011 | SW-011 | Planned | Verify: The software shall implement: what is the SPI flash size? |
| AT-012 | SW-012 | Planned | Verify: The software shall implement: what is the expected flash map? |
| AT-013 | SW-013 | Planned | Verify: The software shall implement: is there a boot manager, secondary bootloader, SUOTA flow, or recovery app? |
| AT-014 | SW-014 | Planned | Verify: The software shall implement: which interface is used for testing: BLE, UART, RTT, SWD, USB CDC, log-only, or a vendor tool? |
| AT-015 | SW-015 | Planned | Verify: The software shall implement: what manual reset or power-cycle step is required after programming? |
| AT-016 | SW-016 | Planned | Verify: The software shall implement: open SmartSnippets Toolbox. |
| AT-017 | SW-017 | Planned | Verify: The software shall implement: select the board/chip family if needed. |
| AT-018 | SW-018 | Planned | Verify: The software shall implement: use `Board -> Detect device`. |
| AT-019 | SW-019 | Planned | Verify: The software shall implement: confirm the J-Link/debug interface and any CDC UART port. |
| AT-020 | SW-020 | Planned | Verify: The software shall implement: open the project `.uvprojx` in Keil uVision. |
| AT-021 | SW-021 | Planned | Verify: The software shall implement: select the intended target. |
| AT-022 | SW-022 | Planned | Verify: The software shall implement: build or rebuild. |
| AT-023 | SW-023 | Planned | Verify: The software shall implement: confirm the expected `.axf`, `.bin`, or `.hex` output was generated. |
| AT-024 | SW-024 | Planned | Verify: The software shall implement: check the build log for warnings, image size, RAM usage, and post-build |
| AT-025 | SW-025 | Planned | Verify: The software shall implement: connect to DA14531 through J-Link/SWD. |
| AT-026 | SW-026 | Planned | Verify: The software shall implement: download a temporary DA1453x SPI programmer into DA14531 RAM. |
| AT-027 | SW-027 | Planned | Verify: The software shall implement: use that RAM program to access external SPI flash. |
| AT-028 | SW-028 | Planned | Verify: The software shall implement: erase, write, read, or verify flash. |
| AT-029 | SW-029 | Planned | Verify: The software shall implement: optionally add a DA14531 bootable-image header. |
| AT-030 | SW-030 | Planned | Verify: The software shall implement: reset the device after programming. |
| AT-031 | SW-031 | Planned | Verify: The software shall implement: running the temporary SmartSnippets RAM programmer |
| AT-032 | SW-032 | Planned | Verify: The software shall implement: reset into the newly programmed SPI image |
| AT-033 | SW-033 | Planned | Verify: The software shall implement: halted by the debugger |
| AT-034 | SW-034 | Planned | Verify: The software shall implement: waiting for a manual power cycle |
| AT-035 | SW-035 | Planned | Verify: The software shall implement: advertising over BLE |
| AT-036 | SW-036 | Planned | Verify: The software shall implement: silent because the programmed image is not valid for the selected boot path |
| AT-037 | SW-037 | Planned | Verify: The software shall implement: confirm the write and verify succeeded. |
| AT-038 | SW-038 | Planned | Verify: The software shall implement: confirm the image was programmed at the correct offset. |
| AT-039 | SW-039 | Planned | Verify: The software shall implement: confirm the file was written in the correct mode (`-bootable` vs raw). |
| AT-040 | SW-040 | Planned | Verify: The software shall implement: reset through SmartSnippets/J-Link. |
| AT-041 | SW-041 | Planned | Verify: The software shall implement: if still needed, power-cycle or replug the board. |
| AT-042 | SW-042 | Planned | Verify: The software shall implement: re-read the relevant flash header and compare with the expected bytes. |
| AT-043 | SW-043 | Planned | Verify: The software shall implement: advertised name |
| AT-044 | SW-044 | Planned | Verify: The software shall implement: service UUID |
| AT-045 | SW-045 | Planned | Verify: The software shall implement: rX/control characteristic UUID |
| AT-046 | SW-046 | Planned | Verify: The software shall implement: tX/notify characteristic UUID |
| AT-047 | SW-047 | Planned | Verify: The software shall implement: expected MTU |
| AT-048 | SW-048 | Planned | Verify: The software shall implement: write type expectations |
| AT-049 | SW-049 | Planned | Verify: The software shall implement: command framing and CRC rules |
| AT-050 | SW-050 | Planned | Verify: The software shall implement: reset/reconnect behavior |
| AT-051 | SW-051 | Planned | Verify: The software shall implement: cOM port |
| AT-052 | SW-052 | Planned | Verify: The software shall implement: baud rate |
| AT-053 | SW-053 | Planned | Verify: The software shall implement: line ending |
| AT-054 | SW-054 | Planned | Verify: The software shall implement: shell prompt or binary framing |
| AT-055 | SW-055 | Planned | Verify: The software shall implement: reset behavior |
| AT-056 | SW-056 | Planned | Verify: The software shall implement: clean update from production. |
| AT-057 | SW-057 | Planned | Verify: The software shall implement: reboot into updated production image. |
| AT-058 | SW-058 | Planned | Verify: The software shall implement: bad or interrupted update. |
| AT-059 | SW-059 | Planned | Verify: The software shall implement: recovery/fallback behavior. |
| AT-060 | SW-060 | Planned | Verify: The software shall implement: recovery repair back to production, if supported. |
| AT-061 | SW-061 | Planned | Verify: The software shall implement: final smoke/regression after repair. |
| AT-062 | SW-062 | Planned | Verify: The software shall implement: building from a copied folder while the Keil project expects SDK-relative |
| AT-063 | SW-063 | Planned | Verify: The software shall implement: programming a raw image where a bootable image is required. |
| AT-064 | SW-064 | Planned | Verify: The software shall implement: programming a bootable image where a raw slot image is required. |
| AT-065 | SW-065 | Planned | Verify: The software shall implement: assuming another DA14531 project uses the same flash layout. |
| AT-066 | SW-066 | Planned | Verify: The software shall implement: assuming BLE, UART, SPI, I2C, or a shell exists before inspecting the project. |
| AT-067 | SW-067 | Planned | Verify: The software shall implement: forgetting to verify the J-Link serial number on the current PC. |
| AT-068 | SW-068 | Planned | Verify: The software shall implement: forgetting that SmartSnippets may leave its RAM programmer running until a |
| AT-069 | SW-069 | Planned | Verify: The software shall implement: treating a BLE reconnect failure as firmware failure before checking whether |
| AT-070 | SW-070 | Planned | Verify: The software shall implement: running destructive image-update tests without first verifying the recovery |
| AT-071 | SW-071 | Planned | Verify: The software shall implement: roles and Transport |
| AT-072 | SW-072 | Planned | Verify: The software shall implement: frame Format |
| AT-073 | SW-073 | Planned | Verify: The software shall implement: production Command Set |
| AT-074 | SW-074 | Planned | Verify: The software shall implement: status and Measurement Payloads |
| AT-075 | SW-075 | Planned | Verify: The software shall implement: wavelengths, PPFD, Calibration, and LED Currents |
| AT-076 | SW-076 | Planned | Verify: The software shall implement: diagnostic Flash Log |
| AT-077 | SW-077 | Planned | Verify: The software shall implement: firmware Update and Recovery |
| AT-078 | SW-078 | Planned | Verify: The software shall implement: recommended SmartDevice Flows |
| AT-079 | SW-079 | Planned | Verify: The software shall implement: security and Policy Notes |
| AT-080 | SW-080 | Planned | Verify: The software shall implement: the red/green user LEDs mentioned in the ICD are controlled via P0_5 and P0_11 |
| AT-081 | SW-081 | Planned | Verify: The software shall implement: the user push button is on P0_10 |
| AT-082 | SW-082 | Planned | Verify: The software shall implement: eN_Peripherals is on P0_6 |
| AT-083 | SW-083 | Planned | Verify: The software shall implement: i2C SCL is on P0_8 and SDA on P0_9 |
| AT-084 | SW-084 | Planned | Verify: The software shall implement: the photodiode current is read by the ADS1115IDGSR. AIN0 is for reading the PD current for all the external LEDs (that is, in a measurement each wavelength an LED is turns on and the signal is read on AIN0 in all LED cases) AIN1 is signal for PPFD signal |
| AT-085 | SW-085 | Planned | Verify: The software shall implement: the wavelength LEDs are driven by LP5816 hanging off the PCA9846PWJ. LED1/2/3/4 are on the LP5816 on channel SC1/SD1 the PCA9846PWJ with LEDs 5/6 are on the LP5816 on channel SC2/SD2 on the PCA9846PWJ |
| AT-086 | SW-086 | Planned | Verify: The software shall implement: leaf temperature is on MLX90632SLD-BCB-000-RE connected to SC0/SD0 on the PCA9846PWJ |
| AT-087 | SW-087 | Planned | Verify: The software shall implement: rH and ambient temp are read from HDC2010YPAR using DA14531 I2C bus |
| AT-088 | SW-088 | Planned | Verify: The software shall implement: accelerometer is from MXC4005XC using DA14531 I2C bus |
| AT-089 | SW-089 | Planned | Verify: The software shall implement: red/green user LEDs not available - can use dev board LED for initial dev work and testing |
| AT-090 | SW-090 | Planned | Verify: The software shall implement: eN_Peripherals no avaiable |
| AT-091 | SW-091 | Planned | Verify: The software shall implement: all external I2C devices not available (so use canned data for testing but again still develop hanrdware interfaces to do real work when target board comes) |
| AT-092 | SW-092 | Planned | Verify: The software shall implement: user push button not available |
