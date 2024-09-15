import time
import os
file=open("quotes.txt","r")
lines = file.read().split("\n")


def ReadIndex(line):
    if(len(line.split("\\"))==5):
        quote = line.split("\\")[0]
        reason = line.split("\\")[1]
        subquote = line.split("\\")[2]
        short = line.split("\\")[3]
        significance = line.split("\\")[4]
        print(f"Quote: {quote}")
        print(f"Short: {short}")
        print(f"Reason: {reason}")
        print(f"Subquote: {subquote}")
        print(f"Significance: {significance}")
def GetIndex(line):
    if(len(line.split("\\"))==5):
        quote = line.split("\\")[0]
        reason = line.split("\\")[1]
        subquote = line.split("\\")[2]
        short = line.split("\\")[3]
        significance = line.split("\\")[4]
        return short
    return "null"
def GetShort(line):
    if(len(line.split("\\"))==5):
        quote = line.split("\\")[0]
        reason = line.split("\\")[1]
        subquote = line.split("\\")[2]
        short = line.split("\\")[3]
        significance = line.split("\\")[4]
        return subquote
    return "null"
end = True
while end:
    t = input(">>> ")
    print("\n********************")
    if(t=="end"):
        end=False
        print("EXIT")
    for i in range(len(lines)):
        ind = GetIndex(lines[i])
        if(ind ==t):
            print(f"INDEX: {i}")
            ReadIndex(lines[i])
            print("")   
    for i in range(len(lines)):
        ind = GetShort(lines[i]).split(" + ")
        for i2 in range(len(ind)):

            if(ind[i2] ==t):
                print(f"INDEX: {i}")
                ReadIndex(lines[i])
                print("")
                
    if(t=="*"):
        for i in range(len(lines)):
            ReadIndex(lines[i])
            print("")
    if(t=="r"):
        file=open("quotes.txt","r")
        lines = file.read().split("\n")
        os.system('cls')

    
time.sleep(5)
