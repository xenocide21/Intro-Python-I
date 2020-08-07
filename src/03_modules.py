"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import os
import platform
import socket

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

print("----------------------------sys.argv-------------------------------")
print(sys.argv)
print("-------------------------------------------------------------------\n\n")

# Print out the OS platform you're using:
# YOUR CODE HERE
print("--------------OS platform-----------------")
print("Current operating system info:")
print(f"Operating system name: {os.name}")
print(f"Platform: {platform.system()}")
print(f"Release: {platform.release()}")
print("------------------------------------------\n\n")

# Print out the version of Python you're using:
# YOUR CODE HERE
print("-------------------------------version of Python--------------------------------")
print(sys.version)
print(f"Python version number: {platform.python_version()}")
print("--------------------------------------------------------------------------------\n\n")


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("---------current process ID--------")
process_ID = os.getpid()
print(f"Current process ID: {process_ID}")
print("-----------------------------------\n\n")

# Print the current working directory (cwd):
# YOUR CODE HERE
print("--------------current working directory--------------")
to_get_full_path = os.path.dirname(os.path.realpath(__file__))
print(to_get_full_path)
print('----------------this works too-----------------------')
cwd = os.getcwd()
print(cwd)
print("-----------------------------------------------------\n\n")

# Print out your machine's login name
# YOUR CODE HERE

print("-------machine's login name------")
hostname = socket.gethostname()
print(hostname)
print("---------------------------------\n\n")
