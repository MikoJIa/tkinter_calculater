import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Калькулятор')
window.geometry('385x435+900+500')
ico = tk.PhotoImage(file='calculator_icon.png')
window.wm_iconphoto(False, ico)
window['bg'] = 'coral4'
# какой вид событий мы обрабатываем


def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char == '\r':
        calculation()
    elif event.char == 'c':
        clear_entry()



window.bind('<Key>', press_key)


def add_digit(numeral):
    value = calc_ent.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc_ent['state'] = tk.NORMAL
    calc_ent.delete(0, tk.END)
    calc_ent.insert(0, value+numeral)
    calc_ent['state'] = tk.DISABLED


def add_operation(symbol):
    value = calc_ent.get()
    calc_ent['state'] = tk.NORMAL
    if value[-1] in '+-/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculation()
        value = calc_ent.get()
    calc_ent.delete(0, tk.END)
    calc_ent.insert(0, value + symbol)
    calc_ent['state'] = tk.DISABLED


def make_button(numeral):
    return tk.Button(master=frame_main_win,
                     command=lambda: add_digit(numeral),
                     text=numeral, font=('Arial', 30),
                     width=3, relief=tk.RAISED, bd='5')


def make_operation_button(symbol):
    return tk.Button(master=frame_main_win, text=symbol,
                     command=lambda: add_operation(symbol),
                     font=('Arial', 30), width=3, relief=tk.RAISED, bd='5', fg='brown1')


def make_calc_button(symbol):
    return tk.Button(master=frame_main_win, text=symbol,
                     command=calculation,
                     font=('Arial', 30), width=3, relief=tk.RAISED, bd='5', fg='brown1')


def make_clear_button(symbol):
    return tk.Button(master=frame_main_win, text=symbol, command=clear_entry, font=('Arial', 30, 'bold'),
                     width=3, relief=tk.RAISED, bd=5, fg='brown1')


def calculation():
    value = calc_ent.get()
    calc_ent['state'] = tk.NORMAL
    if value[-1] in '+-/*':
        operation = value[-1]
        value = value[:-1] + operation + value[:-1]
    calc_ent.delete(0, tk.END)
    try:
        calc_ent.insert(0, eval(value))
        calc_ent['state'] = tk.DISABLED
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'Необходимо вводить только цифры!!!')
        calc_ent.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль делить нельзя!!!')
        calc_ent.insert(0, 0)


def clear_entry():
    calc_ent['state'] = tk.NORMAL
    calc_ent.delete(0, tk.END)
    calc_ent.insert(0, '0')
    calc_ent['state'] = tk.DISABLED



frame_main_win = tk.Frame(master=window, width=400, height=400, bg='BlanchedAlmond')
frame_main_win.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

calc_ent = tk.Entry(master=frame_main_win, relief=tk.SUNKEN, bd=5, font=('Arial', 25, 'bold'), width=19, justify=tk.RIGHT)
# Поместим в поле ввода 0 по умолчанию
calc_ent.insert(0, '0')
calc_ent['state'] = tk.DISABLED
calc_ent.grid(row=0, column=0, columnspan=4, padx=3)

# в command  мы определяем лямбду функцию для того чтобы каждая кнопка выполняла своё действие
make_button('1').grid(row=1, column=0, stick='wens', padx=3, pady=3)
make_button('2').grid(row=1, column=1, stick='wens', padx=3, pady=3)
make_button('3').grid(row=1, column=2, stick='wens', padx=3, pady=3)
make_button('4').grid(row=2, column=0, stick='wens', padx=3, pady=3)
make_button('5').grid(row=2, column=1, stick='wens', padx=3, pady=3)
make_button('6').grid(row=2, column=2, stick='wens', padx=3, pady=3)
make_button('7').grid(row=3, column=0, stick='wens', padx=3, pady=3)
make_button('8').grid(row=3, column=1, stick='wens', padx=3, pady=3)
make_button('9').grid(row=3, column=2, stick='wens', padx=3, pady=3)
make_button('0').grid(row=4, column=1, stick='wens', padx=3, pady=3)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=3, pady=3)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=3, pady=3)
make_operation_button('*').grid(row=3, column=3, stick='wens', padx=3, pady=3)
make_operation_button('/').grid(row=4, column=3, stick='wens', padx=3, pady=3)

make_calc_button('=').grid(row=4, column=2, stick='wens', padx=3, pady=3)

make_clear_button('C').grid(row=4, column=0, stick='wens', padx=3, pady=3)

# задаём минимальный размер колонок  и распределяем их равномерно по frame-у
frame_main_win.grid_columnconfigure(0, minsize=60)
frame_main_win.grid_columnconfigure(1, minsize=60)
frame_main_win.grid_columnconfigure(2, minsize=60)
frame_main_win.grid_columnconfigure(3, minsize=60)

frame_main_win.grid_rowconfigure(1, minsize=60)
frame_main_win.grid_rowconfigure(2, minsize=60)
frame_main_win.grid_rowconfigure(3, minsize=60)
frame_main_win.grid_rowconfigure(4, minsize=60)
frame_main_win.grid_rowconfigure(5, minsize=60)

window.mainloop()