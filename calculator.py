from tkinter import *
import math

root = Tk()
root.geometry("350x500")
root.title("Calculator")
#root.resizable(0,0)
root.configure(bg='lavender')

scvalue = StringVar()
scvalue.set("")

def show(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())
                scvalue.set(value)
            except Exception as e:
                print(e)
                scvalue.set("Error")
    elif text == "Clear":
        scvalue.set("")
    else:
        scvalue.set(scvalue.get() + text)

screen = Entry(root, textvariable=scvalue, font="consolas 18 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)
f = Frame(root)
B = Button(f, text="7", fg="white", bg="black",pady=15, padx=30, font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
B = Button(f, text="8", bg="black",fg="white", pady=15, padx=30, font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
B = Button(f, text="9", bg="black", fg="white",pady=15, padx=30, font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
B = Button(f, text="=", pady=15, padx=30, fg="white", bg="orange", font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
f.pack()
f = Frame(root, bg="black")
B = Button(f, text="4", pady=15, bg="black",fg="white", padx=30, font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
B = Button(f, text="5", pady=15,  bg="black",fg="white",padx=30, font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
B = Button(f, text="6",  bg="black",fg="white",pady=15, padx=30, font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
B = Button(f, text="Clear", bg="black",fg="white", pady=15, padx=5, font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
f.pack()

f = Frame(root, bg="black")
B = Button(f, text="1", pady=15, padx=30,  bg="black",fg="white",font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
B = Button(f, text="2", pady=15, padx=30, bg="black",fg="white", font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
B = Button(f, text="3", pady=15, padx=30, bg="black",fg="white", font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
B = Button(f, text="√", pady=15, padx=30, bg="black",fg="white", font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
f.pack()

f = Frame(root)
B = Button(f, text="+", pady=15, padx=30,  bg="black",fg="white",font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
B = Button(f, text="-", pady=15, padx=30, bg="black",fg="white", font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
B = Button(f, text="*", pady=15, padx=30,  bg="black",fg="white",font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
B = Button(f, text="π", pady=15, padx=30, bg="black",fg="white", font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
f.pack()

f = Frame(root)
B = Button(f, text="/", pady=15, padx=30, bg="black",fg="white", font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
B = Button(f, text="//", pady=15, padx=23,  bg="black",fg="white",font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
B = Button(f, text="%", pady=15, padx=31,  bg="black",fg="white",font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
B = Button(f, text="**", pady=15, padx=24,  bg="black",fg="white",font="consolas 18 bold")
B.pack(side=LEFT)
B.bind("<Button-1>", show)
f.pack()

root.mainloop()