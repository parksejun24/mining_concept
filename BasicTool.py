import hashlib
from time import time
import json
import numpy as np

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
        global chain

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
        hashcode = ""
        passward = passward.zfill(level)
        
        dataHash = chain[needData][2]
        while passward != hashcode:  
            hashcode = hashlib.sha256(str(dataHash).encode("utf-8")).hexdigest()
            hashcode = hashcode[0:level]
            dataHash = dataHash + '0'
            print(hashcode)
        print("The data value is %s." %chain[int(needData)][2])



    def Play():
        print("1. ????????? ?????? | 2. ????????? ?????? | 3. ??????")

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
