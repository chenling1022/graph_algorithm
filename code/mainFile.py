
import time

from Nearest_Hosp_MultiBFS import nearest_Hosp_MultiBFS
from top_K_MultiBFS import top_k_multiBFS 

def readGraphfile(filename):
    print("Reading edges...")
    t0 = time.process_time()
    file = open(filename, mode="r")
    inp = file.read().split('\n')
    pointerDict = {}  # used to store all edges
    for i in inp:
        if ("#" not in i) and len(i) > 2:
            pair = i.split()
            pair = [int(x) for x in pair]
            try:
                pointerDict[pair[0]].append(pair[1])
            except KeyError:
                pointerDict[pair[0]] = [pair[1]]
    file.close()
    t1 = time.process_time() - t0
    print("Input read in {:.2f} seconds".format(t1))
    print("Success!\n")
    return pointerDict

#Generates a given number of hospitals using a hash function
def genHospList(numHosp, pointerDict):
    hospList=[]
    if numHosp<len(pointerDict.keys()):
        Dist=len(pointerDict)//(numHosp)
        print("Generating Hospitals...")
        t0 = time.process_time()
        x=0
        x_next=1
        while True:
            if(x in pointerDict.keys()):
                hospList.append(x)
            if len(hospList)==numHosp:
                break;
            if(x>len(pointerDict)): #rehashing, to ensure that the node is within given range
                x=x_next
                x_next+=1
            x+=Dist
        t1 = time.process_time() - t0
        print("Input read in {:.2f} seconds".format(t1))
        print("Success!")
        return(hospList)
    else:
        return []
    
    

def readHospFile(filename):
    print("Reading Hospitals...")
    t0 = time.process_time()
    file = open(filename, mode="r")
    inp = file.read().split('\n')
    hospList=[] # used to store hospitals
    for i in inp:
        if ("#" not in i and i!=""):
            hospList.append(int(i))
       
    file.close()
    t1 = time.process_time() - t0
    print("Done in {:.2f} seconds".format(t1))
    print("Success!\n")
    return hospList

pointerDict={}
hospList=[]
exportFile=""
verbose=0
k=1
while True:
    print("**************************************")
    print("What Do you want to do?")
    print("1. Read Graph from File")
    print("2. Read Hospitals from File")
    print("3. Generate Hospitals")
    print("4. Enter Output Directory")
    print("5. Find Nearest Hospital to each Node")
    print("6. Find k Nearest Hospitals to each Node")
    print("7. Exit")
    print("**************************************")
    print("8. Developer options")
    print("**************************************")
    print("Enter your choice (Run opt1, Run one among opt 2 & 3) :")
    choice=int(input())
    if(choice==1):
        print("Enter File to Read:")
        filename=input()
        pointerDict=readGraphfile(filename)
    elif(choice==2):
        print("Enter File to Read:")
        filename=input()
        hospList=readHospFile(filename)
    elif(choice==3):
        print("Enter number of hospitals:")
        numHosp=int(input())
        if(numHosp>len(pointerDict)):
            print("Error: Number of Hospitals exceeds Graph size")
        else:
            hospList=genHospList(numHosp, pointerDict)
    elif(choice==4):
        print("Enter Output Directory(pickle file):")
        exportFile=input()
    elif(choice==5):
        if (exportFile!=""):
            nearest_Hosp_MultiBFS(pointerDict, hospList, exportFile, verbose=verbose)
        else:
            nearest_Hosp_MultiBFS(pointerDict, hospList, verbose=verbose)
    elif(choice==6):
        print("Enter k nearest Hospitals to find:")
        k=int(input())
        if (k>len(hospList)):
            print("Error: Value of k exceeds Number of hospitals")
            continue
        else:
            if (exportFile!=""): 
                top_k_multiBFS(k, pointerDict, hospList, exportFile, verbose=verbose)
            else:
                top_k_multiBFS(k, pointerDict, hospList, verbose=verbose)     
    elif(choice==7):
        print("exiting...")
        break;
    elif(choice==8):
        print("Select Verbose Level")
        print("0. Only Times taken for process")
        print("1. Times taken as well as execution details")
        print("2. Print all details, including lists and Dicts")
        verbose=int(input())
        
    
    
    
      
