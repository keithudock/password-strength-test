#! python3
# passwordStrengthTester - Tests the strengh of the password entered

import re, tkinter

def passwordCheck():
    print('Password Checked')
    numRegex = re.compile(r'''(
        .*[0-9]{1,}.*
        )''',re.VERBOSE)

    capRegex = re.compile(r'''(
        .*[A-Z]{1,}.*
        )''',re.VERBOSE)

    lowerRegex = re.compile(r'''(
        .*[a-z]{1,}.*
        )''',re.VERBOSE)

    password = text.get()

    if len(password) >= 8:
        if numRegex.search(password) is not None:
            if capRegex.search(password) is not None:
                if lowerRegex.search(password) is not None:
                    print('Good!')
                    label['fg'] = 'green'
                    label['text'] = 'Good!'
                else:
                    print('Password is not enough!')
                    label['fg'] = 'red'
                    label['text'] = 'Password is not strong enough!'
            else:
                print('Password is not enough!')
                label['fg'] = 'red'
                label['text'] = 'Password is not strong enough!'
        else:
            print('Password is not enough!')
            label['fg'] = 'red'
            label['text'] = 'Password is not strong enough!'
    else:
        print('Password is not enough!')
        label['fg'] = 'red'
        label['text'] = 'Password is not strong enough!'

def showHide():
    if var.get() == 1:
        text['show'] = ''
    else:
        text['show'] = '*'

    
# TODO: Adjust frame to resize with window 

# Create Tkinter Frame
root = tkinter.Tk()

# Set title and window size
root.title('Password Checker')
root.geometry("425x250")

# Label for correctness check
label = tkinter.Label(root,text='').grid(row=1,columnspan=2, sticky='S', padx=20, pady=10)

# Create a text box and have it span the center
text = tkinter.Entry(root, width=30, show='*').grid(row=2,column=0, padx=20, pady=10, sticky='N')

# Show Password checkbox
var = tkinter.IntVar()
show = tkinter.Checkbutton(root, text='Show Password', variable=var, command=showHide).grid(row=2, column=1)

# Button to check password
check = tkinter.Button(root, text='Check Password', command=passwordCheck).grid(row=3,columnspan=2, sticky='S')

# Quit Button
quit = tkinter.Button(root, text='QUIT', fg='red', command=root.destroy).grid(row=4,columnspan=2, sticky='S')


# Requirements Label
requirements = tkinter.Label(root,text='Password must contain:\nAt least 8 characters\nAt least 1 lowercase letter\nAt least 1 uppercase letter\nAt least 1 number')
requirements.grid(row=5,columnspan=2, sticky='S', padx=20, pady=10)

root.bind('<Return>', passwordCheck)
root.mainloop()


