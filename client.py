###########################################
# Author: Aravind Potluri
# Description:  Basic python UDP Client that
#               sends user I/P to server
#               and recevies the response.           
########################################### 

# Macros
serverIP = "127.0.0.1"
serverPORT = 8080

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

# Send the data
while True:
    try:
        # Sending the user input to server
        sock.sendto(input("\n[#] Enter the msg: ").encode('UTF-8'), (serverIP, serverPORT))

        # Receive the response from server
        data, serverAddress = sock.recvfrom(1024) # Assuming MAX data to be received is 1024 Bytes.
        print(f"[#] Response from server: {data.decode('UTF-8')}")

    except KeyboardInterrupt:
        print(" [!] Client shutting down.")
        break

    except Exception as err:
        print(f"An error occurred: {str(err)}")
        break

# Close the server socket
sock.close()
