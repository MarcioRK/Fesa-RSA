from socket import *
serverName = "192.168.15.50"
serverPort = 12500
bufferSize = 250000
publicKey=''
variableList=[]
encryptedText=''

msgFromServer=''
def encrypt(number,e,N):
    return pow(number,e,N)

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind((serverName, serverPort))

while 1:
    msg = input("Input message: ")
    bytesAddressPair = clientSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    if(publicKey==''):
        publicKey=message
    variableList=str(publicKey).split('-')
    e,N=variableList
    e=e.replace("b'","")
    N=N.replace("'","")
    eInt=int(e)
    NInt=int(N)

    for i in msg:
        number = ord(i)
        cryptography = encrypt(number,eInt,NInt)
        bytesToSend = str.encode(str(cryptography))
        clientSocket.sendto(bytesToSend, address)
        
    msgFromServer=encryptedText

    clientMsg = str(message,"utf-8")
    clientIP = "Client IP Address:{}".format(address)
    
    bytesToSend = str.encode("Fim")
    clientSocket.sendto(bytesToSend, address)
    break

clientSocket.close()