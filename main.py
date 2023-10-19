from tkinter import *

#Creating a window & configuring
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


#Labels
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text="new text 2")


#Button
def button_clicked():
    print("I got clicked")
    new_text = input.get() #get texts from entry box
    my_label.config(text=new_text)

#Calls function when pressed
button = Button(text="Click me", command=button_clicked)
button.pack()


#Entries
input = Entry(width=30)
#Adding some text to begin with
input.insert(END, string="Some text to begin with.")
#Gets text in entry
input.get()
input.pack()


#Text
text = Text(height=5, width=30)
text.focus() #Puts cursor in texbox
#Add some text to begin with
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


#Spinbox
def spinbox_used():
    #Gets the current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


#Checkbutton
def checkbutton_used():
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


#RadioButton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#ListBox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana", "Strawberry"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()























window.mainloop()