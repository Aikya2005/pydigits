import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)
expression = ""
input_text = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=input_text,
    font=('Arial', 20),
    bd=10,
    insertwidth=2,
    width=14,
    borderwidth=4,
    justify='right'
)
entry.pack(pady=10)
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)
def clear():
    global expression
    expression = ""
    input_text.set("")
def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""
frame = tk.Frame(root)
frame.pack()

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(frame, text=text, width=5, height=2,
                  command=equal).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(frame, text=text, width=5, height=2,
                  command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5)
tk.Button(root, text="Clear", width=20, height=2,
          command=clear).pack(pady=10)
root.mainloop()
