from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import configparser

# Read configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Server info
ftp_port = int(config['CONFIG']['port'])  # Convert port to an integer
listen_address = config['CONFIG']['listen']

# Set up the FTP server
authorizer = DummyAuthorizer()

# Read user information from config.ini
user_section = config['USERS']
for username, user_info in user_section.items():
    if username != 'default':
        user_info = user_info.split(',')
        password, directory, permissions = user_info
        authorizer.add_user(username, password, directory, perm=permissions)

# Create an FTP handler and associate the authorizer
handler = FTPHandler
handler.authorizer = authorizer

# Create the FTP server
server = FTPServer((listen_address, ftp_port), handler)

print("FTP Server Started")

# Serve forever
server.serve_forever()
