import serial, time

# possible timeout values:
#    1. None: wait forever, block call
#    2. 0: non-blocking mode, return immediately
#    3. x, x is bigger than 0, float allowed, timeout block call

ser = serial.Serial()
# ser.port = "/dev/ttyUSB0"
ser.port = "/dev/ttys2"
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS  # number of bits per bytes
ser.parity = serial.PARITY_NONE  # set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE  # number of stop bits
# ser.timeout = None          #block read
ser.timeout = 1  # non-block read
# ser.timeout = 2              #timeout block read
ser.xonxoff = False  # disable software flow control
ser.rtscts = False  # disable hardware (RTS/CTS) flow control
ser.dsrdtr = False  # disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2  # timeout for write

try:
    ser.open()
except Exception as e:
    print "error open serial port: " + str(e)
    exit()

if ser.isOpen():

    try:
        ser.flushInput()  # flush input buffer, discarding all its contents
        ser.flushOutput()  # flush output buffer, aborting current output
        # and discard all that is in buffer

        from math import *

        Fs = 8000
        f = 500
        sample = 512
        a = [0] * sample
        for n in range(sample):
            a[n] = sin(2 * pi * f * n / Fs)

        # write data
        ser.write(a)
        print("write data: {}".format(a))

        ser.close()
    except Exception as e:
        print "error communicating...: " + str(e)

else:
    print "cannot open serial port "
