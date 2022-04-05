cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(lmatrix)

pico_sdk_init()

add_executable(lmatrix
        main.c
        )

# pull in common dependencies
target_link_libraries(lmatrix
	pico_stdlib
	pico_multicore
	hardware_adc)

# create map/bin/hex file etc.
pico_add_extra_outputs(lmatrix)

pico_enable_stdio_usb(lmatrix 1)
pico_enable_stdio_uart(lmatrix 0)
