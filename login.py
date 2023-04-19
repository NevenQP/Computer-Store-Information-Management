from tkinter import *
from tkinter import messagebox
import json
import sign_up as su
import add_new_staff as ans

# #880808: blue, #D64045: light blue, #F6AE2D: yellow, #FFFFFA: trắng, #141204: 
# #880808: blood red, #D64045: red
class Login:
   def __init__(self, root):      
      f = open("account.txt", "a")
      f.close()
      self.login = root
      self.login.title('Login')
      self.login.configure(bg = "#FFFFFA")
      self.login.geometry("800x720")
      self.login.resizable(False,False)
      self.Sign_in = Label(self.login, text = "Log in", fg = '#880808', bg = '#FFFFFA', highlightthickness = 0, font=('Montserrat Bold',30)).place(x = 340 , y = 100)
      self.User = Label(self.login, text = "User", fg = '#ffb601', bg = '#FFFFFA', font=('Montserrat',20, 'bold')).place(x = 100 , y = 200)
      self.User_box = Entry(self.login, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',20), textvariable = StringVar())
      self.User_box.place(x = 350 , y = 200)
      self.Password = Label(self.login, text = "Password", fg = '#ffb601', bg = '#FFFFFA', font=('Montserrat',20, 'bold')).place(x = 100 , y = 300)
      self.Password_box = Entry(self.login, show="*", fg = '#141204', bg = '#FFFFFA', font=('Montserrat',20), textvariable = StringVar())
      self.Password_box.place(x = 350 , y = 300)
      self.Login_button = Button(self.login, text = "Log in", fg = '#FFFFFA', bg = '#880808', font=('Montserrat Bold',20), command = self.do_log_in).place(x = 340 , y = 400)
      self.Sign_up = Label(self.login, text = "Dont have an account ?", fg = '#F6AE2D', bg = '#FFFFFA', font=('Montserrat',15)).place(x = 200 , y = 505)
      self.Sign_up_button = Button(self.login, text = "Sign up", fg = '#FFFFFA', bg = '#D64045', font=('Montserrat Bold',15), command= self.open_sign_up).place(x = 495 , y = 500)

   def do_log_in(self):
      user = self.User_box.get()
      password = self.Password_box.get()
      try: 
         with open("account.txt", 'r') as f:
            account = json.loads(f.read())
      except:
         messagebox.showwarning("showinfo", "Invalide user")
         return
      
      if user not in account:
         messagebox.showwarning("showinfo", "Invalide user")
      elif account[user] == password:
         self.login.destroy()
         root = Tk()
         obj = ans.add_staff(root, user)
         root.mainloop()
      else:
         messagebox.showwarning("showinfo", "Wrong pass")
   
   def open_sign_up(self):
      self.login.destroy()
      sign_up = Tk()
      su.Sign_up(sign_up)
      sign_up.mainloop()   
   
