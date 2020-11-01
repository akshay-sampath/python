
from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk, Image

import mysql.connector



def Show():  
 mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="Chandu 2000",
 database="morse"
 )

 mycursor = mydb.cursor()

 query = """SELECT * FROM result"""	
 result = mycursor.execute(query)
 result1 = mycursor.fetchall()
 print(result1)
 
 i=0
 for x in result1:
    list1.insert(i, x)
    i=i+1
 messagebox.showinfo(message="Display is successful")

 mydb.close()


root = Tk() 
 
variable1 = StringVar(root) 
variable2 = StringVar(root) 

variable1.set("FROM") 
variable2.set("TO") 
	
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
					'C':'-.-.', 'D':'-..', 'E':'.', 
					'F':'..-.', 'G':'--.', 'H':'....', 
					'I':'..', 'J':'.---', 'K':'-.-', 
					'L':'.-..', 'M':'--', 'N':'-.', 
					'O':'---', 'P':'.--.', 'Q':'--.-', 
					'R':'.-.', 'S':'...', 'T':'-', 
					'U':'..-', 'V':'...-', 'W':'.--', 
					'X':'-..-', 'Y':'-.--', 'Z':'--..', 
					'a':'.-', 'b':'-...', 
					'c':'-.-.', 'd':'-..', 'e':'.', 
					'f':'..-.', 'g':'--.', 'h':'....', 
					'i':'..', 'j':'.---', 'k':'-.-', 
					'l':'.-..', 'm':'--', 'n':'-.', 
					'o':'---', 'p':'.--.', 'q':'--.-', 
					'r':'.-.', 's':'...', 't':'-', 
					'u':'..-', 'v':'...-', 'w':'.--', 
					'x':'-..-', 'y':'-.--', 'z':'--..', 
					'1':'.----', '2':'..---', '3':'...--', 
					'4':'....-', '5':'.....', '6':'-....', 
					'7':'--...', '8':'---..', '9':'----.', 
					'0':'-----', ', ':'--..--', '.':'.-.-.-', 
					'?':'..--..', '/':'-..-.', '-':'-....-', 
					'(':'-.--.', ')':'-.--.-'} 

 
def clearAll() : 
	language1_field.delete(1.0, END) 
	language2_field.delete(1.0, END) 


def convert() : 

 message = language1_field.get("1.0", "end")[:-1] 
 if variable1.get() == variable2.get() : 
  messagebox.showerror("Can't Be same Language") 
  return

 elif variable1.get() == "Eng" and variable2.get() == "Morse" : 
  rslt = encrypt(message) 

 elif variable1.get() == "Morse" and variable2.get() == "Eng" : 
  rslt = decrypt(message) 

 else : 
  messagebox.showerror("please choose valid language code..") 
  return
	
 language2_field.insert('end -1 chars', rslt) 
 mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Chandu 2000",
  database="morse"
	)

 mycursor = mydb.cursor()

 d1 =  language1_field.get("1.0", "end")[:-1] 
 d2 =  language2_field.get("1.0", "end")[:-1] 
 query = """INSERT INTO result VALUES (%s,%s)"""
 data = (d1, d2)
 result=mycursor.execute(query, data)
 mydb.commit()
 messagebox.showinfo(message="Data is successfully inserted")


def encrypt(message): 
	cipher = '' 
	for letter in message: 
		if letter != ' ': 
			cipher += MORSE_CODE_DICT[letter] + ' '
		else: 
			cipher += ' '
	
	return cipher 
	
def decrypt(message): 

	message += ' '
	
	decipher = '' 
	citext = '' 
	for letter in message: 
	 
		if (letter != ' '): 
			i = 0
			citext += letter 
	

		else: 
			
			i += 1
	
		
			if i == 2 : 
	
			
				decipher += ' '
			else: 
				decipher += list(MORSE_CODE_DICT.keys())[ 
							list(MORSE_CODE_DICT .values()).index(citext)] 
				citext = '' 
	
	return decipher 



if __name__ == "__main__" : 
 root.geometry("700x700") 
 root.title("Morse Code Translator") 
	
 background_image = ImageTk.PhotoImage(Image.open("E:\\python project\\interface1.jpg"))
 background_label = Label(root, image=background_image)
 background_label.place(x=0, y=0, relwidth=1, relheight=1)

 headlabel = Label(root, text = 'WELCOME TO MORSE CODE CONVERTOR', 
							fg = 'white',bg="black" ) 
 headlabel.configure(font=("TIMES NEW ROMAN", 25))                           
						
	
 label1 = Label(root, text = "YOUR MESSAGE ", 
				fg = 'black', bg = 'orange') 
 label1.configure(font=("TIMES NEW ROMAN", 10))                           

	
 label4 = Label(root, text = "MESSAGE CONVERTED ", 
				fg = 'black', bg = 'orange') 
 label4.configure(font=("TIMES NEW ROMAN", 10))                           
	

 headlabel.place(relx=0.5, rely=0.025, anchor=CENTER)
 label1.place(relx=0.1, rely=0.2, anchor="w")
 label4.place(relx=0.1, rely=0.5, anchor="w")
	
 language1_field = Text(root, height = 5, width = 25, 
									font = "TIMESNEWROMAN 13",highlightbackground="orange",highlightthickness=2) 									
 language2_field = Text(root, height = 5, width = 25, 
									font = "lucida 13", highlightbackground="green",highlightthickness=2) 
		
 language1_field.place(relx=0.5, rely=0.2, anchor=CENTER) 
 language2_field.place(relx=0.5, rely=0.5, anchor=CENTER)
	
 languageCode_list = ["Eng", "Morse"] 
	

 FromLanguage_option = OptionMenu(root, variable1, *languageCode_list) 
 ToLanguage_option = OptionMenu(root, variable2, *languageCode_list) 
		
 FromLanguage_option.place(relx=0.5, rely=0.3, anchor=CENTER)
 ToLanguage_option.place(relx=0.5, rely=0.35, anchor=CENTER)
		
	
 button1 = Button(root, text = "Convert", bg = "#ffc800", fg = "black", 
								command = convert) 
		
 button1.place(relx=0.5, rely=0.4, anchor=CENTER)

 button2 = Button(root, text = "Clear the input fields", bg = "red", 
					fg = "white", command = clearAll) 
	
 button2.place(relx=0.4, rely=0.6, anchor=CENTER) 
 
 button3 = Button( root,text="SHOW",bg="#ff9900",fg="black",command = Show)
 button3.place(relx=0.5, rely=0.65, anchor=CENTER) 

 list1 = Listbox(root, width=100,height=15,fg = 'black')
 list1.place(relx=0.5,rely=0.85,anchor=CENTER)


 
 root.mainloop() 
    
