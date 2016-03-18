import time
import sys
import os
from os import walk
files=[]
alphabet = 'CDEFGHIJKLMNOPQRSTUVWXYZ' #List of drives to search
alphabet = list(alphabet) #Turning above string into iterable list
StringMatch="zeug" #This is the magic string found in the file
log=open("Encrypted-log-%s.txt" % str(time.strftime("%d-%m-%H-%M")), 'ab', 0)
 
def getdrive():
    path = sys.executable
    while os.path.split(path)[1]:
        path = os.path.split(path)[0]
    return path
 
for i in alphabet:
    try:
        drive=i + ":"
        print("Building list of files on %s" % drive)
        if drive + '\\' == getdrive():
            os.chdir('\\')
        else:
            os.chdir(drive)
        rootDir=os.getcwd()
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                files.append(dirName+'/'+fname)
                fle = dirName+'/'+fname
                print fle
                try:
                    f=open(fle, 'rb')
                    data = f.read(64) #Reads the first 64 bytes.
                    f.close()
                    if StringMatch in data:
                        print("Encrypted file found - %s" % fle)
                        log.write(str(fle) + '\r\n')
                except:
                    print("Unable to open file")
    except Exception,e: print str(e)
log.close()