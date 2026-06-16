# System Test Plan

Project: PlantSpeak

Generated: 2026-06-16T04:39:11+00:00

| Test ID | Requirement | Status | Objective |
| --- | --- | --- | --- |
| ST-001 | SW-001 | Planned | Verify: The software shall implement: a single bootable image at `0x00000000` |
| ST-002 | SW-002 | Planned | Verify: The software shall implement: a boot manager plus one or more application slots |
| ST-003 | SW-003 | Planned | Verify: The software shall implement: a vendor SUOTA layout |
| ST-004 | SW-004 | Planned | Verify: The software shall implement: a custom recovery-loader layout |
| ST-005 | SW-005 | Planned | Verify: The software shall implement: a RAM-loaded debug image |
| ST-006 | SW-006 | Planned | Verify: The software shall implement: which folder is the authoritative project root? |
| ST-007 | SW-007 | Planned | Verify: The software shall implement: does the Keil project rely on relative paths into a DA14531 SDK tree? |
| ST-008 | SW-008 | Planned | Verify: The software shall implement: which Keil target should be built? |
| ST-009 | SW-009 | Planned | Verify: The software shall implement: is the output image raw, bootable, encrypted, signed, compressed, or slot-wrapped? |
| ST-010 | SW-010 | Planned | Verify: The software shall implement: does the board boot from external SPI flash, OTP, UART, or RAM? |
| ST-011 | SW-011 | Planned | Verify: The software shall implement: what is the SPI flash size? |
| ST-012 | SW-012 | Planned | Verify: The software shall implement: what is the expected flash map? |
| ST-013 | SW-013 | Planned | Verify: The software shall implement: is there a boot manager, secondary bootloader, SUOTA flow, or recovery app? |
| ST-014 | SW-014 | Planned | Verify: The software shall implement: which interface is used for testing: BLE, UART, RTT, SWD, USB CDC, log-only, or a vendor tool? |
| ST-015 | SW-015 | Planned | Verify: The software shall implement: what manual reset or power-cycle step is required after programming? |
| ST-016 | SW-016 | Planned | Verify: The software shall implement: open SmartSnippets Toolbox. |
| ST-017 | SW-017 | Planned | Verify: The software shall implement: select the board/chip family if needed. |
| ST-018 | SW-018 | Planned | Verify: The software shall implement: use `Board -> Detect device`. |
| ST-019 | SW-019 | Planned | Verify: The software shall implement: confirm the J-Link/debug interface and any CDC UART port. |
| ST-020 | SW-020 | Planned | Verify: The software shall implement: open the project `.uvprojx` in Keil uVision. |
| ST-021 | SW-021 | Planned | Verify: The software shall implement: select the intended target. |
| ST-022 | SW-022 | Planned | Verify: The software shall implement: build or rebuild. |
| ST-023 | SW-023 | Planned | Verify: The software shall implement: confirm the expected `.axf`, `.bin`, or `.hex` output was generated. |
| ST-024 | SW-024 | Planned | Verify: The software shall implement: check the build log for warnings, image size, RAM usage, and post-build |
| ST-025 | SW-025 | Planned | Verify: The software shall implement: connect to DA14531 through J-Link/SWD. |
| ST-026 | SW-026 | Planned | Verify: The software shall implement: download a temporary DA1453x SPI programmer into DA14531 RAM. |
| ST-027 | SW-027 | Planned | Verify: The software shall implement: use that RAM program to access external SPI flash. |
| ST-028 | SW-028 | Planned | Verify: The software shall implement: erase, write, read, or verify flash. |
| ST-029 | SW-029 | Planned | Verify: The software shall implement: optionally add a DA14531 bootable-image header. |
| ST-030 | SW-030 | Planned | Verify: The software shall implement: reset the device after programming. |
| ST-031 | SW-031 | Planned | Verify: The software shall implement: running the temporary SmartSnippets RAM programmer |
| ST-032 | SW-032 | Planned | Verify: The software shall implement: reset into the newly programmed SPI image |
| ST-033 | SW-033 | Planned | Verify: The software shall implement: halted by the debugger |
| ST-034 | SW-034 | Planned | Verify: The software shall implement: waiting for a manual power cycle |
| ST-035 | SW-035 | Planned | Verify: The software shall implement: advertising over BLE |
| ST-036 | SW-036 | Planned | Verify: The software shall implement: silent because the programmed image is not valid for the selected boot path |
| ST-037 | SW-037 | Planned | Verify: The software shall implement: confirm the write and verify succeeded. |
| ST-038 | SW-038 | Planned | Verify: The software shall implement: confirm the image was programmed at the correct offset. |
| ST-039 | SW-039 | Planned | Verify: The software shall implement: confirm the file was written in the correct mode (`-bootable` vs raw). |
| ST-040 | SW-040 | Planned | Verify: The software shall implement: reset through SmartSnippets/J-Link. |
| ST-041 | SW-041 | Planned | Verify: The software shall implement: if still needed, power-cycle or replug the board. |
| ST-042 | SW-042 | Planned | Verify: The software shall implement: re-read the relevant flash header and compare with the expected bytes. |
| ST-043 | SW-043 | Planned | Verify: The software shall implement: advertised name |
| ST-044 | SW-044 | Planned | Verify: The software shall implement: service UUID |
| ST-045 | SW-045 | Planned | Verify: The software shall implement: rX/control characteristic UUID |
| ST-046 | SW-046 | Planned | Verify: The software shall implement: tX/notify characteristic UUID |
| ST-047 | SW-047 | Planned | Verify: The software shall implement: expected MTU |
| ST-048 | SW-048 | Planned | Verify: The software shall implement: write type expectations |
| ST-049 | SW-049 | Planned | Verify: The software shall implement: command framing and CRC rules |
| ST-050 | SW-050 | Planned | Verify: The software shall implement: reset/reconnect behavior |
| ST-051 | SW-051 | Planned | Verify: The software shall implement: cOM port |
| ST-052 | SW-052 | Planned | Verify: The software shall implement: baud rate |
| ST-053 | SW-053 | Planned | Verify: The software shall implement: line ending |
| ST-054 | SW-054 | Planned | Verify: The software shall implement: shell prompt or binary framing |
| ST-055 | SW-055 | Planned | Verify: The software shall implement: reset behavior |
| ST-056 | SW-056 | Planned | Verify: The software shall implement: clean update from production. |
| ST-057 | SW-057 | Planned | Verify: The software shall implement: reboot into updated production image. |
| ST-058 | SW-058 | Planned | Verify: The software shall implement: bad or interrupted update. |
| ST-059 | SW-059 | Planned | Verify: The software shall implement: recovery/fallback behavior. |
| ST-060 | SW-060 | Planned | Verify: The software shall implement: recovery repair back to production, if supported. |
| ST-061 | SW-061 | Planned | Verify: The software shall implement: final smoke/regression after repair. |
| ST-062 | SW-062 | Planned | Verify: The software shall implement: building from a copied folder while the Keil project expects SDK-relative |
| ST-063 | SW-063 | Planned | Verify: The software shall implement: programming a raw image where a bootable image is required. |
| ST-064 | SW-064 | Planned | Verify: The software shall implement: programming a bootable image where a raw slot image is required. |
| ST-065 | SW-065 | Planned | Verify: The software shall implement: assuming another DA14531 project uses the same flash layout. |
| ST-066 | SW-066 | Planned | Verify: The software shall implement: assuming BLE, UART, SPI, I2C, or a shell exists before inspecting the project. |
| ST-067 | SW-067 | Planned | Verify: The software shall implement: forgetting to verify the J-Link serial number on the current PC. |
| ST-068 | SW-068 | Planned | Verify: The software shall implement: forgetting that SmartSnippets may leave its RAM programmer running until a |
| ST-069 | SW-069 | Planned | Verify: The software shall implement: treating a BLE reconnect failure as firmware failure before checking whether |
| ST-070 | SW-070 | Planned | Verify: The software shall implement: running destructive image-update tests without first verifying the recovery |
| ST-071 | SW-071 | Planned | Verify: The software shall implement: roles and Transport |
| ST-072 | SW-072 | Planned | Verify: The software shall implement: frame Format |
| ST-073 | SW-073 | Planned | Verify: The software shall implement: production Command Set |
| ST-074 | SW-074 | Planned | Verify: The software shall implement: status and Measurement Payloads |
| ST-075 | SW-075 | Planned | Verify: The software shall implement: wavelengths, PPFD, Calibration, and LED Currents |
| ST-076 | SW-076 | Planned | Verify: The software shall implement: diagnostic Flash Log |
| ST-077 | SW-077 | Planned | Verify: The software shall implement: firmware Update and Recovery |
| ST-078 | SW-078 | Planned | Verify: The software shall implement: recommended SmartDevice Flows |
| ST-079 | SW-079 | Planned | Verify: The software shall implement: security and Policy Notes |
