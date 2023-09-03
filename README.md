# Simple Python FTP Server

This guide will help you set up and use your FTP server program. Follow these steps to get started.

## Requirements

Before you begin, make sure you have the following:

1. Python installed on your system.
2. The `pyftpdlib` library installed. You can install it using `pip`:

    ```
    pip install pyftpdlib
    ```

3. A configuration file named `config.ini` in the same directory as your Python script. You can use the provided `config.ini` template as a starting point.

## Configuration

Open the `config.ini` file and customize it according to your preferences. Here's what each section means:

### [CONFIG]

- `port`: The port on which the FTP server will listen for connections. Replace with your desired port number.
- `listen`: The IP address on which the FTP server will listen. Use `"0.0.0.0"` to listen on all available network interfaces.

### [USERS]

- Add user entries with the following format:

    ```
    username = password, /path/to/directory, permissions
    ```

    Replace `username` with the desired username, `password` with the user's password, `/path/to/directory` with the directory where the user will have access, and `permissions` with a string of permissions (e.g., "elradfmwMT").

    Example:

    ```
    user1 = password1, /user1_directory, elradfmwMT
    user2 = password2, /user2_directory, elr
    ```

## FTP Server Permissions Guide

In your FTP server's configuration, you can specify permissions for each user to control what actions they are allowed to perform on the server. Permissions are represented as a string of letters, with each letter corresponding to a specific action. Here's a breakdown of the available permissions:

- `e`: Change directory (CWD): Allows the user to change their current directory on the server.
- `l`: List files (LIST, NLST): Grants the user the ability to list files and directories in their current directory.
- `r`: Retrieve file from the server (RETR): Allows the user to download files from the server to their local machine.
- `a`: Append data to an existing file (APPE): Permits the user to append data to an existing file on the server.
- `d`: Delete file or directory (DELE, RMD): Grants the user the ability to delete files or directories on the server.
- `f`: Rename file or directory (RNFR, RNTO): Allows the user to rename files or directories on the server.
- `m`: Create directory (MKD): Permits the user to create new directories on the server.
- `w`: Store a file on the server (STOR): Allows the user to upload files from their local machine to the server.
- `T`: Change file attributes (SITE CHMOD): Grants the user the ability to change file attributes (permissions) on the server.
- `M`: Change file mode (SITE CHMOD): Allows the user to change the file mode on the server.

You can combine these letters to define the desired permissions for each user. Here are a few examples:

- `"elradfmwMT"`: This permission string allows a user to perform almost all actions, including changing directories, listing files, retrieving, appending, deleting, renaming, creating directories, and changing file attributes and mode.

- `"elr"`: This permission string allows basic actions, including changing directories, listing files, and retrieving files, but restricts other operations like uploading, deleting, and renaming.

- `"r"`: This permission string only allows the user to retrieve files from the server, making it read-only.

- `"w"`: This permission string only allows the user to store (upload) files to the server, making it write-only.

You can customize these permission strings for each user in the `[USERS]` section of your `config.ini` file to match your specific access control requirements.


## Running the FTP Server

1. Open a terminal window.
2. Navigate to the directory containing your Python script and `config.ini`.
3. Run the following command to start the FTP server:

    ```bash
    python3 main.py
    ```

    Replace `main.py` with the name of your Python script.

## Connecting to the FTP Server

You can use any FTP client (e.g., [FileZilla](https://filezilla-project.org/download.php)) to connect to your FTP server. Use the following connection details:

- Host: Your FTP server's IP address or hostname.
- Port: The port specified in `config.ini`.
- Username: The username you created in the `config.ini` file.
- Password: The corresponding password for the username.

## Managing Users

To add, modify, or remove users, simply edit the `[USERS]` section of the `config.ini` file and restart the FTP server.

That's it! You've successfully set up and configured your FTP server. You can now transfer files to and from your server using an FTP client.

# Creating a Systemd Service for Your FTP Server (Linux Only)

## Creating the Service File

1. Open a terminal on your Linux server.

2. Use a text editor to create a `.service` file for your FTP server:

    ```bash
    nano /etc/systemd/system/my_ftp_server.service
    ```

3. In the editor, add the following content to your `my_ftp_server.service` file. Replace `your_user` with the appropriate username and `/path/to/your_ftp_server_script.py` with the full path to your FTP server script:

    ```ini
    [Unit]
    Description=FTP Server

    [Service]
    User=your_user
    ExecStart=/usr/bin/python3 /path/to/your_ftp_server_script.py

    [Install]
    WantedBy=multi-user.target
    ```

4. Save the file and exit the text editor.

## Configuring the Service

1. Reload systemd to make it aware of the new service:

    ```bash
    systemctl daemon-reload
    ```

2. Enable the service to start at boot:

    ```bash
    systemctl enable my_ftp_server.service
    ```

3. Start the service:

    ```bash
    systemctl start my_ftp_server.service
    ```

4. You can check the status of your FTP server service:

    ```bash
    systemctl status my_ftp_server.service
    ```

## Managing the Service

You can manage your FTP server service using the following systemd commands:

- To stop the service: `systemctl stop my_ftp_server.service`
- To restart the service: `systemctl restart my_ftp_server.service`
- To disable the service from starting at boot: `systemctl disable my_ftp_server.service`

That's it! You've successfully created a systemd service for your FTP server, which will automatically start on boot and can be managed using standard systemd commands.