from tkinter import *
import os
from PIL import ImageTk, Image


root = Tk()

def callback(): 
    filename = 'interfacecpy.py'
    os.system(filename) 
  

  


if __name__ == "__main__" :
 root.title("Morse Code Convertor")    

 background_image = ImageTk.PhotoImage(Image.open("E:\\python project\\background.jpg"))
 background_label = Label(root, image=background_image)
 background_label.place(x=0, y=0, relwidth=1, relheight=1)

 headlabel1 = Label(root, text = 'MORSE CODE CONVERTOR',wraplength=300,
							 fg = "black") 
 headlabel1.configure(font=("Times New Roman", 25, "bold"))                           
 headlabel1.place(relx=0.5, rely=0.25, anchor=CENTER)
	
 
 root.geometry("400x400") 
 button1 = Button(root, text = "Let's Get In", bg = "brown", fg = "white", command = callback) 
 button1.place(relx=0.5, rely=0.5, anchor=CENTER)
 button1.configure(font=("Piazzolla", 15, "bold"))                           
 

 root.mainloop()