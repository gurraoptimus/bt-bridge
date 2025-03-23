import socket

# Create a Bluetooth socket using RFCOMM protocol
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Connect to the Bluetooth server (replace "" with the server's address)
client.connect(("", 4))

try:
    while True:
        # Get user input and send it to the server
        message = input("Enter message: ")
        client.send(message.encode("utf-8"))
        
        # Receive and print the response from the server
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
except OSError as e:
    # Handle any socket-related errors
    pass

# Close the Bluetooth connection
client.close()