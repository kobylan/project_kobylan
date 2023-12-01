from currency_converter import CurrencyConverter
from tkinter import *

root = Tk()
root.title('Converter')
root.geometry('300x250+300+300')
root.resizable(width=False, height=False)
root['bg'] = 'black'
c = CurrencyConverter()


header_frame = Frame(root)
header_frame.pack(fill=X)


header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)


h_currency = Label(header_frame, text='Валюта', bg='black', fg='lime', font='Arial 12 bold')
h_currency.grid(row=0, column=0, sticky=EW)
h_course = Label(header_frame, text='Курс', bg='black', fg='lime', font='Arial 12 bold')
h_course.grid(row=0, column=1, columnspan=2, sticky=EW)

# USD curs
usd_currency = Label(header_frame, text='USD', font='Arial 10')
usd_currency.grid(row=1, column=0, sticky=EW)
usd_one = Label(header_frame, text=1, font='Arial 10')
usd_one.grid(row=1, column=1, sticky=EW)
usd_converted = Label(header_frame, text='%.2f'  % c.convert(1, 'USD', 'RUB'), font='Arial 10')
usd_converted.grid(row=1, column=2, sticky=EW)

# EUR curs
eur_currency = Label(header_frame, text='EUR', font='Arial 10')
eur_currency.grid(row=1, column=0, sticky=EW)
eur_one = Label(header_frame, text=1, font='Arial 10')
eur_one.grid(row=1, column=1, sticky=EW)
eur_converted = Label(header_frame, text='%.2f' % c.convert(1, 'EUR', 'RUB'), font='Arial 10')
eur_converted.grid(row=1, column=2, sticky=EW)

# KZT curs

kzt_currency = Label(header_frame, text='kzt', font='Arial 10')
kzt_currency.grid(row=1, column=0, sticky=EW)
kzt_one = Label(header_frame, text=1, font='Arial 10')
kzt_one.grid(row=1, column=1, sticky=EW)
kzt_converted = Label(header_frame, text='%.2f' % c.convert(1, 'kzt', 'RUB'), font='Arial 10')
kzt_converted.grid(row=1, column=2, sticky=EW)

calc_frame = Frame(root, bg='black')
calc_frame.pack(expand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1, weight=1)

# RUB curs

l_rub = Label(calc_frame, text='Рубль: ', bg='black', fg='lime', font='Arial 12 bold' )
l_rub.grid(row=0, column=0, padx=10)
e_rub = Entry(calc_frame, justify=CENTER, font='Arial 10')
e_rub.grid(row=0, column=1, columnspan=2, pady=10, padx=10, sticky=EW)

btn_calc = Button(calc_frame, text='Submit' )
btn_calc.grid(row=1, column=1, columnspan=2, sticky=EW, padx=10)

res_frame = Frame(root)
res_frame.pack(expand=1, fill=BOTH, padx=5)
res_frame.grid_columnconfigure(1, weight=1)

l_usd = Label(res_frame, text='USD', font='Arial 10 bold')
l_usd.grid(row=2, column=0)
e_usd = Entry(res_frame, justify=CENTER, font='Arial 10')
e_usd.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)


# EUR
l_eur = Label(res_frame, text='EUR', font='Arial 10 bold')
l_eur.grid(row=2, column=0)
e_eur = Entry(res_frame, justify=CENTER, font='Arial 10')
e_eur.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)

#KZT

l_kzt = Label(res_frame, text='KZT', font='Arial 10 bold')
l_kzt.grid(row=2, column=0)
e_kzt = Entry(res_frame, justify=CENTER, font='Arial 10')
e_kzt.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)

root.mainloop()
