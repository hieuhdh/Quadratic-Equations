from makeCenter import *
from math import *

def clearAC():
    A.set("")
    B.set("")
    C.set("")
    KQ.set("")

def solve():
    a = float(A.get())
    b = float(B.get())
    c = float(C.get())
    file = open("log.txt","a", encoding= "utf-8")
    if a == 0:
        if b==0 and c == 0:
            KQ.set("Phương trình vô số nghiệm trên tập R")
            file.writelines(f"Phương trình {a}x^2 + {b}x + {c} có vô số nghiệm trên tập R \n")
        elif b == 0 and c != 0:
            KQ.set("Phương trình vô nghiệm trên tập R")
            file.writelines(f"Phương trình {a}x^2 + {b}x + {c} vô nghiệm trên tập R \n")
        else:
            KQ.set("x = " + str(eval("-c/b")))
            file.writelines(f"Phương trình {a}x^2 + {b}x + {c} nhận x = {-c/b} làm nghiệm. \n")
            
    else:
        delta = pow(b,2) - 4*a*c
        if delta > 0:
            KQ.set(f"x1 = {((-b+sqrt(delta))/2*a).__round__(8)}; x2={((-b-sqrt(delta))/2*a).__round__(8)}")
            file.writelines(f"Phương trình {a}x^2 + {b}x + {c} nhận x1 = {((-b+sqrt(delta))/2*a).__round__(8)} và x2 = {((-b-sqrt(delta))/2*a).__round__(8)} làm 2 nghiệm thực. \n")
        elif delta == 0:
            KQ.set("x1 = x2 = " + str(eval("-b/2*a")))
            file.writelines(f"Phương trình {a}x^2 + {b}x + {c} nhận x = {-b/2*a} làm nghiệm \n")
        else:
            s = "i"
            tmp = sqrt(-delta)/2*a
            second = str(tmp)+s
            first = -b/2*a
            x1 = str(str(first) + "+" + second)
            x2 = str(str(first) + "-" + second)
            KQ.set(f"x1 = {x1}; x2={x2}")
            file.writelines(f"Phương trình {a}x^2 + {b}x + {c} nhận x1 = {x1} và x2 = {x2} làm 2 nghiệm phức. \n")
    file.close()

def Init():
    global root
    root = Tk()
    makecenter(root)
    global A, B, C, KQ
    A = StringVar()
    B = StringVar()
    C = StringVar()
    KQ = StringVar()
    root.title("deuteri")
    root.minsize(height=200,width=300)
    root.resizable(height=True,width=True)
    root.configure(background='#6e6aba')
    Label(root,text="Giải phương trình bậc 2", fg="black",font=("Times New Roman",17), justify=CENTER,bg="#6e6aba").grid(row = 0,columnspan=2)
    Label(root,text="Hệ số a: ",font=("Times New Roman",10),bg="#6e6aba").grid(row = 1,column=0)
    Label(root,text="Hệ số b: ",font=("Times New Roman",10),bg="#6e6aba").grid(row = 2,column=0)
    Label(root,text="Hệ số c: ",font=("Times New Roman",10),bg="#6e6aba").grid(row = 3,column=0)
    Entry(root,width=35,textvariable=A).grid(row=1,column = 1)
    Entry(root,width=35,textvariable=B).grid(row=2,column = 1)
    Entry(root,width=35,textvariable=C).grid(row=3,column = 1)

    frameButton = Frame()
    Button(frameButton,text = "Giải",bg="#6e6aba", command=solve,font=("Times New Roman",10)).pack(side=LEFT)
    Button(frameButton,text = "Tiếp tục",font=("Times New Roman",10),command=clearAC).pack(side=LEFT)
    Button(frameButton,text = "Thoát",command=root.quit,font=("Times New Roman",10)).pack(side=LEFT)
    frameButton.grid(row=4,column=1)

    Label(root,text="Kết quả: ",font=("Times New Roman",10),bg="#6e6aba").grid(row = 5,column=0)
    Entry(root,width=35,textvariable=KQ,font=("Segoe UI",10)).grid(row=5,column = 1)

