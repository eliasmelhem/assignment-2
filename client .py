import socket, sys

cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cSocket.settimeout(10)
try:
    cSocket.connect(('127.0.0.1',4444))
except socket.error as error:
    print('EXCEPTION: ', error)
    sys.exit(1)

while True:

    try:
        for i in range(20):
            data0 = cSocket.recv(1024).decode()
            print(data0)
            data00 = cSocket.recv(1024).decode()
            print(data00)
            answer=input("the answer is: ")
            cSocket.send(answer.encode())
            if i ==20 :
                break


        data = cSocket.recv(1024).decode()
        print("The Mark for your exam is :"+data)
        break
    except socket.error as error:
        print("EXCEPTION 2: ", error)
print('END..')
cSocket.close()

