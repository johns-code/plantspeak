# User Needs Document

Project: PlantSpeak

Generated: 2026-06-16T04:39:11+00:00

| ID | Need | Rationale |
| --- | --- | --- |
| UN-001 | a single bootable image at `0x00000000` | Captured from the submitted high-level requirements brief. |
| UN-002 | a boot manager plus one or more application slots | Captured from the submitted high-level requirements brief. |
| UN-003 | a vendor SUOTA layout | Captured from the submitted high-level requirements brief. |
| UN-004 | a custom recovery-loader layout | Captured from the submitted high-level requirements brief. |
| UN-005 | a RAM-loaded debug image | Captured from the submitted high-level requirements brief. |
| UN-006 | which folder is the authoritative project root? | Captured from the submitted high-level requirements brief. |
| UN-007 | does the Keil project rely on relative paths into a DA14531 SDK tree? | Captured from the submitted high-level requirements brief. |
| UN-008 | which Keil target should be built? | Captured from the submitted high-level requirements brief. |
| UN-009 | is the output image raw, bootable, encrypted, signed, compressed, or slot-wrapped? | Captured from the submitted high-level requirements brief. |
| UN-010 | does the board boot from external SPI flash, OTP, UART, or RAM? | Captured from the submitted high-level requirements brief. |
| UN-011 | what is the SPI flash size? | Captured from the submitted high-level requirements brief. |
| UN-012 | what is the expected flash map? | Captured from the submitted high-level requirements brief. |
| UN-013 | is there a boot manager, secondary bootloader, SUOTA flow, or recovery app? | Captured from the submitted high-level requirements brief. |
| UN-014 | which interface is used for testing: BLE, UART, RTT, SWD, USB CDC, log-only, or a vendor tool? | Captured from the submitted high-level requirements brief. |
| UN-015 | what manual reset or power-cycle step is required after programming? | Captured from the submitted high-level requirements brief. |
| UN-016 | open SmartSnippets Toolbox. | Captured from the submitted high-level requirements brief. |
| UN-017 | select the board/chip family if needed. | Captured from the submitted high-level requirements brief. |
| UN-018 | use `Board -> Detect device`. | Captured from the submitted high-level requirements brief. |
| UN-019 | confirm the J-Link/debug interface and any CDC UART port. | Captured from the submitted high-level requirements brief. |
| UN-020 | open the project `.uvprojx` in Keil uVision. | Captured from the submitted high-level requirements brief. |
| UN-021 | select the intended target. | Captured from the submitted high-level requirements brief. |
| UN-022 | build or rebuild. | Captured from the submitted high-level requirements brief. |
| UN-023 | confirm the expected `.axf`, `.bin`, or `.hex` output was generated. | Captured from the submitted high-level requirements brief. |
| UN-024 | check the build log for warnings, image size, RAM usage, and post-build | Captured from the submitted high-level requirements brief. |
| UN-025 | connect to DA14531 through J-Link/SWD. | Captured from the submitted high-level requirements brief. |
| UN-026 | download a temporary DA1453x SPI programmer into DA14531 RAM. | Captured from the submitted high-level requirements brief. |
| UN-027 | use that RAM program to access external SPI flash. | Captured from the submitted high-level requirements brief. |
| UN-028 | erase, write, read, or verify flash. | Captured from the submitted high-level requirements brief. |
| UN-029 | optionally add a DA14531 bootable-image header. | Captured from the submitted high-level requirements brief. |
| UN-030 | reset the device after programming. | Captured from the submitted high-level requirements brief. |
| UN-031 | running the temporary SmartSnippets RAM programmer | Captured from the submitted high-level requirements brief. |
| UN-032 | reset into the newly programmed SPI image | Captured from the submitted high-level requirements brief. |
| UN-033 | halted by the debugger | Captured from the submitted high-level requirements brief. |
| UN-034 | waiting for a manual power cycle | Captured from the submitted high-level requirements brief. |
| UN-035 | advertising over BLE | Captured from the submitted high-level requirements brief. |
| UN-036 | silent because the programmed image is not valid for the selected boot path | Captured from the submitted high-level requirements brief. |
| UN-037 | confirm the write and verify succeeded. | Captured from the submitted high-level requirements brief. |
| UN-038 | confirm the image was programmed at the correct offset. | Captured from the submitted high-level requirements brief. |
| UN-039 | confirm the file was written in the correct mode (`-bootable` vs raw). | Captured from the submitted high-level requirements brief. |
| UN-040 | reset through SmartSnippets/J-Link. | Captured from the submitted high-level requirements brief. |
| UN-041 | if still needed, power-cycle or replug the board. | Captured from the submitted high-level requirements brief. |
| UN-042 | re-read the relevant flash header and compare with the expected bytes. | Captured from the submitted high-level requirements brief. |
| UN-043 | advertised name | Captured from the submitted high-level requirements brief. |
| UN-044 | service UUID | Captured from the submitted high-level requirements brief. |
| UN-045 | rX/control characteristic UUID | Captured from the submitted high-level requirements brief. |
| UN-046 | tX/notify characteristic UUID | Captured from the submitted high-level requirements brief. |
| UN-047 | expected MTU | Captured from the submitted high-level requirements brief. |
| UN-048 | write type expectations | Captured from the submitted high-level requirements brief. |
| UN-049 | command framing and CRC rules | Captured from the submitted high-level requirements brief. |
| UN-050 | reset/reconnect behavior | Captured from the submitted high-level requirements brief. |
| UN-051 | cOM port | Captured from the submitted high-level requirements brief. |
| UN-052 | baud rate | Captured from the submitted high-level requirements brief. |
| UN-053 | line ending | Captured from the submitted high-level requirements brief. |
| UN-054 | shell prompt or binary framing | Captured from the submitted high-level requirements brief. |
| UN-055 | reset behavior | Captured from the submitted high-level requirements brief. |
| UN-056 | clean update from production. | Captured from the submitted high-level requirements brief. |
| UN-057 | reboot into updated production image. | Captured from the submitted high-level requirements brief. |
| UN-058 | bad or interrupted update. | Captured from the submitted high-level requirements brief. |
| UN-059 | recovery/fallback behavior. | Captured from the submitted high-level requirements brief. |
| UN-060 | recovery repair back to production, if supported. | Captured from the submitted high-level requirements brief. |
| UN-061 | final smoke/regression after repair. | Captured from the submitted high-level requirements brief. |
| UN-062 | building from a copied folder while the Keil project expects SDK-relative | Captured from the submitted high-level requirements brief. |
| UN-063 | programming a raw image where a bootable image is required. | Captured from the submitted high-level requirements brief. |
| UN-064 | programming a bootable image where a raw slot image is required. | Captured from the submitted high-level requirements brief. |
| UN-065 | assuming another DA14531 project uses the same flash layout. | Captured from the submitted high-level requirements brief. |
| UN-066 | assuming BLE, UART, SPI, I2C, or a shell exists before inspecting the project. | Captured from the submitted high-level requirements brief. |
| UN-067 | forgetting to verify the J-Link serial number on the current PC. | Captured from the submitted high-level requirements brief. |
| UN-068 | forgetting that SmartSnippets may leave its RAM programmer running until a | Captured from the submitted high-level requirements brief. |
| UN-069 | treating a BLE reconnect failure as firmware failure before checking whether | Captured from the submitted high-level requirements brief. |
| UN-070 | running destructive image-update tests without first verifying the recovery | Captured from the submitted high-level requirements brief. |
| UN-071 | roles and Transport | Captured from the submitted high-level requirements brief. |
| UN-072 | frame Format | Captured from the submitted high-level requirements brief. |
| UN-073 | production Command Set | Captured from the submitted high-level requirements brief. |
| UN-074 | status and Measurement Payloads | Captured from the submitted high-level requirements brief. |
| UN-075 | wavelengths, PPFD, Calibration, and LED Currents | Captured from the submitted high-level requirements brief. |
| UN-076 | diagnostic Flash Log | Captured from the submitted high-level requirements brief. |
| UN-077 | firmware Update and Recovery | Captured from the submitted high-level requirements brief. |
| UN-078 | recommended SmartDevice Flows | Captured from the submitted high-level requirements brief. |
| UN-079 | security and Policy Notes | Captured from the submitted high-level requirements brief. |
