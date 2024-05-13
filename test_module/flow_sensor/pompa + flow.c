#include "sensirion_common.h"
#include "sensirion_i2c_hal.h"
#include "sf06_lf_i2c.h"
#include <stdio.h> 
#include <wiringPi.h>

#define pin_pwm 13
#define en_a 19
#define en_b 26

#define sensirion_hal_sleep_us sensirion_i2c_hal_sleep_usec

void print_byte_array(uint8_t* array, uint16_t len) {
    uint16_t i = 0;
    printf("0x");
    for (; i < len; i++) {
        printf("%02x", array[i]);
    }
}

void controlMotor(int pwm_value, int delay_time) {
    // Forward motion
    digitalWrite(MOTOR_PIN_1, HIGH);
    digitalWrite(MOTOR_PIN_2, LOW);
    pwmWrite(PWM_PIN, pwm_value);
    delay(delay_time);
    
    // Stop
    digitalWrite(MOTOR_PIN_1, LOW);
    digitalWrite(MOTOR_PIN_2, LOW);
    pwmWrite(PWM_PIN, 0); // Stop PWM
    delay(delay_time);
}

int main(void) {
    int16_t error = NO_ERROR;
    sensirion_i2c_hal_init();
    sf06_lf_init(SLF3C_1300F_I2C_ADDR_08);

    sf06_lf_stop_continuous_measurement();
    sensirion_hal_sleep_us(100000);
    uint32_t product_identifier = 0;
    uint8_t serial_number[8] = {0};
    error =
        sf06_lf_read_product_identifier(&product_identifier, serial_number, 8);
    if (error != NO_ERROR) {
        printf("error executing read_product_identifier(): %i\n", error);
        return error;
    }
    printf("product_identifier: %u ", product_identifier);
    printf("serial_number: ");
    print_byte_array(serial_number, 8);
    printf("\n");
    error = sf06_lf_start_h2o_continuous_measurement();
    if (error != NO_ERROR) {
        printf("error executing start_h2o_continuous_measurement(): %i\n",
               error);
        return error;
    }

    float a_flow = 0.0;
    float a_temperature = 0.0;
    uint16_t a_signaling_flags = 0u;
    uint16_t repetition = 0;

    float a_flow_20 = 0.0;

    int flag_tampil_flow = 0;

    wiringPiSetup();
    pinMode(PWM_PIN, PWM_OUTPUT);
    pinMode(MOTOR_PIN_1, OUTPUT);
    pinMode(MOTOR_PIN_2, OUTPUT);

    // Set PWM frequency
    pwmSetMode(PWM_MODE_MS); // Mark-space mode
    pwmSetClock(400); // Set PWM frequency to 20kHz

    // Input desired PWM value
    int pwm_value;
    printf("Enter PWM value (0-1023): ");
    scanf("%d", &pwm_value);

    if (pwm_value < 0 || pwm_value > PWM_RANGE) {
        printf("Invalid PWM value. Exiting...\n");
        return 1;
    }

    // Run motor for 60 seconds
    int duration = 60000; // 60 seconds in milliseconds
    int iterations = duration / (2 * pwm_value); // Number of iterations to cover 60 seconds
    
    // Control motor for specified duration
    for (int i = 0; i < iterations; i++) {
        controlMotor(pwm_value, 1000); // Run motor for 1 second
        flag_tampil_flow++;
        sensirion_hal_sleep_us(20000);
        error = sf06_lf_read_measurement_data(
            INV_FLOW_SCALE_FACTORS_SLF3C_1300F, &a_flow, &a_temperature,
            &a_signaling_flags);
        if (error != NO_ERROR) {
            printf("error executing read_measurement_data(): %i\n", error);
            continue;
        }

        a_flow_20 += a_flow

        if (flag_tampil_flow >= 20){
            printf("%.2f ", a_flow_20/20);
            flag_tampil_flow = 0;
            a_flow_20 = 0;
        }
    }

    // int16_t error = NO_ERROR;
    // sensirion_i2c_hal_init();
    // sf06_lf_init(SLF3C_1300F_I2C_ADDR_08);

    // sf06_lf_stop_continuous_measurement();
    // sensirion_hal_sleep_us(100000);
    // uint32_t product_identifier = 0;
    // uint8_t serial_number[8] = {0};
    // error =
    //     sf06_lf_read_product_identifier(&product_identifier, serial_number, 8);
    // if (error != NO_ERROR) {
    //     printf("error executing read_product_identifier(): %i\n", error);
    //     return error;
    // }
    // printf("product_identifier: %u ", product_identifier);
    // printf("serial_number: ");
    // print_byte_array(serial_number, 8);
    // printf("\n");
    // error = sf06_lf_start_h2o_continuous_measurement();
    // if (error != NO_ERROR) {
    //     printf("error executing start_h2o_continuous_measurement(): %i\n",
    //            error);
    //     return error;
    // }
    // float a_flow = 0.0;
    // float a_temperature = 0.0;
    // uint16_t a_signaling_flags = 0u;
    // uint16_t repetition = 0;

    // float a_flow_20 = 0.0;

    // int flag_tampil_flow = 0;
  
    // for (repetition = 0; repetition < 5000; repetition++) {
    //     flag_tampil_flow++;
    //     sensirion_hal_sleep_us(20000);
    //     error = sf06_lf_read_measurement_data(
    //         INV_FLOW_SCALE_FACTORS_SLF3C_1300F, &a_flow, &a_temperature,
    //         &a_signaling_flags);
    //     if (error != NO_ERROR) {
    //         printf("error executing read_measurement_data(): %i\n", error);
    //         continue;
    //     }

    //     a_flow_20 += a_flow

    //     if (flag_tampil_flow >= 20){
    //         printf("%.2f ", a_flow_20/20);
    //         flag_tampil_flow = 0;
    //         a_flow_20 = 0;
    //     }
    //     //printf("a_flow: %.2f ", a_flow);
    // }

    error = sf06_lf_stop_continuous_measurement();
    if (error != NO_ERROR) {
        return error;
    }
    return NO_ERROR;
}