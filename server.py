###########################################
# Author: Aravind Potluri
# Description:  Basic python UDP Server that
#               echos back captilized text.           
########################################### 

# Macros
serverIP = "0.0.0.0"    # Accept from any IP.
serverPORT = 8080       # Server Port   

# Importing Libraries
import socket

# Creating socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	
    print("[+] Socket successfully created")
except:
    print(f"[-] Socket creation failed")
    sock.close()
    exit()

# Binding socket and listening for connection
try:
    sock.bind((serverIP, serverPORT))	
    print(f"[+] socket successfully binded on port {serverPORT}")
    print("[+] wating for connection...\n")
except:
    print(f"[-] Socket binding failed")	
    sock.close()
    exit()

# Establishing the connection
while True:
    try:
        # Receive data from any client
        data, clientAddress = sock.recvfrom(1024) # Assuming MAX data to be received is 1024 Bytes.
        msg = data.decode('UTF-8')
        print(f"[#] Received message from {clientAddress}: {msg}")

        # Data processing
        msg = msg.upper()

        # Echoing back the captilized msg to client
        sock.sendto(msg.encode('UTF-8'), clientAddress)

    except KeyboardInterrupt:
        print(" [!] Server shutting down.")
        break

    except Exception as err:
        print(f"An error occurred: {str(err)}")
        break

# Close the server socket
sock.close()
