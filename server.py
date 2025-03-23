import socket

# Create a Bluetooth socket using RFCOMM protocol
sever = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Bind the socket to any address and port 4
sever.bind(("", 4))

# Start listening for incoming connections
sever.listen(1)

# Accept a connection from a client
client, address = sever.accept()

try:
    while True:
        # Receive data from the client
        data = client.recv(1024)
        if not data:
            break
        # Print the received message
        print(f"Message: {data.decode('utf-8')}")
        # Prompt the user to enter a response
        message = input("Enter message: ")
        # Send the response back to the client
        client.send(message.encode("utf-8"))
except OSError as e:
    # Handle any socket-related errors
    pass

# Close the client and server sockets
client.close()
sever.close()
