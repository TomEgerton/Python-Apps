import tkinter as tk
import colours as col
import random
import threading

colours = col.ColourDic()
window = tk.Tk()


def randCol():
    """
    Sets a timed interval to change the box colour randomly every 1.5 seconds
    :return:
    Updated colours
    """
    threading.Timer(1.5, randCol).start()
    x = colours[random.randint(0, 19)]
    hexval = col.RGBToHex(x["r"], x["g"], x["b"])
    hexcomp = col.CompCol(x["r"], x["g"], x["b"])
    label1['bg'] = hexval
    label1['text'] = hexval
    label2['fg'] = hexval
    label2['bg'] = hexcomp
    label2['text'] = hexcomp
    label1['fg'] = hexcomp


label1 = tk.Label(width=40, height=20)
label2 = tk.Label(width=40, height=20)
label1.pack()
label2.pack()
randCol()
window.mainloop()
