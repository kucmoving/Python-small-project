import PIL
from PIL import Image
from tkinter import *
from tkinter.filedialog import *
#################################################################################################
window = Tk()
window.title("Resize and Compress Images")
window.minsize(width=40, height=120)
window.config(padx=0, pady=0, bg="grey")
#################################################################################################

file_list = None
#---------------------------------------------------function--------------------------------------------#
def open_file():
    global file_list
    file_list = askopenfilenames(title="Please select files you want to resize and compress.")

def save_file():
    global file_list
    print(file_list)
    times = 0
    height = int(height_entry.get())
    width = int(width_entry.get())
    save_path = asksaveasfilename(title="Please enter where you want to save.")
    for _ in file_list:
        img = PIL.Image.open(file_list[times])
        img = img.resize((height, width), PIL.Image.ANTIALIAS)
        img.save(save_path + f"{times}.JPG")
        times = times + 1                                                 ####times is used to locate the no. of file
        print("yes")
    system_label.config(text="Finished! Please Check!^^", bg="grey", fg="yellow")

#----------------------------------------------------UI---------------------------------------------------#
height_label = Label(text="Height:", bg="grey", fg="yellow")
height_label.place(x=15, y=50)

height_entry = Entry(textvariable=4, highlightthickness=0)
height_entry.insert(0,"600")
height_entry.place(x=80, y=50,width=50)

width_label = Label(text="Width", bg="grey", fg="yellow")
width_label.place(x=15, y=90)

width_entry = Entry(textvariable=5,highlightthickness=0)      #-------textvariable cannot be the same, otherwise doesn't work well
width_entry.insert(0,"800")
width_entry.place(x=80, y=90,width=50)

open_but = Button(text="Open File", highlightthickness=0, width=20, command=open_file)
open_but.place(x=15, y=20)
save_but = Button(text="Convert and Save File", highlightthickness=0, width=20, command=save_file)
save_but.place(x=15, y=120)

system_label = Label(text="System: Waiting for your input^^", bg="grey", fg="yellow")
system_label.place(x=15,y=150)

window.mainloop()

