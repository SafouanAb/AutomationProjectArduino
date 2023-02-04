import unittest
import serial

class TestSerialPort(unittest.TestCase):
    def setUp(self):
        # Open the serial port at 9600 baud rate
        self.ser = serial.Serial("COM5", 9600)


    def test_receive(self):
        # Read data from the serial port
        data = self.ser.readline().decode("utf-8").strip()
        # Print the data
        print(data)
    def tearDown(self):
        # Close the serial port
        self.ser.close()

if __name__ == "__main__":
    unittest.main()