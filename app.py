# Import libraries
from canon import MG5700
from pprint import pprint

# Printer constants
HOST = '192.168.1.223'
ADMIN_PASSWORD = 'admin'

# Create printer instance
printer = MG5700(HOST)

# Log in as an administrator
logged_in = printer.login(ADMIN_PASSWORD)

# Check the log-in was successful
assert logged_in, 'Admin log-in failed!'

# Get some parameters
lan_settings = printer.get_lan_settings()

# Then, display them
pprint(lan_settings)
