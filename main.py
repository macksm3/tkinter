# Glossary Project

# import coin module for proof of concept testing
from coin import Coin

from tkinter import *
from tkinter import messagebox  # import messagebox library
from tkinter import colorchooser  # submodule
from tkinter import filedialog
# from PIL import ImageTk, Image


# key down function from original test code
def click(event=None):
    # entered_text = textentry.get()  # this will collect the text from the text entry box
    output.delete(0.0, END)
    output.insert(END, penny.get_subtotal(textentry.get()))


# from BroCode
def submit():
    username = entry.get()
    print(f"Hello {username}!")
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get())-1, END)


def display():
    if(x.get()):     # get value of variable x from checkbutton
        print("You agree!")
    else:
        print("You don't agree :(")


food = ["pizza", "hamburger", "hotdog"]

def order():
    if(f.get()==0):
        print("You ordered pizza!")
    elif(f.get()==1):
        print("You ordered a hamburger!")
    elif(f.get()==2):
        print("You ordered a hotdog!")
    else:
        print("huh?")

def scale_submit():
    print("The temperature is: " + str(scale.get()) + " degreesC")

def list_select():

    food =[]

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)

    # print(listbox.get(listbox.curselection()))

def add_to_list():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def delete_from_list():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())


def messagebox_click():
    # messagebox.showinfo(title='Info message box',message='You are a person')
    """for i in range(0, 5):
        messagebox.showwarning(title='WARNING!', message='You have A VIRUS!!!!')
        i += 1"""
    # messagebox.showinfo(title='ERROR!', message='something went wrong :(')

    #if messagebox.askokcancel(title='ask ok cancel', message='Do you want to?'):
        #print('You did it!')
    #else:
        #print('You canceled! :(')

    #if messagebox.askretrycancel(title='ask retry cancel', message='Do you want to retry?'):
        #print('You retried!')
    #else:
        #print('You canceled! :(')

    #if messagebox.askyesno(title='ask yes or no', message='Do you agree?'):
        #print('congrats! :)')
    #else:
        #print('Too bad! :(')

    #answer = messagebox.askquestion(title='ask question', message='Do you like pie?')
    #if(answer == 'yes'):
        #print('I like pie too')
    #else:
        #print('Why not? :(')

    answer = messagebox.askyesnocancel(title='yes no cancel',
                                       message='Do you like to code?',
                                       #icon='warning',      # triangle
                                       #icon='info',         # light bulb
                                       #icon='error',        # red circle
                                       )
    if(answer == True):
        print('You like to code')
    elif(answer == False):
        print('Then why are you watching a video on coding? :(')
    else:
        print('You have dodged the question? :(')


def change_color():
    window.config(bg=colorchooser.askcolor()[1])  # change background color
    '''
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    print(colorHex)
    window.config(bg=colorHex)  # change background color
    '''

def get_text():
    text_input = text_area.get("1.0", END)
    print(text_input)

def saveFile():
    file = filedialog.asksaveasfile(initialdir="/home/m3/PycharmProjects/tkinter",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("markdown file", ".md"),   # does not work like demo
                                        ("HTML file", ".html"),     # does not work like demo
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = str(text_area.get("1.0", END))
    # filetext = input("Enter text to save here: ")  # use this for text console entry of text to save
    file.write(filetext)
    file.close()


def openFile():
    filepath = filedialog.askopenfilename(initialdir="/home/m3/PycharmProjects/tkinter",
                                          title="Open file okay?",
                                          filetypes=(("text files", "*.txt"),
                                                     ("markdown", "*.md"),
                                                     ("all files", "*.*")),
                                          )
    file = open(filepath, 'r')
    print(file.read())
    file.close()


def cut():
    print("You cut some text")

def copy():
    print("You copied some text")

def paste():
    print("You pasted some text")





'''
# exit function replaced by direct button press to exit
def close_window():
    window.destroy()
    exit()
'''

# instantiate coin here
penny = Coin("pennies", 0.01)  # test project code


# main window generation starts here
window = Tk()
window.title("Here is my Project")
window.config(background="cyan")

# from BroCode
icon = PhotoImage(file='m3-blue-icon.png')
window.iconphoto(True, icon)

# exit button from original test project
quit_button = Button(window, text="Exit Program", width=10, command=window.quit)
quit_button.grid(row=0, column=0, sticky=N)

# My Photo from original test project
my_logo = PhotoImage(file="ConsultLogo2.png")
logo_label = Label(window, image=my_logo, bg='cyan')
logo_label.grid(row=0, column=1, columnspan=2)

# color chooser button
color_button = Button(text='change color', command=change_color)
color_button.grid(row=0, column=4, sticky=N)

# from BroCode
add_img = PhotoImage(file='conf_icon_edit.png')

# label hybrid from original and BroCode
first_label = Label(window,
                    text="Enter a number ->",
                    font="Ariel 14 bold",
                    fg="#00ff00",
                    bg="black",
                    relief=RAISED,
                    bd=5,
                    padx=20,
                    pady=10,
                    image=add_img,
                    compound='left')
first_label.grid(row=1, column=1, pady=2)

# text box from the original test project as user entry
textentry = Entry(window, width=10, bg="yellow")
textentry.grid(row=1, column=2, sticky=W)
textentry.focus()

# text box from original test project for output
output = Text(window, width=50, height=4, wrap=WORD, background="yellow")
output.grid(row=2, column=1)

bn_enter_icon = PhotoImage(file='bn_enter_down.gif')

# create submit button
button = Button(window,
                text="get value\nof pennies",
                command=click,
                font=("Hack", 13),
                fg="#00FF00",
                bg="black",
                activeforeground='#00FF00',
                activebackground='black',
                state=ACTIVE,
                image=bn_enter_icon,
                compound='left')
button.grid(row=2, column=2, columnspan=3, sticky=W)
window.bind('<Return>', click)
window.bind('<KP_Enter>', click)

entry = Entry(window,
              font=("Comic Sans MS", 18),
              fg="#00FF00",
              bg="black",
              )
entry.insert(0, "enter text")
#entry.config(show="*")  # replace every character with *
#entry.config(state=DISABLED)
entry.grid(row=3, column=1)

submit_button = Button(window, text="submit", command=submit)
submit_button.grid(row=3, column=4)

delete_button = Button(window, text="delete", command=delete)
delete_button.grid(row=3, column=3)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.grid(row=3, column=2)


checkbox_photo = PhotoImage(file='pgs_checked_icon.png')
x = BooleanVar()
check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=('Mathjax_Typewriter', 20),
                           fg="#00FF00",
                           bg="black",
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=checkbox_photo,
                           compound='left')
check_button.grid(row=4, column=1)


pizzaImage = PhotoImage(file='Crestron swirl 40x40.png')
hamburgerImage = PhotoImage(file='CrestronBlue 40x40.png')
hotdogImage = PhotoImage(file='crestron icon.png')
foodImages = [pizzaImage, hamburgerImage, hotdogImage]
f = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],     # adds text to radio buttons
                              variable=f,       # groups radiobuttons together if they share the same variable
                              value=index,       # assigns each radiobuton a different value
                              padx=25,
                              font=("Impact", 20),
                              image=foodImages[index],       # adds image to radio button
                              compound='left',               # adds image and text (left side)
                              indicatoron=0,                 # eliminate circle indicators
                              width=200,                     # sets width of radio buttons
                              command=order                 # set command of radiobutton to function
                              )
    radiobutton.grid(row=index+6, column=1, sticky=W)

scale_photo = PhotoImage(file='exclamation_point.gif')
scale_label = Label(window, image=scale_photo, bg='cyan')
scale_label.grid(row=9, column=0, sticky=E)
scale = Scale(window,
              from_=0,
              to=100,
              length=400,
              orient=HORIZONTAL,
              font=('FreeMono', 11, 'bold'),
              tickinterval=10,          # displays numbers along scale
              showvalue=0,            # hide current value
              resolution=5,              # create steps
              troughcolor='#00FF00',
              fg='#FF4800',
              bg='#111111',)
scale.set(((scale['from']-scale['to'])/2) + scale['to'])               # starting value in middle
scale.grid(row=9, column=1, pady=10)
scale_button = Button(window, text='read scale', command=scale_submit)
scale_button.grid(row=9, column=2)


listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 15),
                  width=12,
                  selectmode=MULTIPLE,
                  )
listbox.grid(row=10, column=1, sticky=E)

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.insert(0, "new list item")
entryBox.grid(row=11, column=1, sticky=E)

orderFromListButton = Button(window, text="order from list", command=list_select)
orderFromListButton.grid(row=10, column=2)

addToListButton = Button(window, text="add to list", command=add_to_list)
addToListButton.grid(row=11, column=2, sticky=W)

deleteFromListButton = Button(window, text="delete from list", command=delete_from_list)
deleteFromListButton.grid(row=10, column=3)


messagebox_button = Button(window,
                           command=messagebox_click,
                           text='click here for messagebox',
                           font=('Georgia', 20),
                           fg='#00ff00',
                           bg='black')
messagebox_button.grid(row=12, column=1, sticky=W)

text_area = Text(window,
                 bg='light yellow',
                 font=('FreeSerif', 15),
                 height=8,
                 width=30,
                 padx=20,
                 pady=20,
                 fg='purple',
                 )
text_area.grid(row=13, column=1, rowspan=2)

# frame = a rectangular container to group and hold widgets
frame = Frame(window, bg="pink", bd=5, relief=SUNKEN)
frame.grid(row=13, column=2, columnspan=2, sticky=W)

text_get_button = Button(frame, text="get text", command=get_text)
text_get_button.grid(row=0, column=1)

file_save_button = Button(frame,
                           command=saveFile,
                           text='save to file',
                           font=('Lato', 20),
                           fg='#00ff00',
                           bg='black')
file_save_button.grid(row=1, column=1, pady=20, sticky=E)

file_open_button = Button(frame,
                           command=openFile,
                           text='open a file',
                           font=('Lato', 20),
                           fg='#00ff00',
                           bg='black')
file_open_button.grid(row=2, column=1, sticky=W)


# menu bar
openImage = PhotoImage(file="icons8-opened-folder-48.png")
saveImage = PhotoImage(file="icons8-save-48.png")
exitImage = PhotoImage(file="icons8-close-window-48.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("Georgia", 13))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile, image=openImage, compound='left')
fileMenu.add_command(label="Save", command=saveFile, image=saveImage, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit, image=exitImage, compound='left')

editMenu = Menu(menubar, tearoff=0, font=("Georgia", 13))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)



# create another label
end_label = Label(window, text="\nThat's All Folks!", bg="white", fg="blue", font="none 12 bold")
end_label.grid(row=30, column=0, columnspan=5, sticky=S, pady=30)

# run main loop
window.mainloop()
