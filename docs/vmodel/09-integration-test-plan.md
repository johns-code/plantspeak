# Integration Test Plan

Project: PlantSpeak

Generated: 2026-06-16T06:09:07+00:00

| Test ID | Requirement | Status | Objective |
| --- | --- | --- | --- |
| IT-001 | SW-001 | Planned | Verify: The software shall implement: build ICD capabilities on DA14531 according to schematics PlanSpeak Schematic V3.pdf |
| IT-002 | SW-002 | Planned | Verify: The software shall implement: the red/green user LEDs mentioned in the ICD are controlled via P0_5 and P0_11 |
| IT-003 | SW-003 | Planned | Verify: The software shall implement: the user push button is on P0_10 |
| IT-004 | SW-004 | Planned | Verify: The software shall implement: eN_Peripherals is on P0_6 |
| IT-005 | SW-005 | Planned | Verify: The software shall implement: i2C SCL is on P0_8 and SDA on P0_9 |
| IT-006 | SW-006 | Planned | Verify: The software shall implement: the photodiode current is read by the ADS1115IDGSR. AIN0 is for reading the PD current for all the external LEDs (that is, in a measurement each wavelength an LED is turns on and the signal is read on AIN0 in all LED cases) AIN1 is signal for PPFD signal |
| IT-007 | SW-007 | Planned | Verify: The software shall implement: the wavelength LEDs are driven by LP5816 hanging off the PCA9846PWJ. LED1/2/3/4 are on the LP5816 on channel SC1/SD1 the PCA9846PWJ with LEDs 5/6 are on the LP5816 on channel SC2/SD2 on the PCA9846PWJ |
| IT-008 | SW-008 | Planned | Verify: The software shall implement: leaf temperature is on MLX90632SLD-BCB-000-RE connected to SC0/SD0 on the PCA9846PWJ |
| IT-009 | SW-009 | Planned | Verify: The software shall implement: rH and ambient temp are read from HDC2010YPAR using DA14531 I2C bus |
| IT-010 | SW-010 | Planned | Verify: The software shall implement: accelerometer is from MXC4005XC using DA14531 I2C bus |
| IT-011 | SW-011 | Planned | Verify: The software shall implement: red/green user LEDs not available - can use dev board LED for initial dev work and testing |
| IT-012 | SW-012 | Planned | Verify: The software shall implement: eN_Peripherals no avaiable |
| IT-013 | SW-013 | Planned | Verify: The software shall implement: all external I2C devices not available (so use canned data for testing but again still develop hanrdware interfaces to do real work when target board comes) |
| IT-014 | SW-014 | Planned | Verify: The software shall implement: user push button not available |
