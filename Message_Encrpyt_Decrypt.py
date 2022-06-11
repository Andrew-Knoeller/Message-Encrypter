import PySimpleGUI as gui
import onetimepad

# Had a TON of problems with the diffrent encryption libaries. Finally found this
# OneTimePad libary that worked as the rest I could not get to decrypt properly
# The execeptions thrown on the other libraries had literally no information.
# The execptions just said: Could not decrypt.
# ANyway I decided on this simple program with these libaries.

# Liked this theme and I think it went good with the 'feel' of the program
gui.theme('DarkAmber')

# Simple layout. Text to inform user, Place to enter text and buttons for encrypt/decrypt
# Must use the ctrl-c shortcut to copy message as right-clicking doesnt open context box
layout = [ [gui.Text('Encrypt and Decrypt messages to friends!')],
           [gui.Text('Enter your message'), gui.InputText(key='-INPUT-', size=(85, 10))],
           [gui.Text(size=(40,1), key='-OUTPUT-')],
           [gui.Button('Encrypt'), gui.Button('Decrypt')],
           [gui.Multiline(font='Courier 10', key='-EXTRA-', size=(85,10))],
           [gui.Button('Close')] ]

screen = gui.Window('Encrypt/Decrypt', layout)



# Put in a loop so the screen stays until user hits 'X' at the top or the close button
while True:
    event, values = screen.Read()
    if event == gui.WIN_CLOSED or event == 'Close':
        break

# Logic for the encrypt button. Simply gather text and encrypt it using onetimepad
    if event == 'Encrypt':
        message = values['-INPUT-']
        encryptedmsg = onetimepad.encrypt(message, 'random')
        
        # Display results in multiline box for user to copy
        screen['-EXTRA-'].update(encryptedmsg)  

# Logic for the decrypt button. Simply gather text and decrypt it using onetimepad
    if event == 'Decrypt':
        message = values['-INPUT-']
        decryptedmsg = onetimepad.decrypt(message, 'random')
        screen['-EXTRA-'].update(decryptedmsg)
screen.close()