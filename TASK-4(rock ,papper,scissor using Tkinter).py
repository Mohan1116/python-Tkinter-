import tkinter as tk
import random
window = tk.Tk()
window.title("Rock Paper Scissor")
window.geometry("500x300")
instructions = tk.Label(window, text="Rock Beats Scissor    Scissor Beats Paper      Paper Beats Rock")
instructions.place(x=50,y=5)
result = tk.Label(window, text="Choose an option")
result.place(x=250,y=50)
def rock():
    result.config(text="ME:  Rock")
    a = random.choice(["paper ","scissor"])
    robot_result = tk.Label(window,text=f"ROBOT:   {a}")
    robot_result.place(x=250,y=70)
    if a==("paper "):
        winner = tk.Label(window, text="ROBOT WON")
        winner.place(x=250,y=90)
    else:
        winner = tk.Label(window, text="YOU WON",width=10)
        winner.place(x=250,y=90) 
tk.Button(window, text="Rock", command=rock).place(x=100,y=50)
def paper():
    result.config(text="ME:  paper")
    a = random.choice(["rock   ","scissor"])
    robot_result = tk.Label(window,text=f"ROBOT:   {a}")
    robot_result.place(x=250,y=70)
    if a==("scissor"):
        winner = tk.Label(window, text="ROBOT WON")
        winner.place(x=250,y=90)
    else:
        winner = tk.Label(window, text="YOU WON",width=10)
        winner.place(x=250,y=90)
tk.Button(window, text="Paper", command=paper).place(x=100,y=100)
def scissor():
    result.config(text="ME:  scissor")
    a = random.choice(["rock   ","paper "])
    robot_result = tk.Label(window,text=f"ROBOT:   {a}")
    robot_result.place(x=250,y=70)
    if a==("rock   "):
        winner = tk.Label(window, text="ROBOT WON")
        winner.place(x=250,y=90)
    else:
        winner = tk.Label(window, text="YOU WON",width=10)
        winner.place(x=250,y=90)
tk.Button(window, text="Scissor", command=scissor).place(x=100,y=150)
window.mainloop()
        
    
    



