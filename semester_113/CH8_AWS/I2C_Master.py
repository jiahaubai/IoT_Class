import smbus
import time
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import Image

I2C_SLAVE_ADDRESS = 0x55
bus = smbus.SMBus(1)

serial = i2c(port=1, address=0x3C)
oled = ssd1306(serial)

device = ssd1306(i2c(port=1,address=0x3c),width=128,height=64,rotate=0)
#device = contrast(1)

def read_motion_status():
	status = bus.read_byte(I2C_SLAVE_ADDRESS)
	return status
	
def oled_show(message):
	with canvas(device, dither=True) as draw:
		text_size = draw.textsize(message)
		draw.text(((device.width-text_size[0])//2,(device.height-text_size[1])//2),message,fill="white")
	
while True:
	status = read_motion_status()
	if status is not None:
		if status == 0xAA:
			message = "Moving"
		elif status == 0x00:
			message = "No Motion"
		oled_show(message)
	time.sleep(0.1)	
	
			
	
