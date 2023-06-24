import socket, threading,json
sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
sSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sSocket.bind(('127.0.0.1', 4444))
sSocket.listen(5)
print("server ON....")
count=0
store={}
with open("Question.json","r") as Question:
    o_fQ = json.load(Question)
student_answer=[]
with open("Answers.json","r") as Answer:
    o_fA = json.load(Answer)
def handle (C,cd):
    while True:
        try:
            for key,value in o_fQ.items():
                C.send(key.encode())
                print(key+str(cd))
                C.send(value.encode())
                rmsg = C.recv(1024).decode()
                student_answer.append(rmsg)
                if key=='Question20':
                    break
            print (student_answer)
            count=0
            for i in range(0,20):
                if student_answer[i] == o_fA[i]:
                    count+=1
            C.send(str(count).encode())
            break
        except socket.error as e:
            print(e)
        except KeyError as e:
            C.send("The name does not exist yet".encode())
    print("Finish the connection with ", cd)

previously_clients=[]
while True:
    C, cd = sSocket.accept()
    previously_clients.append(cd)
    thr1 = threading.Thread(target=handle, args=(C, cd))
    thr1.start()
    print("wait another client...")