#ifndef PLANTSPEAK_ICD_COMMAND_TABLE_H
#define PLANTSPEAK_ICD_COMMAND_TABLE_H

typedef struct {
    const char *requirement_id;
    const char *command_name;
} plantspeak_icd_command_t;

static const plantspeak_icd_command_t PLANTSPEAK_ICD_COMMANDS[] = {
    {"SW-001", "describe-icd"},
    {"SW-002", "set-user-led"},
    {"SW-003", "read-user-button"},
    {"SW-004", "set-peripheral-enable"},
    {"SW-005", "scan-i2c-bus"},
    {"SW-006", "read-light-sensors"},
    {"SW-007", "drive-wavelength-leds"},
    {"SW-008", "read-leaf-temperature"},
    {"SW-009", "read-ambient-climate"},
    {"SW-010", "read-acceleration"},
    {"SW-011", "set-dev-board-led"},
    {"SW-012", "report-peripheral-enable-unavailable"},
    {"SW-013", "read-canned-sensor-data"},
    {"SW-014", "report-user-button-unavailable"},
};

#endif
