import unittest
import os

# Get the directory where the test files are located
test_dir = os.path.dirname(os.path.abspath(__file__))

# Use the discover function to find all test files in the directory
test_suite = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')

# Run the test suite
unittest.TextTestRunner().run(test_suite)
