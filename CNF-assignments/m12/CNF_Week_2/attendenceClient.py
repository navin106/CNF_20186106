import socket
remote_server = "google.com"
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as soc: 
    soc.connect((remote_server, 80))
    host = soc.getsockname()[0]
def Main():
    
    # print(host)
    port = 4985
    s = socket.socket()
    s.connect((host, port))
    message = input("-->")
    while message != 'q':
        s.send(message.encode())
        data = s.recv(1024)
        print("Recieved from Server: " + str(data.decode()))
        if str(data.decode()) == 'ATTENDANCE-SUCCESS':
            break
        message = input("-->")
    s.close()
if __name__ == '__main__':
    Main()