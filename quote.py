import time
import os
file=open("quotes.txt","r")
lines = file.read().split("\n")



def GetSub(line):
    dic = {}
    if(len(line.split("\\"))==5):
        quote = line.split("\\")[0]
        reason = line.split("\\")[1]
        subquote = line.split("\\")[2]
        short = line.split("\\")[3]
        significance = line.split("\\")[4]
        dic["quote"]=quote
        dic["analysis"]=reason
        dic["subquote"]=subquote
        dic["short"]=short
        dic["significance"]=significance
    return dic

import json
 
# Data to be written
dictionary = {}
dictionary2={}
for i in range(len(lines)):
    if(GetSub(lines[i])!={}):
        dictionary2[f"Quote {i+1}"]=GetSub(lines[i])
dictionary["Quotes"]=dictionary2
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("quotes.json", "w") as outfile:
    outfile.write(json_object)

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
    it=0
    if(t=="end"):
        end=False
        print("EXIT")
    for i in range(len(lines)):
        ind = GetIndex(lines[i])
        if(ind ==t):
            print(f"INDEX: {i+1}")
            ReadIndex(lines[i])
            print("")
            it+=1
    for i in range(len(lines)):
        ind = GetShort(lines[i]).split(" + ")
        for i2 in range(len(ind)):

            if(ind[i2] ==t):
                print(f"INDEX: {i+1}")
                ReadIndex(lines[i])
                print("")
                it+=1
    
    try:
        for i in range(len(lines)):
            if(i+1==int(t)):
                print(f"INDEX: {i+1}")
                ReadIndex(lines[i])
                print("")
                it+=1
    except ValueError:
        pass
    if(t=="*"):
        for i in range(len(lines)):
            ReadIndex(lines[i])
            print("")
            it+=1
    if(t=="r"):
        file=open("quotes.txt","r")
        lines = file.read().split("\n")
        os.system('cls')

    print(f"\nFound {it} Quotes from target command '{t}'")
time.sleep(5)
