# Glossary Project

from tkinter import *
# from PIL import ImageTk, Image

# key down function
def click(event = None):
    # entered_text = textentry.get()  # this will collect the text from the text entry box
    output.delete(0.0, END)
    output.insert(END, penny.get_subtotal(textentry.get()))

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


'''
# exit function
def close_window():
    window.destroy()
    exit()
'''

# create coin class
class Coin:
    def __init__(self, name, value):
        self.name = name
        self.value = float(value)
        self.qty = 0
        self.stackval = 0.00

    def get_subtotal(self, qty_str):
        """ get quantity of each coin and calculate total value """
        self.qty = int(qty_str or 0)    # default input value set to 0
        self.stackval = self.value * self.qty
        return f"Total of {self.name}: {self.value} x {self.qty} = ${'{:,.2f}'.format(self.stackval)}"


# instantiate coins here
penny = Coin("pennies", 0.01)

##### main:
window = Tk()
window.title("Here is my Project")
window.config(background="cyan")

icon = PhotoImage(file='m3-blue-icon.png')
window.iconphoto(True, icon)

# exit button
quit_button = Button(window, text="Exit Program", width=10, command=window.quit)
quit_button.grid(row=0, column=0, sticky=N)

##### My Photo
my_logo = PhotoImage(file="ConsultLogo2.png")
logo_label = Label(window, image=my_logo, bg='yellow')
logo_label.grid(row=0, column=1, columnspan=3)


add_img = PhotoImage(file='M3 Logo.png')

# create label
first_label = Label(window,
                    text="Enter something",
                    font="none 12 bold",
                    fg="blue",
                    bg="yellow",
                    relief=RAISED,
                    bd=5,
                    padx=20,
                    pady=10,
                    image=add_img,
                    compound='right')
first_label.grid(row=1, column=1, pady=2)

# create text box
textentry = Entry(window, width=10, bg="yellow")
textentry.grid(row=2, column=0, sticky=E)
textentry.focus()

# create a text box
output = Text(window, width=50, height=4, wrap=WORD, background="yellow")
output.grid(row=2, column=1)

bn_enter_icon = PhotoImage(file='bn_enter_down.gif')

# create submit button
button = Button(window,
                text="Click Me!",
                command=click,
                font=("Comic Sans", 20),
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
              font=("Comic Sans", 25),
              fg="#00FF00",
              bg="black")
#entry.insert(0, "default text")
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
                           font=('Comic Sans', 20),
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

scale = Scale(window,
              from_=0,
              to=100,
              length=400,
              orient=HORIZONTAL,
              font=('Consolas', 11),
              tickinterval=10,          # displays numbers along scale
              showvalue=0,            # hide current value
              resolution=5,              # create steps
              troughcolor='#00FF00',
              fg='#FF4800',
              bg='#111111',)
scale.set(((scale['from']-scale['to'])/2) + scale['to'])               # starting value in middle
scale.grid(row=9, column=1, pady=10)
scale_button = Button(window, text='submit', command=scale_submit)
scale_button.grid(row=9, column=2)


listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 15),
                  width=12,
                  selectmode=MULTIPLE,
                  )
listbox.grid(row=10, column=1)

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.grid(row=11, column=1)

submitButton = Button(window, text="submit", command=list_select)
submitButton.grid(row=10, column=2)

addButton = Button(window, text="add", command=add_to_list)
addButton.grid(row=11, column=2)

deleteButton = Button(window, text="delete", command=delete_from_list)
deleteButton.grid(row=11, column=3)


# create another label
end_label = Label(window, text="\nThat's All Folks!", bg="white", fg="blue", font="none 12 bold")
end_label.grid(row=30, column=0, columnspan=5, sticky=S, pady=30)

##### run main loop
window.mainloop()
