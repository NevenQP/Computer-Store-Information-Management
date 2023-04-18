from tkinter import *
from tkinter import messagebox
import json
from mana import *

# #880808: blue, #D64045: light blue, #F6AE2D: yellow, ##FFFFFA: trắng, #141204: đen
# #880808: blood red, #D64045: red
class add_staff:
    def __init__(self, root, id):
        self.id = id
        self.staffs = []
        with open("staff.txt", "r") as f:
            staffs = json.loads(f.read())   
        for staff in staffs:
            self.staffs.append(staff)
        

        Exist = FALSE
        for i in range(len(self.staffs)):
            if self.staffs[i][0] == self.id:
                Exist = TRUE
                break
        
        if Exist is FALSE:
            self.window = root
            self.window.title("New staff")
            self.window.geometry("720x300")
            self.window.configure(bg = "#FFFFFA")
            self.window.resizable(False, False)

            self.add_staff_tittle = Label(self.window, text = "New staff? Enter information", fg = '#880808', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 0, column = 0)
            self.add_staff_name = Label(self.window, text = "Name", fg = '#880808', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 1, column = 0)
            self.add_staff_name_e = Entry(self.window, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
            self.add_staff_name_e.grid(row = 1, column = 1)
            self.add_staff_dob = Label(self.window, text = "Dob", fg = '#880808', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 2, column = 0)
            self.add_staff_dob_e = Entry(self.window, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
            self.add_staff_dob_e.grid(row = 2, column = 1)
            self.add_staff_contact_number = Label(self.window, text = "Contact Number", fg = '#880808', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 3, column = 0)
            self.add_staff_contact_number_e = Entry(self.window, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
            self.add_staff_contact_number_e.grid(row = 3, column = 1)
            self.add_staff_email = Label(self.window, text = "Email", fg = '#880808', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 4, column = 0)
            self.add_staff_email_e = Entry(self.window, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
            self.add_staff_email_e.grid(row = 4, column = 1)
            self.add_staff_position = Label(self.window, text = "Position", fg = '#880808', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 5, column = 0)
            self.add_staff_position_e = Entry(self.window, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
            self.add_staff_position_e.grid(row = 5, column = 1)

            self.submit = Button(self.window, text = "Submit", fg = '#FFFFFA', bg = '#D64045', font=('Montserrat Bold',16), command = self.add_staff_data).place(x = 310, y = 225) 
        else:
            root.destroy()
            root = Tk()
            obj = Management(root, self.id)
            root.mainloop()

    def add_staff_data(self):
        name = self.add_staff_name_e.get()
        dob = self.add_staff_dob_e.get()
        contact_number = self.add_staff_contact_number_e.get()
        email = self.add_staff_email_e.get()
        position = self.add_staff_position_e.get()

        if  name == '' or position == '' or dob == '' or contact_number == '' or email == '':
            mes = Label(self.window, text = "Invalid", fg = '#880808', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.grid(row = 6, column = 1)
            mes.after(3000,lambda:mes.destroy())
        else:
            self.staffs.append([self.id, name, dob, contact_number, email, position])
            messagebox.showwarning("showinfo", "Success")
            
            with open("staff.txt", "w") as f:
                f.truncate(0)
                f.write(json.dumps(self.staffs))
            
            self.window.destroy()
            root = Tk()
            obj = Management(root, self.id)
            root.mainloop()
    
if __name__ == "__main__":
    root = Tk()
    obj = add_staff(root, '1')
    root.mainloop()