import serial
import subprocess
import optparse

def get_arguements():
    parser = optparse.OptionParser()
    parser.add_option("-b", "--baudrate", help="To set the Baud Rate of the communication", dest="baud_rate")
    parser.add_option("-p", "--serial_port", help="To provide Serial Port for the communication", dest="serial_port")

    (options, arguements) = parser.parse_args()
    if not options.baud_rate:
        parser.error("[-] Provide the Serial Communication Baud Rate")

    if not options.serial_port:
        parser.error("[-] Provide the Serial Port for Communication")

    return options

options = get_arguements()
baud_rate = options.baud_rate
serial_port = options.serial_port

# Configure the serial port
ser = serial.Serial(port=str(serial_port), baudrate=int(baud_rate), parity=serial.PARITY_ODD, stopbits=serial.STOPBITS_TWO, bytesize=serial.SEVENBITS)  # Replace 'COM3' with the appropriate port and baud rate
print("Baud Rate: " + str(baud_rate))
print("Serial Port: " + str(serial_port))

# Read serial input
while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)


