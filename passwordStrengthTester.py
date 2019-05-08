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

    # TODO: Debug to find why password checker doesn't update label

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
    
# TODO: Adjust frame to resize with window 

# Create Tkinter Frame
root = tkinter.Tk()

# Set title and window size
root.title('Password Checker')
root.geometry("300x125")

# Label for correctness check
label = tkinter.Label(root,text='')
label.grid(row=1,columnspan=2, sticky='S', padx=20, pady=10)

# Create a text box and have it span the center
text = tkinter.Entry(root, width=30)
text.grid(row=2,columnspan=2, padx=20, pady=10, sticky='N')

# Button to check password
check = tkinter.Button(root, text='Check Password', command=passwordCheck)
check.grid(row=3,column=0, sticky='S')

# Quit Button
quit = tkinter.Button(root, text='QUIT', fg='red', command=root.destroy)
quit.grid(row=3,column=1, sticky='S')

# TODO: Add Requirements Label



root.mainloop()


