import os
import threading 
import time
import json
from threading import*

dt={}
def create(key,value,timeout=0):
    if key in dt:
        print("ERROE : Key aready exists....") 
    else:
            if len(dt)<(1024*1024*1024) and value<=(16*1024*1024): #condition for file size less than 1GB and Jason object value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #condition for input key_name capped at 32chars
                    dt[key]=l
            else:
                print("ERROE : Size limit exceeded....")


def read(key):
    if key not in dt:
        print("ERROE : Data not found....") 
    else:
        b=dt[key]
        if b[1]!=0:
            if time.time()<b[1]: #Time comparison
                string=str(key)+":"+str(b[0]) #JasonObject format (key:value)
                return string
            else:
                print("ERROR: TTL of",key,"has expired....")
        else:
            stri=str(key)+":"+str(b[0])
            return string
        

def delete(key):
    if key not in dt:
        print("ERROE : Data not found....") 
    else:
        b=dt[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del dt[key]
                print("Key Deleted....")
            else:
                print("ERROR: TTL of",key,"has expired....") 
        else:
            del dt[key]
            print("Key Deleted....")


opt=1
while(opt<=4 and opt>0):

        print('\nHello there! please choose the operation you want to perform')

        print('1. CREATE KEY')

        print('2. READ KEY')

        print('3. DELETE KEY')

        print('4. DISPLAY DATA')

        opt=int(input("ENTER YOUR OPTION : "))

        if(opt==1):

                key=input("\nEnter Key : ")
                value=int(input("Enter Value : "))
                timeout=int(input("Enter Time : "))
                create(key,value,timeout)

        elif(opt==2):

                key=input("\nEnter the Key to read : ")
                print(read(str(key)))

        elif(opt==3):

                key=input("\nEnter Key to be deleted : ")
                delete(key)

        elif(opt==4):
            
                print("\n")
                print(dt,timeout)

        else:

                break
