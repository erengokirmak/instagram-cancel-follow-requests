from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import CancelFunctionality

root = Tk()
root.title("Instagram Pending Follow Request Canceller")
root.grid_propagate(1)


requestsFileSelection = None

def onFileSelect():
    global requestsFileSelection
    requestsFileSelection = fd.askopenfile()

def onSubmit():
    if usernameField.get() != "" and passwordField != "" and requestsFileSelection != None:
        print(requestsFileSelection)
        CancelFunctionality.cancel(username=usernameField.get(), password=passwordField.get(), path_to_html_file=requestsFileSelection.name)
    else:
        messagebox.showerror("Insufficient Information", "The program requires your username, password, and your pending requests file to work")
        

usernameLabel = Label(root, text="Username: ")
usernameField = Entry(root, width=40)
usernameField.focus_set()

passwordLabel = Label(root, text="Password: ")
passwordField = Entry(root, width=40)


usernameLabel.grid(row=0, column=0, padx=10, pady=5)
usernameField.grid(row=0, column=1, padx=10)
passwordLabel.grid(row=1, column=0, padx=10)
passwordField.grid(row=1, column=1, padx=10)

fileSelectionButton = Button(text="Pending Requests File", command=onFileSelect)
fileSelectionButton.grid(row=2, columnspan=2, pady=5)
submitButton = Button(text="Get Rid Of Pending Requests!", command=onSubmit)
submitButton.grid(row=3,columnspan=2, pady=2)

root.mainloop()