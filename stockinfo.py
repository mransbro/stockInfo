import yfinance as yf

import xlsxwriter
from tkinter import *

top = Tk()
L1 = Label(top, text = "Stock symbol")
L1.pack( side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)

top.mainloop()