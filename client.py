############################################################
# Author:       Aravind Potluri <aravindswami135@gmail.com>
# Description:  Basic python UDP Client that sends user I/P
#               to server and recevies the response.           
############################################################ 

# Macros
serverIP = "127.0.0.1"  # Target node's IP Address.
serverPORT = 8080       # Target node's Port.

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

# Sending the data
while True:
    try:
        # Sending the user input to server
        sock.sendto(input("\n[#] Enter the msg: ").encode('UTF-8'), (serverIP, serverPORT))

        # Receive the response from server
        try:
            sock.settimeout(5) # Time out, if the connection cant be established.
            data, serverAddress = sock.recvfrom(1024) # Assuming MAX data to be received is 1024 Bytes.
            print(f"[#] Response from server: {data.decode('UTF-8')}")
        except TimeoutError:
            print("[-] No Response from server, check the connections !")

    except KeyboardInterrupt:
        print("\n[!] Client shutting down.")
        break

    except Exception as err:
        print(f"[!] ERROR: {str(err)}")
        break

# Close the server socket
sock.close()
