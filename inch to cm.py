import tkinter
root = tkinter.Tk()
root.title("Inches to Centimeters Converter")
width = 400
height = 400
root.geometry(f"{width}x{height}")
root.resizable(False, False)
def convert(n):
    return n * 2.54

entry = tkinter.Entry(root)
entry.pack(pady=10)
result = tkinter.Label(root, text="")
result.pack(pady=10)
root.button = tkinter.Button(root, text="Convert", command=lambda: result.config(text=f"{convert(float(entry.get())):.2f} cm"))
root.button.pack(pady=10)
root.mainloop()