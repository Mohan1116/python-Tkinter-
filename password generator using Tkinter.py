import tkinter as tk
import random
window = tk.Tk()
window.title("PASSWORD GENERATION")
window.geometry("500x300")
length_label = tk.Label(window, text="required password legth")
length_label.pack()
password_length = tk.Entry(window,width=50)
password_length.pack()
a= random.choice([chr(i) for i in range(97, 123)])
b= random.choice([chr(i) for i in range(65, 90)])
c= random.choice([chr(i) for i in range(48, 57)])
d= random.choice(["@","#","$","&","!"])
def length():
    string = password_length.get()
    i=int(string)
    if i<4:
        error = tk.Label(window, text="minimum password lenght should be 4")
        error.pack()
    else:
        strength_label = tk.Label(window, text="password strength  1:low,2:medium,3:high")
        strength_label.pack()
        password_strength = tk.Entry(window,width=50)
        password_strength.pack()
        def strength():
            string = password_strength.get()
            integer=int(string)
            if integer==1:
                l = [a, b, c, d]
                j=random.choices(l,weights=[1,1,4,1],k=i)
                s="".join(str(i)for i in j)
                result = tk.Label(window,text=f"{s}")
                result.pack()
                def copy_password():
                    window.clipboard_clear()
                    window.clipboard_append(s)
                tk.Button(window,text="Copy Password",command=copy_password).pack()
            elif integer==2:
                l = [a, b, c, d]
                j=random.choices(l,weights=[2,2,2,2],k=i)
                s="".join(str(i)for i in j)
                result = tk.Label(window,text=f"{s}")
                result.pack()
                def copy_password():
                    window.clipboard_clear()
                    window.clipboard_append(s)
                tk.Button(window,text="Copy Password",command=copy_password).pack()
            elif integer==3:
                l = [a, b, c, d]
                j=random.choices(l,weights=[1,1,1,1],k=i)
                s="".join(str(i)for i in j)
                result = tk.Label(window,text=f"{s}")
                result.pack()
                def copy_password():
                    window.clipboard_clear()
                    window.clipboard_append(s)
                tk.Button(window,text="Copy Password",command=copy_password).pack()
            else:
                label = tk.Label(window, text="ERROR")
                label.pack()
        tk.Button(window, text="click",command=strength).pack()
tk.Button(window, text="click", command=length).pack()
window.mainloop()

        
