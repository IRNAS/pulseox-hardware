Here are the files and instructions for you to test your pulse oximeter. 

# FLASHING THE FIRMWARE <a id="fw_flash"></a>

For flashing the firmware onto the MCU we are using the [Nucleo64 board programmer](http://www.st.com/content/ccc/resource/technical/document/user_manual/98/2e/fa/4b/e0/82/43/b7/DM00105823.pdf/files/DM00105823.pdf/jcr:content/translations/en.DM00105823.pdf).

<img src="https://user-images.githubusercontent.com/14543226/31545279-ee7916ba-b01e-11e7-9460-3babfc17405f.PNG" alt="nucleo_board" width= "400" >

1. Use the top 4 pins of the 6-pin connector (CN4) on the STM programmer to hook up the MCU.

<img src="https://user-images.githubusercontent.com/14543226/31545231-d2702bfc-b01e-11e7-88f5-e918a634aabc.PNG" alt="programmer_pinout" width= "400" >

|STM|GliaX main PCB|
|:-----:|:-----:|
|1 - VDD|5V|
|2 - SWCLK|CK|
|3 - GND|GND|
|4 - SWDIO|IO|

2. Connect your GliaX pulse oximeter with the PC with a microUSB cable and turn the switch to ON.
3. Connect the programmer with your PC with miniUSB wire.
4. You will notice a vew flash drive recognized on your pc NODE_L073RZ

<img src="https://user-images.githubusercontent.com/14543226/31546386-6437a5de-b023-11e7-8ae6-17a0888c4b53.PNG" alt="disk" width= "200" >

5. A new explorer window will pop up with DETAILS.TXT and MBED.HTM files. Should you see FAIL.TXT file in this window, this means something went wrong. Check for hardware bugs on the PCB or faulty connections.

6. Drag and drop a .bin firmware file into this drive. The LD1 on the STM programmer should blink switching between red and green. Once thec copying is done, you've successfully flashed your firmware onto your pulse oximeter.

7. Press RESET button.

# LED TEST

1. flash the 'diagnostic.bin' to your pulse oximeter following the procedure in [FLASHING THE FIRMWARE](#fw_flash) section. 
2. The display will show which LED should be turned on. 
3. Check if all LEDs are turning on as the display suggests. If the two don't match, you have most probably soldered the wires the wrong way.

# 2 DEBUG FIRMWARE

Debug firmware allows you to output the data from your GliaX pulse oximeter to your PC via USB to RS232 levels serial UART converter.

|USB-RS232| GliaX|
|:----:|:----:|
|5V|5V|
|TXD|CK|
|RXD|IO|
|GND|GND|

1. Open a serial terminal like Termite os similar (or install it of you haven't done so in the past). This demonstration will be done for [Termite](https://www.compuphase.com/software_termite.htm). 

2. Press 'Settings'
3. Configure your window as shown here 

<img src="https://user-images.githubusercontent.com/14543226/31546850-64932e5c-b025-11e7-800d-1ce65178edc3.PNG" alt="disk" width= "200" >

4. double click the 'Log File' and set the log file location
5. Click 'OK'
6. Plug in your USB-RS232 UART converter which must be hooked up to your GliaX as shown in the table above. 
7. Connect your pulse oximeter with your PC via microUSB cable and turn it on
8. Follow the instructions on the display.


