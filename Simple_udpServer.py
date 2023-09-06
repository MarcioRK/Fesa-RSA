from socket import *
import random
from Crypto.Util import number

def generatePrime():
    return number.getPrime(4096)

def decrypt(letterDecryption,d,N):
    return pow(letterDecryption,d,N)

q = generatePrime()
p = generatePrime()
N = p*q
totienteN = p*q-p-q+1
e = generatePrime()
while e > totienteN:
    e = generatePrime()
while totienteN%e==0:
    while e > totienteN:
        e = generatePrime()
d = pow(e, -1, totienteN)

msgFromClient = str(e)+'-'+str(N)
bytesToSend = str.encode(msgFromClient)
serverName = "192.168.15.50"
serverPort = 12500
bufferSize = 250000

clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.sendto(bytesToSend, (serverName, serverPort))

letras=[]
msgFromServer=''

while 1:
    
    while msgFromServer!='Fim':
        msgFromServer = clientSocket.recvfrom(bufferSize)
        msgFromServer = str(msgFromServer[0],"utf-8")
        if(msgFromServer!='Fim'):
            letras.append(msgFromServer)

    decryptedText = ''
    for i in letras:
        iInt=int(i)
        originalNumber = decrypt(iInt,d,N)
        originalLetter = chr(originalNumber)
        decryptedText = decryptedText+str(originalLetter)

    if(msgFromServer=='Fim'):
        print('Decrypted text:'+decryptedText)
        break

