# import all necessary packages and libraries
from tkinter import *                         
from tkinter import messagebox
from cryptography.fernet import Fernet as fn

# importing the functions in other files created manually
from Encryption import *
from Decryption import *

def start():
    ''' Function is for creating the base window.'''
    root = Tk()        #Creating base window
    root.title("Secure Your Data Here")

    Label(root, text = "Select a option here:").place(x = 40, y = 40)
    Var1 = IntVar()

    Rbtn1 = Radiobutton(root, text = "Encrypt", variable = Var1, value = 1)
    Rbtn1.place(x = 40, y = 65)

    Rbtn2 = Radiobutton(root, text = "Decrypt", variable = Var1, value = 2)
    Rbtn2.place(x = 40, y = 90)

    #passing the selected value from radio button
    btn = Button(root, text = "OKAY", command = lambda: Next(Var1.get()))
    btn.place(x = 40, y = 110)

    def Next(choice):
        '''This function is for next button or okay button on the base window
            that is root.'''

        if choice == 1:  #comparing the values returnes from radio button on base window
            root.destroy()    #destroying the base window

            #generating new window on the basis of the choice
            root2 = Tk()
            root2.title("Encryption")

            def back():
                '''This function is for back button on secondary window
                for going back to base window. It contains a destroy
                function and a callback to previous window that is start
                function.'''
                
                root2.destroy()
                start()
                
            def enc():
                '''This function passes the message entered for
                    encryption to the encrypt function.'''
                
                encrypt(e1.get())
                e1.delete(0, END)
                messagebox.showinfo("Done", "Encryption Successfull.")
            
            Label(root2, text = "Enter your Message here:").place(x = 40, y = 40)
            e1 = Entry(root2)
            
            e1.place(x = 40, y = 65)

            btn1 = Button(root2, text = "Encrypt", command = enc)
            btn1.place(x = 40, y = 90)

            btn2 = Button(root2, text = "Back", command = back)
            btn2.place(x = 40, y = 115)
            
            root2.mainloop()

        elif choice == 2:
            # this is for another choice of user  i.e. decryption
            root.destroy()
            root2 = Tk()
            root2.title("Decryption")
            decrypt_obj = Decryption()
            
            msg = decrypt_obj.decrypt() # passing the message to the decrypt function.

            def back():
                root2.destroy()
                start()

            # Asking how the user wants to convey there message
            Msgbox = messagebox.askyesno("Success", "Decryptiion Success.\n" + "Do you want to see message here.")

            if Msgbox == True:
                # Displaying message to the user on the new fresh window.
                Label(root2, text = "'" + str(msg) + "'").place(x = 30, y = 80)

            else:
                # Creating the new file where the decrypted message will be stored
                file_name = 'Decr_msg.txt'
                with open(file_name, "wb") as decr_msg:
                    decr_msg.write(bytes(msg, 'UTF-8'))
                    
                Label(root2, text = "Message saved in "+ file_name).place(x = 20, y = 80)

            btn2 = Button(root2, text = "Back", command = back)
            btn2.place(x = 40, y = 115)

            root2.mainloop()
                  
        #else:
            # showing error if user tries to go next without any choice
            #messagebox.showerror("Invalid", "Invalid Choice!")

    root.mainloop()

start()

