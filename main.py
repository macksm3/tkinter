# Glossary Project

# import coin module for proof of concept testing
from coin import Coin

from tkinter import *
from tkinter import messagebox  # import messagebox library
from tkinter import colorchooser  # submodule
from tkinter import filedialog
from tkinter import ttk
# from PIL import ImageTk, Image


# key down function from original test code
def click(event):
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


def create_window():
    new_window = Toplevel()     #Toplevel() = new window on top of other windows, linked to a 'bottom' window
    # new_window = Tk()      #Tk() = new independent window
    # old_window.destroy()   # close out of old_window


def doSomething(event):
    # print("You pressed: " + event.keysym)
    key_label.config(text=event.keysym)


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

entryFrame = Frame(window)
entryFrame.grid(row=3, column=1,columnspan=3)

entry = Entry(entryFrame,
              font=("Comic Sans MS", 18),
              fg="#00FF00",
              bg="black",
              )
entry.insert(0, "enter text")
#entry.config(show="*")  # replace every character with *
#entry.config(state=DISABLED)
entry.pack(side="left")

submit_button = Button(entryFrame, text="submit", command=submit)
submit_button.pack(side="right")

delete_button = Button(entryFrame, text="delete", command=delete)
delete_button.pack(side="right")

backspace_button = Button(entryFrame, text="backspace", command=backspace)
backspace_button.pack(side="right")


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


# radio buttons generated from list with for loop
pizzaImage = PhotoImage(file='Crestron swirl 40x40.png')
hamburgerImage = PhotoImage(file='CrestronBlue 40x40.png')
hotdogImage = PhotoImage(file='crestron icon.png')
foodImages = [pizzaImage, hamburgerImage, hotdogImage]
f = IntVar()

radioFrame = Frame(window, relief="raised", bd=5)
radioFrame.grid(row=6, column=1, sticky=E)

for index in range(len(food)):
    radiobutton = Radiobutton(radioFrame,
                              text=food[index],     # adds text to radio buttons
                              variable=f,       # groups radiobuttons together if they share the same variable
                              value=index,       # assigns each radiobuton a different value
                              padx=25,
                              font=("Impact", 20),
                              image=foodImages[index],       # adds image to radio button
                              compound='left',               # adds image and text (left side)
                              indicatoron=False,                 # eliminate circle indicators
                              width=200,                     # sets width of radio buttons
                              command=order                 # set command of radiobutton to function
                              )
    radiobutton.pack()


# scale = sliding numeric control
scale_frame = Frame(window, bg='white', bd=3, relief=RIDGE)
scale_frame.grid(row=9, column=1, columnspan=4, padx=20, pady=10)

scale_cold = PhotoImage(file='icons8-snowflake-48.png')
cold_label = Label(scale_frame, image=scale_cold, bg='cyan')
cold_label.grid(row=9, column=0, padx=20, sticky=E)

scale = Scale(scale_frame,
              from_=0,
              to=100,
              length=400,
              orient=HORIZONTAL,
              font=('FreeMono', 11, 'bold'),
              tickinterval=10,          # displays numbers along scale
              #showvalue=0,            # hide current value
              #resolution=5,              # create steps
              troughcolor='#00FF00',
              fg='#FF4800',
              bg='#111111',)
scale.set(((scale['from']-scale['to'])/2) + scale['to'])               # starting value in middle
scale.grid(row=9, column=1, pady=20)

scale_hot = PhotoImage(file='icons8-fire-48.png')
hot_label = Label(scale_frame, image=scale_hot, bg='cyan')
hot_label.grid(row=9, column=2, padx=20, sticky=W)

scale_button = Button(scale_frame, text='read scale', command=scale_submit)
scale_button.grid(row=9, column=3, padx=20)


listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 14),
                  width=14,
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
                 height=5,
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
file_save_button.grid(row=1, column=1, pady=5, sticky=E)

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

Button(window, text="create new window", command=create_window).grid(row=15, column=1, pady=20)

notebook = ttk.Notebook(window)   # widget that manages a collection of windows/displays

tab1 = Frame(notebook)      # new frame for tab 1
tab2 = Frame(notebook)      # new frame for tab 2
tab3 = Frame(notebook)      # new frame for tab 3

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.add(tab3, text="Tab 3")
notebook.grid(row=16, column=0, columnspan=2)
# notebook.pack(expand=True, fill="both")    # expand to fill any space not otherwise used
                                            # fill space on x and y axis

Label(tab1, text="Hello, this is tab#1", width=50, height=5).pack()
Label(tab2, text="Whatup', this is tab#2", width=50, height=5).pack()
Label(tab3, text="Goodbye, this is tab#3", width=50, height=5).pack()


# progress bar - import function breaks other things in this program
# offloading it to separate file


# canvas = widget that is used to draw graphs, plots, images in a window
canvas = Canvas(window, height=250, width=400)
# greenLine = canvas.create_line(0, 0, 400, 250, fill="green", width=5)
# redLine = canvas.create_line(0, 250, 400, 0, fill="red", width=5)
# canvas.create_rectangle(50, 50, 350, 200, fill="purple")
# canvas.create_polygon(200, 0, 350, 250, 50, 250, fill="yellow")
# points = [200, 0, 350, 100, 300, 250, 100, 250, 50, 100]
points = [250, 10, 390, 100, 330, 240, 170, 240, 90, 100]
canvas.create_polygon(points, fill="yellow", outline="black", width=3)
# canvas.create_arc(0, 0, 250, 250, fill="blue", style=PIESLICE, start=90, extent=180)
canvas.create_arc(10, 10, 240, 240, fill="red", extent=180, width=10)
canvas.create_arc(10, 10, 240, 240, fill="white", extent=180, start=180, width=10)
canvas.create_oval(80, 90, 170, 160, fill="white", width=10)
canvas.grid(row=16, column=2, columnspan=3, padx=5)


window.bind("<Key>", doSomething)
key_label = Label(window, font=("FreeSerif", 100))
key_label.grid(row=17, column=1)



# create another label
end_label = Label(window, text="\nThat's All Folks!", bg="white", fg="blue", font="none 12 bold")
end_label.grid(row=30, column=0, columnspan=5, sticky=S, pady=12)

# exit button from original test project
quit_button = Button(window, text="Exit Program", width=15, command=window.quit)
quit_button.grid(row=31, column=0, columnspan=5, sticky=S)

# run main loop
window.mainloop()
