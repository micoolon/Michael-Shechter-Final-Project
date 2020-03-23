from tkinter import *
from tkinter import font as tkFont
import hashlib
import csv

# main window of the app
root = Tk()
root.title('Registration System')
root.minsize(1008, 500)
root.resizable(width=False, height=False)

root.configure(bg='LightSkyBlue')


# Main menu. Starts here and also goes back here when the corresponding button is clicked, and when registration is done
def main_menu():
    for widget in root.winfo_children():
        widget.grid_forget()

    button_font = tkFont.Font(family='Rockwell', size=12)
    title_font = tkFont.Font(family='Times New Roman', size=30)

    welcome = Label(root, text= 'Welcome to the Portal!', font=title_font, bg='LightSkyBlue', fg='OrangeRed3')
    welcome.grid(row=2, column=10, pady=130, padx=130)

    reg_btn = Button(root, text='Register', font=button_font)
    reg_btn.grid(row=3, column=0, pady=40)
    reg_btn.config(height=4, width=20, bg='pale goldenrod')
    reg_btn.bind('<Button-1>', to_reg)

    log_btn = Button(root, text='Login', font=button_font)
    log_btn.grid(row=3, column=20)
    log_btn.config(height=4, width=20, bg='pale goldenrod')
    log_btn.bind('<Button-1>', to_log)

'''
This is the registration page. you get here after clicking 'register' in the main menu.
It takes the details, and moves to the next function.
'''
def to_reg(event):
    for widget in root.winfo_children():
       widget.grid_forget()
    parameters = []

    title_font = tkFont.Font(family='Times New Roman', size=15)
    title = Label(root, text= 'Please provide details', font=title_font, bg='LightSkyBlue', fg='darkgreen')
    title.grid(row=2, column=3, pady=50, padx=20)

    f_name = Label(root, text='First Name:', bg='LightSkyBlue')
    f_name.grid(row=5, column=1, pady=5)
    f_name_entry = Entry(root, width=20)
    f_name_entry.grid(row=5, column=2)
    parameters.append(f_name_entry)

    l_name = Label(root, text='Last Name:', bg='LightSkyBlue')
    l_name.grid(row=6, column=1, pady=5)
    l_name_entry = Entry(root, width=20)
    l_name_entry.grid(row=6, column=2)
    parameters.append(l_name_entry)

    email = Label(root, text='Email:         ', bg='LightSkyBlue')
    email.grid(row=7, column=1, pady=5)
    email_entry = Entry(root, width=20)
    email_entry.grid(row=7, column=2)
    parameters.append(email_entry)

    gender = Label(root, text='Gender:      ', bg='LightSkyBlue')
    gender.grid(row=8, column=1)

    v = IntVar()
    male = Radiobutton(root, text='M', variable=v, value=1, bg='LightSkyBlue')
    male.grid(row=8, column=2, pady=5)
    female = Radiobutton(root, text='F', variable=v, value=2, bg='LightSkyBlue')
    female.grid(row=8, column=3)
    parameters.append(v)

    username = Label(root, text='Username:', bg='LightSkyBlue')
    username.grid(row=9, column=1, pady=5)
    username_entry = Entry(root, width=20)
    username_entry.grid(row=9, column=2)
    parameters.append(username_entry)

    password = Label(root, text='Password:', bg='LightSkyBlue')
    password.grid(row=10, column=1, pady=5)
    password_entry = Entry(root, show='*', width=20)
    password_entry.grid(row=10, column=2)
    parameters.append(password_entry)

    # lambda function to make the register button go to next function.
    commit = lambda: reg_handler(parameters)
    reg_btn = Button(root, text='Register', command=commit)
    reg_btn.grid(row=12, column=3)
    reg_btn.config(bg='pale goldenrod')

    to_main = Button(root, text='Back to Main Menu', command=main_menu)
    to_main.config(height=2, width=15, bg='pale goldenrod')
    to_main.grid(row=14, column=0, pady=50)


'''
This checks if there is any empty field left after clicking 'register', and also checks if the username already
exists. if everything checks out, it goes to the registration function
'''
def reg_handler(vars):
    a = (vars[0]).get()
    if len(a) == 0 or a == 0:
        empty = Label(root, text='   Please fill all details!   ', bg='LightSkyBlue', fg='red')
        empty.grid(row=7, column=3)
        to_reg()
    b = (vars[1]).get()
    if len(b) == 0 or b == 0:
        empty = Label(root, text='   Please fill all details!   ', bg='LightSkyBlue', fg='red')
        empty.grid(row=7, column=3)
        to_reg()
    c = (vars[2]).get()
    if len(c) == 0 or c == 0:
        empty = Label(root, text='   Please fill all details!   ', bg='LightSkyBlue', fg='red')
        empty.grid(row=7, column=3)
        to_reg()
    if (vars[3]).get() == 1:
        d = 'M'
    else:
        d = 'F'
    e = (vars[4]).get()
    if len(e) == 0 or e == 0:
        empty = Label(root, text='   Please fill all details!   ', bg='LightSkyBlue', fg='red')
        empty.grid(row=7, column=3)
        to_reg()
    f = (vars[5]).get()
    if len(f) == 0 or f == 0:
        empty = Label(root, text='   Please fill all details!   ', bg='LightSkyBlue', fg='red')
        empty.grid(row=7, column=3)
        to_reg()
    f = hashlib.sha256(f.encode())
    f = str(f.hexdigest())

    # used try because if the file doesn't exist yet, it can crash.
    try:
        with open('users.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                for field in row:
                    if field == e:
                        already = Label(root, text='Username already exists!', bg='LightSkyBlue', fg='red')
                        already.grid(row=7, column=3)
                        to_reg()
        registration(a, b, c, d, e, f)
    except FileNotFoundError:
        registration(a, b, c, d, e, f)


# This function registers the details to the CSV file and then sends the user back to main menu
def registration(a, b, c, d, e, f):
    with open('users.csv', 'a') as csv_file:
        csv_file.write(f'{a},{b},{c},{d},{e},{f}\n')
    main_menu()


# This is the login page. you get here after clicking 'Login' in the main menu. It requests the login details.
def to_log(event):
    for widget in root.winfo_children():
       widget.grid_forget()

    vars = []

    title_font = tkFont.Font(family='Times New Roman', size=15)
    title = Label(root, text='Please provide login details', font=title_font, bg='LightSkyBlue', fg='darkgreen')
    title.grid(row=2, column=3, pady=50, padx=20)

    username = Label(root, text='Username:', bg='LightSkyBlue')
    username.grid(row=3, column=1, pady=5)
    username_entry = Entry(root, width=20)
    username_entry.grid(row=3, column=2)
    vars.append(username_entry)

    password = Label(root, text='Password:', bg='LightSkyBlue')
    password.grid(row=4, column=1, pady=5)
    password_entry = Entry(root, show='*', width=20)
    password_entry.grid(row=4, column=2)
    vars.append(password_entry)

    commit = lambda: log_handler(vars)
    log_btn = Button(root, text='Login', command=commit)
    log_btn.grid(row=5, column=3)
    log_btn.config(bg='pale goldenrod')

    to_main = Button(root, text='Back to Main Menu', command=main_menu)
    to_main.config(height=2, width=15, bg='pale goldenrod')
    to_main.grid(row=6, column=0, pady=100)

# This moves the details from the login page to the checker.
def log_handler(vars):
    a = (vars[0]).get()
    b = (vars[1]).get()
    b = hashlib.sha256(b.encode())
    b = str(b.hexdigest())
    login_check(a, b)

# This checks that the login details are correct. If everything is correct, it sends the user to the last page.
def login_check(a, b):
    checker = 0
    with open('users.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            for field in row:
                if field == a:
                    for field_b in row:
                        if field_b == b:
                            checker = 1
                        else:
                            checker = 2

    if checker == 1:
        print('login successful!')
        login(a)
    else:
        incorrect_details = Label(root, text='Incorrect details!', bg='LightSkyBlue', fg='red')
        incorrect_details.grid(row=3, column=3)


# This is the page you get when you have logged in successfully.
def login(a):
    for widget in root.winfo_children():
       widget.grid_forget()
    with open('users.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            for field in row:
                if field == a:
                    titlefont = tkFont.Font(family='Times New Roman', size=15)
                    title = Label(root, text=f'Welcome {row[0]}!'.title(), font=titlefont, bg='LightSkyBlue',fg='darkgreen')
                    title.grid(row=2, column=3, pady=50, padx=250)
                    output = f'Name: {str.capitalize(row[0])} \n Last Name: {str.capitalize(row[1])} \n Email: {row[2]} \n Gender: {row[3]}'
                    details = Label(root, text=output, bg='LightSkyBlue', fg='purple3',)
                    details.grid(row=5, column=3)

    to_main = Button(root, text='Back to Main Menu', command=main_menu)
    to_main.config(height=2, width=15, bg='pale goldenrod')
    to_main.grid(row=6, column=0, pady=100)


main_menu()

root.mainloop()