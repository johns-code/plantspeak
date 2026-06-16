# Unit Test Plan

Project: PlantSpeak

Generated: 2026-06-16T04:39:11+00:00

| Test ID | Requirement | Status | Objective |
| --- | --- | --- | --- |
| UT-001 | SW-001 | Planned | Verify: The software shall implement: a single bootable image at `0x00000000` |
| UT-002 | SW-002 | Planned | Verify: The software shall implement: a boot manager plus one or more application slots |
| UT-003 | SW-003 | Planned | Verify: The software shall implement: a vendor SUOTA layout |
| UT-004 | SW-004 | Planned | Verify: The software shall implement: a custom recovery-loader layout |
| UT-005 | SW-005 | Planned | Verify: The software shall implement: a RAM-loaded debug image |
| UT-006 | SW-006 | Planned | Verify: The software shall implement: which folder is the authoritative project root? |
| UT-007 | SW-007 | Planned | Verify: The software shall implement: does the Keil project rely on relative paths into a DA14531 SDK tree? |
| UT-008 | SW-008 | Planned | Verify: The software shall implement: which Keil target should be built? |
| UT-009 | SW-009 | Planned | Verify: The software shall implement: is the output image raw, bootable, encrypted, signed, compressed, or slot-wrapped? |
| UT-010 | SW-010 | Planned | Verify: The software shall implement: does the board boot from external SPI flash, OTP, UART, or RAM? |
| UT-011 | SW-011 | Planned | Verify: The software shall implement: what is the SPI flash size? |
| UT-012 | SW-012 | Planned | Verify: The software shall implement: what is the expected flash map? |
| UT-013 | SW-013 | Planned | Verify: The software shall implement: is there a boot manager, secondary bootloader, SUOTA flow, or recovery app? |
| UT-014 | SW-014 | Planned | Verify: The software shall implement: which interface is used for testing: BLE, UART, RTT, SWD, USB CDC, log-only, or a vendor tool? |
| UT-015 | SW-015 | Planned | Verify: The software shall implement: what manual reset or power-cycle step is required after programming? |
| UT-016 | SW-016 | Planned | Verify: The software shall implement: open SmartSnippets Toolbox. |
| UT-017 | SW-017 | Planned | Verify: The software shall implement: select the board/chip family if needed. |
| UT-018 | SW-018 | Planned | Verify: The software shall implement: use `Board -> Detect device`. |
| UT-019 | SW-019 | Planned | Verify: The software shall implement: confirm the J-Link/debug interface and any CDC UART port. |
| UT-020 | SW-020 | Planned | Verify: The software shall implement: open the project `.uvprojx` in Keil uVision. |
| UT-021 | SW-021 | Planned | Verify: The software shall implement: select the intended target. |
| UT-022 | SW-022 | Planned | Verify: The software shall implement: build or rebuild. |
| UT-023 | SW-023 | Planned | Verify: The software shall implement: confirm the expected `.axf`, `.bin`, or `.hex` output was generated. |
| UT-024 | SW-024 | Planned | Verify: The software shall implement: check the build log for warnings, image size, RAM usage, and post-build |
| UT-025 | SW-025 | Planned | Verify: The software shall implement: connect to DA14531 through J-Link/SWD. |
| UT-026 | SW-026 | Planned | Verify: The software shall implement: download a temporary DA1453x SPI programmer into DA14531 RAM. |
| UT-027 | SW-027 | Planned | Verify: The software shall implement: use that RAM program to access external SPI flash. |
| UT-028 | SW-028 | Planned | Verify: The software shall implement: erase, write, read, or verify flash. |
| UT-029 | SW-029 | Planned | Verify: The software shall implement: optionally add a DA14531 bootable-image header. |
| UT-030 | SW-030 | Planned | Verify: The software shall implement: reset the device after programming. |
| UT-031 | SW-031 | Planned | Verify: The software shall implement: running the temporary SmartSnippets RAM programmer |
| UT-032 | SW-032 | Planned | Verify: The software shall implement: reset into the newly programmed SPI image |
| UT-033 | SW-033 | Planned | Verify: The software shall implement: halted by the debugger |
| UT-034 | SW-034 | Planned | Verify: The software shall implement: waiting for a manual power cycle |
| UT-035 | SW-035 | Planned | Verify: The software shall implement: advertising over BLE |
| UT-036 | SW-036 | Planned | Verify: The software shall implement: silent because the programmed image is not valid for the selected boot path |
| UT-037 | SW-037 | Planned | Verify: The software shall implement: confirm the write and verify succeeded. |
| UT-038 | SW-038 | Planned | Verify: The software shall implement: confirm the image was programmed at the correct offset. |
| UT-039 | SW-039 | Planned | Verify: The software shall implement: confirm the file was written in the correct mode (`-bootable` vs raw). |
| UT-040 | SW-040 | Planned | Verify: The software shall implement: reset through SmartSnippets/J-Link. |
| UT-041 | SW-041 | Planned | Verify: The software shall implement: if still needed, power-cycle or replug the board. |
| UT-042 | SW-042 | Planned | Verify: The software shall implement: re-read the relevant flash header and compare with the expected bytes. |
| UT-043 | SW-043 | Planned | Verify: The software shall implement: advertised name |
| UT-044 | SW-044 | Planned | Verify: The software shall implement: service UUID |
| UT-045 | SW-045 | Planned | Verify: The software shall implement: rX/control characteristic UUID |
| UT-046 | SW-046 | Planned | Verify: The software shall implement: tX/notify characteristic UUID |
| UT-047 | SW-047 | Planned | Verify: The software shall implement: expected MTU |
| UT-048 | SW-048 | Planned | Verify: The software shall implement: write type expectations |
| UT-049 | SW-049 | Planned | Verify: The software shall implement: command framing and CRC rules |
| UT-050 | SW-050 | Planned | Verify: The software shall implement: reset/reconnect behavior |
| UT-051 | SW-051 | Planned | Verify: The software shall implement: cOM port |
| UT-052 | SW-052 | Planned | Verify: The software shall implement: baud rate |
| UT-053 | SW-053 | Planned | Verify: The software shall implement: line ending |
| UT-054 | SW-054 | Planned | Verify: The software shall implement: shell prompt or binary framing |
| UT-055 | SW-055 | Planned | Verify: The software shall implement: reset behavior |
| UT-056 | SW-056 | Planned | Verify: The software shall implement: clean update from production. |
| UT-057 | SW-057 | Planned | Verify: The software shall implement: reboot into updated production image. |
| UT-058 | SW-058 | Planned | Verify: The software shall implement: bad or interrupted update. |
| UT-059 | SW-059 | Planned | Verify: The software shall implement: recovery/fallback behavior. |
| UT-060 | SW-060 | Planned | Verify: The software shall implement: recovery repair back to production, if supported. |
| UT-061 | SW-061 | Planned | Verify: The software shall implement: final smoke/regression after repair. |
| UT-062 | SW-062 | Planned | Verify: The software shall implement: building from a copied folder while the Keil project expects SDK-relative |
| UT-063 | SW-063 | Planned | Verify: The software shall implement: programming a raw image where a bootable image is required. |
| UT-064 | SW-064 | Planned | Verify: The software shall implement: programming a bootable image where a raw slot image is required. |
| UT-065 | SW-065 | Planned | Verify: The software shall implement: assuming another DA14531 project uses the same flash layout. |
| UT-066 | SW-066 | Planned | Verify: The software shall implement: assuming BLE, UART, SPI, I2C, or a shell exists before inspecting the project. |
| UT-067 | SW-067 | Planned | Verify: The software shall implement: forgetting to verify the J-Link serial number on the current PC. |
| UT-068 | SW-068 | Planned | Verify: The software shall implement: forgetting that SmartSnippets may leave its RAM programmer running until a |
| UT-069 | SW-069 | Planned | Verify: The software shall implement: treating a BLE reconnect failure as firmware failure before checking whether |
| UT-070 | SW-070 | Planned | Verify: The software shall implement: running destructive image-update tests without first verifying the recovery |
| UT-071 | SW-071 | Planned | Verify: The software shall implement: roles and Transport |
| UT-072 | SW-072 | Planned | Verify: The software shall implement: frame Format |
| UT-073 | SW-073 | Planned | Verify: The software shall implement: production Command Set |
| UT-074 | SW-074 | Planned | Verify: The software shall implement: status and Measurement Payloads |
| UT-075 | SW-075 | Planned | Verify: The software shall implement: wavelengths, PPFD, Calibration, and LED Currents |
| UT-076 | SW-076 | Planned | Verify: The software shall implement: diagnostic Flash Log |
| UT-077 | SW-077 | Planned | Verify: The software shall implement: firmware Update and Recovery |
| UT-078 | SW-078 | Planned | Verify: The software shall implement: recommended SmartDevice Flows |
| UT-079 | SW-079 | Planned | Verify: The software shall implement: security and Policy Notes |
