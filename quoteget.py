import customtkinter as ctk
class Item():
    def __init__(self,str):
        arr= str.split("\\")
        if(len(arr)>3):
            self.quote=arr[0]
            self.id=arr[1]
            self.label=arr[2]
            self.reason=arr[3]
            self.significance=arr[4]
            self.valid=True
        else:
            self.valid=False
            self.quote=""
            self.id=""
            self.label=""
            self.reason=""
            self.significance=0
    
    def set(self,quote,reason,label,id,significance):
        self.quote=quote
        self.reason=reason
        self.label=label,
        self.id=id
        self.significance=significance

def Enter():
    quote=entryQ.get("0.0", "end").replace("\n","")
    entryQ.delete("0.0","end")
    reason=entryR.get("0.0", "end").replace("\n","")
    entryR.delete("0.0","end")
    label = entryL.get("0.0", "end").replace("\n","")
    entryL.delete("0.0","end")
    id=entryID.get().replace("\n","")
    entryID.delete(0,"end")
    sig = entryS.get().replace("\n","")
    entryS.delete(0,"end")
    f=open("quotes.txt","a+")
    str=quote+"\\"+reason+"\\"+label+"\\"+id+"\\"+sig
    str=str.replace("\n","")+"\n"
    f.write(str)
    f.close()
   
ctk.set_default_color_theme("dark-blue")
root=ctk.CTk()
root.geometry("480x375")


textH = ctk.CTkLabel(root,text="Add Quote:",width=100)
textH.place(x=190,y=5)

textQ = ctk.CTkLabel(root,text="Quote:")
textQ.place(x=20,y=25+10)
entryQ = ctk.CTkTextbox(root, width=200,height=100)
entryQ.place(x=20,y=25+40)

textR = ctk.CTkLabel(root,text="Reason:")
textR.place(x=20,y=25+10+140)
entryR = ctk.CTkTextbox(root, width=200,height=100)
entryR.place(x=20,y=25+40+140)

textL = ctk.CTkLabel(root,text="Label:")
textL.place(x=20+240,y=25+10)
entryL = ctk.CTkTextbox(root, width=200,height=100)
entryL.place(x=20+240,y=25+40)

textID = ctk.CTkLabel(root,text="ID:")
textID.place(x=20+240,y=25+10+140)
entryID = ctk.CTkEntry(root, width=200,height=30)
entryID.place(x=20+240,y=25+40+140)

textS = ctk.CTkLabel(root,text="Significance:")
textS.place(x=20+240,y=25+10+140+70)
entryS = ctk.CTkEntry(root, width=200,height=30)
entryS.place(x=20+240,y=25+40+140+70)

button = ctk.CTkButton(root,text="Enter",command=Enter,width=100,height=30)
button.place(x=190,y=25+40+140+40+70+20)


root.mainloop()