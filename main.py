import tkinter as tk

# ---------------- Window ---------------- #
root = tk.Tk()
root.title("Calculator")
root.geometry("360x600")
root.configure(bg="#1E1E1E")
root.resizable(False, False)

# ---------------- Display ---------------- #
display_var = tk.StringVar(value="0")

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 32),
    bg="#1E1E1E",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)

display.pack(fill="both", padx=20, pady=(30, 20), ipady=30)

# ---------------- Functions ---------------- #

def button_click(value):
    current = display_var.get()

    # Clear
    if value == "AC":
        display_var.set("0")
        return

    # Delete
    if value == "DEL":
        if len(current) > 1:
            display_var.set(current[:-1])
        else:
            display_var.set("0")
        return

    # Percentage
    if value == "%":
        try:
            result = float(current) / 100
            display_var.set(str(result))
        except:
            display_var.set("Error")
        return

    # Calculate
    if value == "=":
        try:
            expression = current.replace("×", "*").replace("÷", "/").replace("−", "-")
            result = eval(expression)

            if result == int(result):
                result = int(result)

            display_var.set(str(result))

        except:
            display_var.set("Error")
        return

    operators = ["+", "−", "×", "÷"]

    # Replace operator
    if value in operators:
        if current[-1] in operators:
            display_var.set(current[:-1] + value)
        else:
            display_var.set(current + value)
        return

    # Decimal
    if value == ".":
        last = current.split("+")[-1].split("−")[-1].split("×")[-1].split("÷")[-1]

        if "." in last:
            return

    # Remove leading zero
    if current == "0" or current == "Error":
        display_var.set(value)
    else:
        display_var.set(current + value)


# ---------------- Keyboard ---------------- #

def key_press(event):

    key = event.keysym
    char = event.char

    if char.isdigit():
        button_click(char)

    elif char == "+":
        button_click("+")

    elif char == "-":
        button_click("−")

    elif char == "*":
        button_click("×")

    elif char == "/":
        button_click("÷")

    elif char == ".":
        button_click(".")

    elif key == "Return":
        button_click("=")

    elif key == "BackSpace":
        button_click("DEL")

    elif key == "Escape":
        button_click("AC")
        # ---------------- Button Frame ---------------- #

button_frame = tk.Frame(root, bg="#1E1E1E")
button_frame.pack(fill="both", expand=True, padx=15, pady=15)

# Make rows and columns resize equally
for i in range(5):
    button_frame.rowconfigure(i, weight=1)

for j in range(4):
    button_frame.columnconfigure(j, weight=1)

# ---------------- Buttons ---------------- #

buttons = [
    ["AC", "DEL", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

for r, row in enumerate(buttons):
    for c, text in enumerate(row):

        if text == "":
            continue

        # Colors
        if text in ["÷", "×", "−", "+", "="]:
            bg = "#FF9500"   # Orange
            fg = "white"

        elif text in ["AC", "DEL", "%"]:
            bg = "#505050"   # Gray
            fg = "white"

        else:
            bg = "#333333"   # Dark Gray
            fg = "white"

        btn = tk.Button(
            button_frame,
            text=text,
            command=lambda t=text: button_click(t),
            font=("Arial", 20, "bold"),
            bg=bg,
            fg=fg,
            activebackground="#666666",
            activeforeground="white",
            bd=0,
            relief="flat",
            cursor="hand2"
        )

        btn.grid(
            row=r,
            column=c,
            padx=8,
            pady=8,
            sticky="nsew"
        )

# ---------------- Keyboard Binding ---------------- #

root.bind("<Key>", key_press)

# ---------------- Run App ---------------- #

root.mainloop()
