import hashlib
from time import time
import json
import numpy as np
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

count = 1
chain = [[None for col in range(5)] for row in range(1)]

class Blockchain():

    def newBlock():
        global chain
        blockData = {
            'index' : len(chain) - 1,
            'timeStamp' : time(),
            'data' : input("Enter data you want to add to block : "),
            'hash' : "",
            'nonce' : "",
        }
        blockData['hash'] = hashlib.sha512(str(blockData['data']).encode("utf-8")).hexdigest() 
        return blockData

    def saveChain(updateList):
        global count, chain
        chain[count-1][0] = updateList['index']
        chain[count-1][1] = updateList['timeStamp']
        chain[count-1][2] = updateList['data']
        chain[count-1][3] = updateList['hash']
        chain[count-1][4] = updateList['nonce']
        count = count +1

        nextChain = []       
        for row in range(count):
            line = []
            for col in range(5):
                if row != count-1:
                    line.append(chain[row][col])
                else:
                    line.append(None)
            nextChain.append(line)

        chain = nextChain
        
    def catchData():
        if count == 1:
            print("Data Block is empty")
            Blockchain.Play()

        print("The current index ranges from 0 to {}.".format(count-2))
        needData = input("Enter index value for the data you want. : ")
        needData = int(needData)

        check = False
        while check != True:
            if needData < 0 & count-1 <needData:
                needData = input("index out of range. Please enter a valid index of data : ")
            else:
                check = True
        
        level = np.random.randint(1,10)
        print("The mining level is %d." %level)
        passward = ""
        passward = passward.zfill(level)
        hashcode = ""
        i = 0
        b = 0
        c = 0
        while passward != hashcode:  
            hashcode = hashlib.sha256(str(c).encode("utf-8")).hexdigest()
            hashcode = hashcode[0:level]
            i = np.random.rand()
            b = np.random.rand()
            c = i*b 
            print(hashcode, c)

        print("The data value is %s." %chain[int(needData)][2])

    def Play():
        print("1. 데이터 입력 | 2. 데이터 선택 | 3. 종료")
        command =  input()
        if command == '1':
            Blockchain.saveChain(Blockchain.newBlock())
            Blockchain.Play()
        elif command == '2':
            Blockchain.catchData()
            Blockchain.Play()
        elif command == '3':
            exit()
        else:
            print("Please enter a valid input")
            Blockchain.Play()

Blockchain.Play()