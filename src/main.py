from makeCenter import *
from math import *
from PhuongTrinh import*

def clearAC():
    username.set("")
    password.set("")
    KQ.set("")

def init():
    global root
    root = Tk()
    global username,password, KQ
    username = StringVar()
    password = StringVar()
    KQ = StringVar()
    
    root.title("deuteri")
    root.minsize(height=50,width=300)
    root.resizable(height=True,width=True)
    
    root.configure(background='#6e6aba')
    Label(root,text="Login", fg="black",font=("Times New Roman",17), justify=CENTER, bg="#6e6aba").grid(row = 0,columnspan=2)
    Label(root,text="Username:",font=("Times New Roman",10), bg="#6e6aba").grid(row = 1,column=0)
    Label(root,text="Password ",font=("Times New Roman",10), bg="#6e6aba").grid(row = 2,column=0)
    Entry(root,width=35,textvariable=username).grid(row=1,column = 1)
    Entry(root,width=35,textvariable=password).grid(row=2,column = 1)

    frameButton = Frame()
    Button(frameButton,text = "Login",bg="#6e6aba", command=solve,font=("Times New Roman",10)).pack(side=LEFT)
    Button(frameButton,text = "Xóa màn hình",font=("Times New Roman",10),command=clearAC).pack(side=LEFT)
    Button(frameButton,text = "Thoát",command=root.quit,font=("Times New Roman",10)).pack(side=LEFT)
    frameButton.grid(row=4,column=1)

    Label(root,text="Notification: ",font=("Times New Roman",10),bg="#6e6aba").grid(row = 5,column=0)
    Entry(root,width=35,textvariable=KQ,font=("Times New Roman",10)).grid(row=5,column = 1)
def solve():
    a = (username.get())
    b = (password.get())

    if a == "admin" and b == "adminn":
        root.destroy()
        Init()
        root.mainloop()
    else:
        KQ.set("Đăng nhập không thành công!")

def main():
    init()
    makecenter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
