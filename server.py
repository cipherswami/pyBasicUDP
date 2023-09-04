############################################################
# Author:       Aravind Potluri <aravindswami135@gmail.com>
# Description:  Basic python UDP Server that echos back the
#               captilized text.        
############################################################ 

# Macros
serverIP = "0.0.0.0"    # Accept from any IP.
serverPORT = 8080       # Server Port. 

# Libraries
import socket

# Creating socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	
    print("[+] Socket successfully created")
except:
    print(f"[-] Socket creation failed")
    sock.close()
    exit()

# Binding the socket
try:
    sock.bind((serverIP, serverPORT))	
    print(f"[+] socket successfully binded on port {serverPORT}")
except:
    print(f"[-] Socket binding failed")	
    sock.close()
    exit()

# Waiting for connections
while True:
    try:
        print("\n[+] wating for connection...")
        # Receive data from any client
        data, clientAddress = sock.recvfrom(1024) # Assuming MAX data to be received is 1024 Bytes.
        msg = data.decode('UTF-8')
        print(f"[#] Received message from {clientAddress[0]} : {msg}")

        # Data processing
        msg = msg.upper()

        # Echoing back the captilized msg to client
        sock.sendto(msg.encode('UTF-8'), clientAddress)
        print(f"[#] Sent Response: {msg}")

    except KeyboardInterrupt:
        print("\n[!] Server shutting down.")
        break

    except Exception as err:
        print(f"[!] ERROR: {str(err)}")
        break

# Close the server socket
sock.close()
