import tkinter as tk
window = tk.Tk()
window.title("CALCULATOR")
window.geometry("500x300")
number=tk.Entry(window)
number.pack()
numbers=tk.Entry(window)
numbers.pack()
instructions = tk.Label(window, text="+:add,-:subtract,*:multiply,/:division,//:floor division,%:remainder,**:power")
instructions.pack()
opt=tk.Entry(window)
opt.pack()
def run():
    string = number.get()
    a=int(string)
    strings = numbers.get()
    b=int(strings)
    option = opt.get()
    if option=="+":
        s=a+b
        result = tk.Label(window,text=f"addition ={s}")
        result.pack()
    elif option=="-":
        s=a-b
        result = tk.Label(window,text=f"subtraction ={s}")
        result.pack()
    elif option=="*":
        s=a*b
        result = tk.Label(window,text=f"multiplication ={s}")
        result.pack()
    elif option=="/":
        s=a/b
        result = tk.Label(window,text=f"division ={s}")
        result.pack()
    elif option=="//":
        s=a//b
        result = tk.Label(window,text=f"floor division ={s}")
        result.pack()
    elif option=="%":
        s=a%b
        result = tk.Label(window,text=f"remainder ={s}")
        result.pack()
    elif option=="**":
        s=a**b
        result = tk.Label(window,text=f"power ={s}")
        result.pack()
    else:
        error = tk.Label(window, text="ERROR")
        error.pack()
tk.Button(window, text="click", command=run).pack()
window.mainloop()
    

      
