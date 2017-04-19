import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

settemp = input('Set desired temperature: ' )

mode = input('Select 1 for AC, 0 for Heat: ')

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        #return temp_c, temp_f
	return temp_f	

while True:
	if mode == 1:
		print('Desired Temperature ', settemp)
		print('Current Temperature ', read_temp())	
		if settemp < read_temp():
			print('Turning on AC to bring down the temp')
			time.sleep(10)
		else:
			print('The temperature is just fine')
			time.sleep(10)
	elif mode == 0:
		print('Desired Temperature ', settemp)
                print('Current Temperature ', read_temp())
		if settemp > read_temp():
			print('Turning on the heat to raise the temp')
			time.sleep(10)
		else:
			print('The temperature is just fine')
			time.sleep(10)
        else:
                print('I assume you wanted to turn on the heat')
		print('Desired Temperature ', settemp)
                print('Current Temperature ', read_temp())
                if settemp > read_temp():
                        print('Turning on the heat to raise the temp')
                        time.sleep(10)
		else:
			print('The temperature is lower than the desired temp')
			time.sleep(10)
