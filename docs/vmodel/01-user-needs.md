# User Needs Document

Project: PlantSpeak

Generated: 2026-06-16T08:25:12+00:00

| ID | Need | Rationale |
| --- | --- | --- |
| UN-001 | build ICD capabilities on DA14531 according to schematics PlanSpeak Schematic V3.pdf | Captured from the submitted high-level requirements brief. |
| UN-002 | the red/green user LEDs mentioned in the ICD are controlled via P0_5 and P0_11 | Captured from the submitted high-level requirements brief. |
| UN-003 | the user push button is on P0_10 | Captured from the submitted high-level requirements brief. |
| UN-004 | eN_Peripherals is on P0_6 | Captured from the submitted high-level requirements brief. |
| UN-005 | i2C SCL is on P0_8 and SDA on P0_9 | Captured from the submitted high-level requirements brief. |
| UN-006 | the photodiode current is read by the ADS1115IDGSR. AIN0 is for reading the PD current for all the external LEDs (that is, in a measurement each wavelength an LED is turns on and the signal is read on AIN0 in all LED cases) AIN1 is signal for PPFD signal | Captured from the submitted high-level requirements brief. |
| UN-007 | the wavelength LEDs are driven by LP5816 hanging off the PCA9846PWJ. LED1/2/3/4 are on the LP5816 on channel SC1/SD1 the PCA9846PWJ with LEDs 5/6 are on the LP5816 on channel SC2/SD2 on the PCA9846PWJ | Captured from the submitted high-level requirements brief. |
| UN-008 | leaf temperature is on MLX90632SLD-BCB-000-RE connected to SC0/SD0 on the PCA9846PWJ | Captured from the submitted high-level requirements brief. |
| UN-009 | rH and ambient temp are read from HDC2010YPAR using DA14531 I2C bus | Captured from the submitted high-level requirements brief. |
| UN-010 | accelerometer is from MXC4005XC using DA14531 I2C bus | Captured from the submitted high-level requirements brief. |
| UN-011 | red/green user LEDs not available - can use dev board LED for initial dev work and testing | Captured from the submitted high-level requirements brief. |
| UN-012 | eN_Peripherals no avaiable | Captured from the submitted high-level requirements brief. |
| UN-013 | all external I2C devices not available (so use canned data for testing but again still develop hanrdware interfaces to do real work when target board comes) | Captured from the submitted high-level requirements brief. |
| UN-014 | user push button not available | Captured from the submitted high-level requirements brief. |
