#include <stdio.h>
#include "pico/multicore.h"
#include "pico/stdlib.h"

int var = 0;
int another = 0;

// Core 1 main code
void core1_code() {
	while(true) {
		another = another + 1;
		printf("Counter: %i\n", another);
		sleep_ms(200);
	}
}

void core0_code() {
	const uint LED_PIN = PICO_DEFAULT_LED_PIN;
	gpio_init(LED_PIN);
	gpio_set_dir(LED_PIN, GPIO_OUT);
	while (true) {
		gpio_put(LED_PIN, 1);
		sleep_ms(250);
		gpio_put(LED_PIN, 0);
		sleep_ms(250);
		var = var + 1;
		printf("Resistance is futile %i\n", var);
	}
}

// Core 0 main code
int main() {
    stdio_init_all();

    multicore_launch_core1(core1_code); // Start core 1
    core0_code();			// Run core 0

    return 0;
    
}
