#! python3
# passwordStrengthTester - Tests the strengh of the password entered

import re, tkinter

# TODO: Add uppercase and lowercase requirement
# TODO: Add 1 digit requirement
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

    password1 = numRegex.search(password)
    password2 = capRegex.search(password1)
    password3 = lowerRegex.search(password2)

    if password3 is None or len(password) < 8:
        #print('Password is not strong enough')
        label['fg'] = 'red'
        label['text'] = 'Password is not strong enough!'
    else:
        #print('Good!')
        label['fg'] = 'green'
        label['text'] = 'Good!'
    
 
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



root.mainloop()


