import socket
import csv
remote_server = "google.com"
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as soc: 
    soc.connect((remote_server, 80))
    host = soc.getsockname()[0]
def main():
    reader = csv.reader(open('data.csv', 'r'))
    dictionary = {}
    for row in reader:
        dictionary[row[0]] = [row[1],row[2]]
    port = 4900
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    c, addr = s.accept()
    mark = ['ATTENDANCE-SUCCESS','ROLLNUMBER-NOTFOUND']
    while True:
        data = c.recv(1024)
        if not data:
            break
        data = data.decode()
        datalist = data.split(' ')
        if datalist[0] == 'MARK-ATTENDANCE':
            for keys in dictionary:
                if(keys == datalist[1]):
                    c.send(dictionary[keys][0].encode())
                    data = c.recv(1024)
                    if not data:
                        break
                    data = data.decode()
                    if (str(data) == datalist[1]):
                        c.send(mark[0].encode())
                    else:
                        c.send(mark[1].encode()) 
                else:
                    c.send(mark[1].encode())
        c.close()
if __name__ == '__main__':
    main()