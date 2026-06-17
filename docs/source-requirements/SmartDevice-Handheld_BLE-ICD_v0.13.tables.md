## Table 0
| Item | Value |
| Applies to | DA14531MOD-based P531 handheld wand and companion SmartDevice application |
| Production BLE name | P531-Handheld |
| Recovery BLE name | P531-Recovery |
| Protocol version | 0x01 |
| Updated for | DEVICE_INFO_SET, PPFD calibration index 6, averaging limits, six wavelength channels, recovery/update flow, flash diagnostic logging, and MTU67 write support with 20-byte TX notification fragments |

## Table 1
| As-built scope: this document describes the current target branch implementation. Reserved commands/events from earlier drafts are omitted unless implemented. Image update regression is handled separately from normal ICD regression because full image transfer is slow. |

## Table 2
| Advertised state | BLE local name | Meaning | SmartDevice expectation |
| Production application | P531-Handheld | Normal measurement/calibration firmware is running. | Use full command set in this document. |
| Recovery application | P531-Recovery | Minimal recovery firmware is running and ready for image update. | Use PING, GET_INFO, IMAGE_BEGIN, IMAGE_DATA, IMAGE_END, and REBOOT. Other opcodes may return UNKNOWN_OPCODE. |

## Table 3
| Field | Offset | Size | Type | Description |
| VER | 0 | 1 | u8 | Protocol version. Current value: 0x01. |
| OPC | 1 | 1 | u8 | Command opcode or event opcode. |
| FLAGS | 2 | 1 | u8 | b0 FragStart reserved, b1 FragCont reserved, b2 Resp, b3 AckReq reserved. |
| SEQ | 3 | 1 | u8 | SmartDevice-selected sequence value. Responses echo this value. |
| LEN | 4 | 2 | u16le | Payload length in bytes. Response payloads include RET as byte 0. |
| PAYLOAD | 6 | LEN | bytes | Command-specific payload. Requests do not include RET. Responses always begin with RET. |
| CRC16 | 6+LEN | 2 | u16le | CRC-16/X25 over VER..PAYLOAD. |

## Table 4
| RET | Name | Meaning |
| 0x00 | OK | Command accepted/completed. |
| 0x01 | UNKNOWN_OPCODE | Opcode not implemented in the current advertised state. |
| 0x02 | BAD_PARAM | Payload length or field value invalid. |
| 0x03 | BUSY | Device busy. |
| 0x04 | NOT_READY | Required state is missing, for example peripheral power is off before START_MEAS. |
| 0x05 | DENIED | Rejected by security/policy. |
| 0x06 | CRC_FAIL | Frame CRC mismatch. |
| 0x07 | TIMEOUT | Operation timeout. |
| 0x08 | TOO_LONG | Payload too long. |
| 0x09 | UNSUPPORTED | Valid field not supported by this build. |
| 0x0A | LOW_POWER_GUARD | Rejected by low-power guard. |

## Table 5
| OPC | Name | Request | Response | Notes |
| 0x01 | PING | - | RET, UPTIME_MS:u32 | Liveness check. |
| 0x02 | GET_INFO | - | RET, FW_VER[3], HW_REV:u8, SERIAL:u32, BUILD_ID:u32 | SERIAL/HW_REV come from provisioned flash identity. |
| 0x03 | GET_STATUS | - | RET, status struct | See Section 4. |
| 0x04 | SET_TIME | EPOCH_S:u32 | RET | Sets handheld time base used by status/log timestamps. |
| 0x05 | SET_RED_LED | MODE:u8, PERIOD_100MS:u16, DUTY_PCT:u8 | RET | MODE: 0 off, 1 on, 2 blink. |
| 0x06 | SET_GREEN_LED | MODE:u8, PERIOD_100MS:u16, DUTY_PCT:u8 | RET | MODE: 0 off, 1 on, 2 blink. |
| 0x07 | SET_PERIPH_POWER | EN:u8 (0/1) | RET | Must be ON before START_MEAS. Logs power transitions. |
| 0x08 | REBOOT | - | RET then disconnect/reset | Commits pending verified image before reset. |
| 0x09 | ENTER_DEEP_SLEEP | - | RET then sleep | Target-board wake validation deferred; dev-board wake is not authoritative. |
| 0x0A | DEVICE_INFO_SET | HW_REV:u8, SERIAL:u32 | RET | Manufacturing/calibration provisioning. Rejects SERIAL=0xFFFFFFFF. |
| 0x10 | START_MEAS | MODE:u8, COUNT:u16, INTERVAL_MS:u16, MEAS_AVG:u8, FLAGS:u8 | RET, measurement frame | Only MODE=0 ONESHOT implemented. Requires peripheral power ON. |
| 0x14 | LOG_GET | START_IDX:u16, MAX_ITEMS:u16 | RET, N:u16, N records | Returns up to 5 compact log records per request. |
| 0x15 | LOG_CLEAR | - | RET | Erases the log sector and resets log count to 0. |
| 0x22 | CAL_GET | W_IDX:u8 | RET, CAL_VER, CAL_FLAGS, N, CAL_REC | W_IDX 0..5 LEDs, W_IDX 6 PPFD. |
| 0x23 | CAL_SET | CAL_REC (11 bytes) | RET | NVM commit. Current local returns: 0 OK, 1 bad len/not found, 2 flash/bounds error. |
| 0x40 | IMAGE_BEGIN | Preferred compact: TYPE:u8, SIZE:u32, VER[3], CRC32:u32. Legacy accepted: TYPE:u8, COMPRESS:u8, SIZE:u32, VER[3], CRC32:u32 | RET, WINDOW:u16, SLOT:u8 | Starts staged production image upload. |
| 0x41 | IMAGE_DATA | OFFSET:u16, BYTES:u8, DATA[BYTES] | RET | Chunk data. BYTES <= available ICD request payload and <=255. With ATT_MTU 23, use <=12 data bytes per IMAGE_DATA frame. With negotiated ATT_MTU 67, current firmware supports up to 53 data bytes per IMAGE_DATA frame. |
| 0x42 | IMAGE_END | - | RET, VERIFY:u8 | VERIFY: 0 OK, 1 size mismatch, 2 CRC mismatch, 3 other. REBOOT required to run new image. |
| 0x51 | LED_CUR_SET | W_IDX:u8, I_LED_UA:u16 | RET | Only W_IDX 0..5. W_IDX 6 is PPFD and is rejected. |
| 0x52 | LED_CUR_GET | W_IDX:u8 | RET, W_IDX:u8, I_LED_UA:u16 | Reads stored current for physical LED index. |

## Table 6
| GET_STATUS field | Type | Units | Description |
| UPTIME_MS | u32 | ms | Time since application boot. |
| BATT_MV | u16 | mV | Battery voltage. |
| PERIPH_PWR | u8 | bool | Peripheral power state. |
| SENSOR_FLAGS | u16 | bitmap | Current sensor presence/status bitmap. |
| FAULT_FLAGS | u16 | bitmap | Current fault bitmap. |
| RSSI_DBM | i8 | dBm | Latest connection RSSI. |
| LAST_RESET | u8 | enum | Reset reason from platform status. |
| HANDHELD_TIME_S | u32 | s | Unix time if SET_TIME has been called; otherwise uptime-derived seconds. |

## Table 7
| START_MEAS request field | Type | Rule |
| MODE | u8 | Only 0=ONESHOT implemented. Other values return BAD_PARAM. |
| COUNT | u16 | Set to 1 for current ONESHOT flow. Parsed for payload shape compatibility. |
| INTERVAL_MS | u16 | Must be >=200. Used for host pacing compatibility. |
| MEAS_AVG | u8 | Allowed: 0, 1, 2, 4, 8, 16. 0 is treated as 1. Averaging applies only to ADC-derived fields. |
| FLAGS | u8 | Reserved; set 0. |

## Table 8
| Measurement response field | Type | Units | Description |
| RET | u8 | - | 0 OK, or error. |
| MEAS_ID | u16 | - | Monotonic measurement ID. |
| HANDHELD_TIME_S | u32 | s | Current handheld time. Firmware member name is ts_ms, but value is seconds. |
| SENSORS | u16 | bitmap | Sensor snapshot. |
| AMB_TEMP_CC | i16 | 0.01 C | Ambient temperature from HDC2010. |
| RH_CPERCENT | u16 | 0.01 %RH | Relative humidity from HDC2010. |
| PPFD_RAW_MV | u16 | mV | PPFD photodiode ADC millivolts. SmartDevice maps mV to PPFD using CAL W_IDX=6. |
| LEAF_TEMP_CC | i16 | 0.01 C | Leaf/object temperature from MLX90632. |
| ACCEL_X/Y/Z_MG | 3 x i16 | mg | MXC4005 axes. |
| ADC_V_MV[12] | 12 x u16 | mV | Physical LED reflectance channels use indices 0..5; remaining entries are reserved/zero. |
| BATT_MV | u16 | mV | Battery voltage. |
| ERRORS | u16 | bitmap | b0 indicates target hardware measurement backend failure. |

## Table 9
| START_MEAS state rule: SmartDevice must send SET_PERIPH_POWER=1 before START_MEAS. If peripheral power is off, START_MEAS returns NOT_READY and records a MEAS_REJECT_POWER diagnostic log entry. |

## Table 10
| W_IDX | Physical channel | Measurement response | Calibration use |
| 0 | 531 nm LED | ADC_V_MV[0] | Reflectance CAL_REC. |
| 1 | 570 nm LED | ADC_V_MV[1] | Reflectance CAL_REC. |
| 2 | 705 nm LED | ADC_V_MV[2] | Reflectance CAL_REC. |
| 3 | 750 nm LED | ADC_V_MV[3] | Reflectance CAL_REC. |
| 4 | 830 nm LED | ADC_V_MV[4] | Reflectance CAL_REC. |
| 5 | 970 nm LED | ADC_V_MV[5] | Reflectance CAL_REC. |
| 6 | PPFD photodiode pseudo-index | PPFD_RAW_MV field, not ADC_V_MV[6] | PPFD two-point mV-to-PPFD calibration. LED_CUR_SET rejects this index. |

## Table 11
| CAL_REC field | Type | LED W_IDX 0..5 | PPFD W_IDX 6 |
| W_IDX | u8 | 0..5 | 6 |
| R1 | u16 | Reflectivity point 1 in Q1.15 | PPFD point 1, PPFD x10 |
| V1_MV | u16 | Measured photodiode mV at R1 | Measured PPFD photodiode mV at point 1 |
| R2 | u16 | Reflectivity point 2 in Q1.15 | PPFD point 2, PPFD x10 |
| V2_MV | u16 | Measured photodiode mV at R2 | Measured PPFD photodiode mV at point 2 |
| COV_MV | u16 | Cover/window diagnostic mV | Reserved; set 0 |

## Table 12
| Code | Name | ARG meaning |
| 0x13 | MEAS_HW_FAIL | stage<<8 | detail |
| 0x14 | MEAS_REJECT_PARAM | mode<<8 | avg |
| 0x15 | MEAS_REJECT_POWER | avg |
| 0x23 | IMAGE_BEGIN_FAIL | return/status |
| 0x25 | IMAGE_DATA_FAIL | return/status |
| 0x27 | IMG_FLASH_ID_BAD | flash device id |
| 0x28 | IMG_BEGIN_BAD | bad length/size/end low word |
| 0x29 | IMG_BOOT_HDR_WRITE_FAIL | written bytes |
| 0x2A | IMG_DATA_WRITE_MISMATCH | actual bytes |
| 0x2B | IMG_END_SIZE_MISMATCH | expected size low word |
| 0x2D | IMG_LAYOUT_SANITY_FAIL | reason |
| 0x2E | IMG_FLASH_NOT_READY | stage |
| 0x31 | CAL_SAVE_ERR | W_IDX |
| 0x33 | LED_CUR_SAVE_ERR | W_IDX |
| 0x34..0x38 | CAL backend errors | backend-specific |
| 0x39 | DEVICE_INFO_SET | HW_REV |
| 0x41 | LOG_CLEAR_OK | reserved |
| 0x42 | LOG_CLEAR_ERR | erase status |
| 0x50 | ICD_TX_OVERSIZE | OPC |
| 0x51 | ICD_LEN_MISMATCH | received length |
| 0x52 | ICD_UNKNOWN_OPCODE | OPC |
| 0x53 | PERIPH_POWER | 0 off / 1 on |
| 0x54 | REBOOT_CMD | 0 |
| 0x55 | SLEEP_CMD | 0 |
| 0x60 | BCB_FLASH_NOT_READY | 0 |
| 0x61 | BCB_CRC_BAD | 0 |
| 0x62 | BCB_WRITE_SHORT | written bytes |

## Table 13
| Flash region | Offset | Size | Purpose |
| Boot manager | 0x00000 | 0x03000 | Stage-1 boot manager, DA14531 bootable format. |
| Slot A | 0x03000 | 0x0B000 | Production application slot. IMAGE_* writes here. |
| Slot B | 0x0E000 | 0x0C000 | Recovery application slot. |
| Logs | 0x1A000 | 0x04000 | Reserved log region; current logger uses first 4 KB. |
| BCB | 0x1E000 | 0x01000 | Boot-control block. |
| CAL/identity | 0x1F000 | 0x01000 | Calibration, LED currents, hardware revision, serial. |

## Table 14
| Failed update expectation: if production cannot run, the boot manager should fall back to the recovery application. The SmartDevice should scan for P531-Recovery, connect, use GET_INFO to confirm RECOVERY_MODE=1, then repeat IMAGE_BEGIN/DATA/END and REBOOT. Recovery GET_INFO returns the normal first 13 bytes plus MODE:u8, FLAGS:u16, UPTIME_MS:u32, RSSI:i8 fields. |

## Table 15
| OPC | Name | Recovery support |
| 0x01 | PING | Supported. |
| 0x02 | GET_INFO | Supported; 24-byte response includes recovery mode and flags. |
| 0x08 | REBOOT | Supported; commits pending verified image then resets. |
| 0x40 | IMAGE_BEGIN | Supported. |
| 0x41 | IMAGE_DATA | Supported. |
| 0x42 | IMAGE_END | Supported. |
| Other | - | Expected to return UNKNOWN_OPCODE. |
