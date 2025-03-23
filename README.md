# Bluetooth Communication (Server and Client)

This project demonstrates a simple Bluetooth communication system using Python's socket module. The communication is set up between a Bluetooth server and a Bluetooth client using the RFCOMM protocol.

Files Included:
1. server.py - This file contains the Bluetooth server code.
2. client.py - This file contains the Bluetooth client code.

## Setup and Usage

### Requirements:
- Python 3.x
- pybluez library (required for Bluetooth communication on Linux)
- Bluetooth adapter on your machine

To install pybluez, use the following command:

    pip install pybluez

### Server Code (server.py):
This script creates a Bluetooth server that listens on RFCOMM port 4. It waits for a client to connect and then exchanges messages.

Steps to run the server:
1. Run the server.py script:

        python server.py

2. The server will start and wait for a connection from a client.
3. After a successful connection, you can send and receive messages between the server and the client.

### Client Code (client.py):
This script connects to the Bluetooth server and allows the user to send and receive messages interactively.

Steps to run the client:
1. Run the client.py script:

        python client.py

2. The client will attempt to connect to the Bluetooth server on port 4.
3. Once connected, you can send messages to the server and receive responses.

### Bluetooth Address:
In the server code, the Bluetooth address of the server is currently set to "", which means it will listen on any available Bluetooth device on port 4. To specify a particular device, replace the empty string with the server's Bluetooth address (e.g., client.connect(("00:11:22:33:44:55", 4))).

### Error Handling:
The scripts handle basic socket errors (e.g., connection issues, disconnections) by catching OSError exceptions. These can be expanded based on your specific use case.

### Closing Connections:
Both the server and client scripts ensure that Bluetooth connections are properly closed after the communication ends.

### Notes:
- The server and client should be run on devices that support Bluetooth and have Python installed.
- Ensure that the Bluetooth adapters are properly paired and connected before running the scripts.
