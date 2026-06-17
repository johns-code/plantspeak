#ifndef PLANTSPEAK_ICD_V013_COMMAND_TABLE_H
#define PLANTSPEAK_ICD_V013_COMMAND_TABLE_H

#include <stdint.h>

#define PLANTSPEAK_ICD_V013_PROTOCOL_VERSION 0x01u
#define PLANTSPEAK_ICD_V013_HEADER_BYTES 6u
#define PLANTSPEAK_ICD_V013_CRC_BYTES 2u
#define PLANTSPEAK_ICD_V013_MAX_REQUEST_PAYLOAD 56u
#define PLANTSPEAK_ICD_V013_TX_NOTIFY_FRAGMENT_BYTES 20u
#define PLANTSPEAK_ICD_V013_NEGOTIATED_ATT_MTU_MAX 67u
#define PLANTSPEAK_ICD_V013_TEST_DEFAULT_ATT_MTU 67u
#define PLANTSPEAK_ICD_V013_ATT67_GATT_WRITE_VALUE_BYTES 64u
#define PLANTSPEAK_ICD_V013_ATT67_IMAGE_DATA_BYTES 53u

typedef struct {
    uint8_t opcode;
    const char *name;
} plantspeak_icd_v013_command_t;

static const plantspeak_icd_v013_command_t PLANTSPEAK_ICD_V013_COMMANDS[] = {
    {0x01u, "PING"},
    {0x02u, "GET_INFO"},
    {0x03u, "GET_STATUS"},
    {0x04u, "SET_TIME"},
    {0x05u, "SET_RED_LED"},
    {0x06u, "SET_GREEN_LED"},
    {0x07u, "SET_PERIPH_POWER"},
    {0x08u, "REBOOT"},
    {0x09u, "ENTER_DEEP_SLEEP"},
    {0x0Au, "DEVICE_INFO_SET"},
    {0x10u, "START_MEAS"},
    {0x14u, "LOG_GET"},
    {0x15u, "LOG_CLEAR"},
    {0x22u, "CAL_GET"},
    {0x23u, "CAL_SET"},
    {0x40u, "IMAGE_BEGIN"},
    {0x41u, "IMAGE_DATA"},
    {0x42u, "IMAGE_END"},
    {0x51u, "LED_CUR_SET"},
    {0x52u, "LED_CUR_GET"},
};

#endif
