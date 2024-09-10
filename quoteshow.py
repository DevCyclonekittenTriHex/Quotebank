import customtkinter as ctk
root = ctk.CTk()
root.geometry("480x375")

scrollable_frame = ctk.CTkScrollableFrame(master=root, width=480, height=325)
scrollable_frame.place(x=0,y=50)
class Button():
    def __init__(self,frame,index):
        fm = ctk.CTkFrame(master=frame,width=440,height=200,fg_color="red")
        fm.grid(row=index,column=0)
        btn1 = ctk.CTkButton(master=fm,width=400,height=50)
        btn1.pack()
Button(scrollable_frame,0)
Button(scrollable_frame,1)
Button(scrollable_frame,2)
Button(scrollable_frame,3)
Button(scrollable_frame,4)
Button(scrollable_frame,5)
Button(scrollable_frame,6)
Button(scrollable_frame,7)
Button(scrollable_frame,8)
root.mainloop()