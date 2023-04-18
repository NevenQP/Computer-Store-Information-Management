from tkinter import *
from tkinter import messagebox
import json
from datetime import datetime
# #880808: blue, #D64045: light blue, #880808: yellow, #FFFFFA: trắng, #141204: đen
# #880808: blood red, #D64045: red
class Management: 
    def __init__(self, root, id):
        self.staff_id = id
        self.staffs = []
        self.customers = []
        self.products = []
        self.bills = []
        self.load_data()
        self.window = root
        self.window.title("Computer Store Information Management")
        self.window.geometry("1280x720")
        self.window.configure(bg="#FFFFFA")
        self.window.resizable(False, False)

        self.title = Label(self.window, text = "Computer Store Information Management", fg = '#FFFFFA', bg = '#880808',pady = 30, font=('Montserrat Bold',23)).pack(fill = X)
        
        #button
        self.btn_frame = Frame(self.window, bg = '#FFFFFA')
        self.btn_frame.pack(fill = X)
        self.staff_btn = Button(self.btn_frame, text = "Staff", fg = '#FFFFFA', bg = '#880808', width = 10, font=('Montserrat Bold',15), command = self.display_staff).grid(row=0, column=0, padx = 75, pady = 10)
        self.product_btn = Button(self.btn_frame, text = "Product", fg = '#FFFFFA', bg = '#880808', width = 10, font=('Montserrat Bold',15), command = self.display_product).grid(row=0, column=1, padx=95, pady = 10)
        self.customer_btn = Button(self.btn_frame, text = "Customer", fg = '#FFFFFA', bg = '#880808', width = 10, font=('Montserrat Bold',15), command = self.display_customer).grid(row=0, column=2, padx=95, pady = 10)
        self.bill_btn = Button(self.btn_frame, text = "Bill", fg = '#FFFFFA', bg = '#880808', width = 10, font=('Montserrat Bold',15), command = self.display_bill).grid(row=0, column=3, padx=95, pady = 10)

        self.staff_frame = Frame(self.window, bg = "#FFFFFA")
        self.customer_frame = Frame(self.window, bg = "#FFFFFA")
        self.product_frame = Frame(self.window, bg = "#FFFFFA")
        self.bill_frame = Frame(self.window, bg = "#FFFFFA")


        #staff frame
        #staff function button
        self.staff_func_frame = Frame(self.staff_frame, bg = '#FFFFFA')
        self.staff_func_frame.pack(side = LEFT, fill = Y)
        self.show_staff_btn = Button(self.staff_func_frame, text = "Show staff list", fg = "#FFFFFA", bg = '#D64045', width = 15, font=('Montserrat Bold',15), command = self.show_staff_list).pack(pady = 10)
        self.delete_staff_btn = Button(self.staff_func_frame, text = "Delete staff", fg = "#FFFFFA", bg = '#D64045', width = 15, font=('Montserrat Bold',15), command = self.delete_staff).pack(pady = 10)
        self.search_staff_btn = Button(self.staff_func_frame, text = "Search staff", fg = "#FFFFFA", bg = '#D64045', width = 15, font=('Montserrat Bold',15), command = self.search_staff).pack(pady = 10)

        self.staff_wrk_frame = Frame(self.staff_frame, bg = '#FFFFFA')
        self.staff_wrk_frame.pack(expand = TRUE, fill = BOTH)

        #customer frame
        self.customer_func_frame = Frame(self.customer_frame, bg = '#FFFFFA')
        self.customer_func_frame.pack(side = LEFT, fill = Y)
        self.show_customer_btn = Button(self.customer_func_frame, text = "Show customer list", fg = "#FFFFFA", bg = '#D64045', width = 15, font=('Montserrat Bold',15), command = self.show_customer_list).pack(pady = 10)
        self.add_customer_btn = Button(self.customer_func_frame, text = "Add customer", fg = "#FFFFFA", bg = '#D64045', width = 15, font=('Montserrat Bold',15), command = self.add_customer).pack(pady = 10)
        self.delete_customer_btn = Button(self.customer_func_frame, text = "Delete customer", fg = "#FFFFFA", bg = '#D64045', width = 15, font=('Montserrat Bold',15), command = self.delete_customer).pack(pady = 10)
        self.search_customer_btn = Button(self.customer_func_frame, text = "Search customer", fg = "#FFFFFA", bg = '#D64045', width = 15, font=('Montserrat Bold',15), command = self.search_customer).pack(pady = 10)

        self.customer_wrk_frame = Frame(self.customer_frame, bg = '#FFFFFA')
        self.customer_wrk_frame.pack(expand = TRUE, fill = BOTH)

        #product frame
        self.product_func_frame = Frame(self.product_frame, bg = '#FFFFFA')
        self.product_func_frame.pack(side = LEFT, fill = Y)
        self.show_product_btn = Button(self.product_func_frame, text = "Show product list", fg = "#FFFFFA", bg = '#D64045', width = 15, font=('Montserrat Bold',15), command = self.show_product_list).pack(pady = 10)
        self.add_product_btn = Button(self.product_func_frame, text = "Add product", fg = "#FFFFFA", bg = '#D64045', width = 15, font=('Montserrat Bold',15), command = self.add_product).pack(pady = 10)
        self.delete_product_btn = Button(self.product_func_frame, text = "Delete product", fg = "#FFFFFA", bg = '#D64045', width = 15, font=('Montserrat Bold',15), command = self.delete_product).pack(pady = 10)
        self.search_product_btn = Button(self.product_func_frame, text = "Search product", fg = "#FFFFFA", bg = '#D64045', width = 15, font=('Montserrat Bold',15), command = self.search_product).pack(pady = 10)

        self.product_wrk_frame = Frame(self.product_frame, bg = '#FFFFFA')
        self.product_wrk_frame.pack(expand = TRUE, fill = BOTH)

        #bill frame
        self.bill_func_frame = Frame(self.bill_frame, bg = '#FFFFFA')
        self.bill_func_frame.pack(side = LEFT, fill = Y)
        self.show_bill_btn = Button(self.bill_func_frame, text = "Show bill list", fg = "#FFFFFA", bg = '#D64045', width = 15, font=('Montserrat Bold',15), command = self.show_bill_list).pack(pady = 10)
        self.add_bill_btn = Button(self.bill_func_frame, text = "Add bill", fg = "#FFFFFA", bg = '#D64045', width = 15, font=('Montserrat Bold',15), command = self.add_bill).pack(pady = 10)
        self.delete_bill_btn = Button(self.bill_func_frame, text = "Delete bill", fg = "#FFFFFA", bg = '#D64045', width = 15, font=('Montserrat Bold',15), command = self.delete_bill).pack(pady = 10)
        self.search_bill_btn = Button(self.bill_func_frame, text = "Search bill", fg = "#FFFFFA", bg = '#D64045', width = 15, font=('Montserrat Bold',15), command = self.search_bill).pack(pady = 10)

        self.bill_wrk_frame = Frame(self.bill_frame, bg = '#FFFFFA')
        self.bill_wrk_frame.pack(expand = TRUE, fill = BOTH)

        self.window.protocol("WM_DELETE_WINDOW", self.save_data)
    def save_data(self):
        with open("staff.txt", "w") as f:
            f.truncate(0)
            f.write(json.dumps(self.staffs))
        with open("product.txt", "w") as f:
            f.truncate(0)
            f.write(json.dumps(self.products))
        with open("customer.txt", "w") as f:
            f.truncate(0)
            f.write(json.dumps(self.customers))
        with open("bill.txt", "w") as f:
            f.truncate(0)
            f.write(json.dumps(self.bills))
        self.window.destroy()

    def load_data(self):
        with open("staff.txt", "r") as f:
            staffs = json.loads(f.read())   
        for staff in staffs:
            self.staffs.append(staff)
    
        with open("product.txt", "r") as f:
            products = json.loads(f.read())   
        for product in products:
            self.products.append(product)
        
        with open("customer.txt", "r") as f:
            customers = json.loads(f.read())   
        for customer in customers:
            self.customers.append(customer)

        with open("bill.txt", "r") as f:
            bills = json.loads(f.read())   
        for bill in bills:
            self.bills.append(bill)

    def clear_frame(self):
        for widgets in self.staff_wrk_frame.winfo_children():
            widgets.destroy()
        
        for widgets in self.customer_wrk_frame.winfo_children():
            widgets.destroy()
        
        for widgets in self.product_wrk_frame.winfo_children():
            widgets.destroy()
        
        for widgets in self.bill_wrk_frame.winfo_children():
            widgets.destroy()

    #staff function
    def display_staff(self):
        self.clear_frame()
        self.customer_frame.forget()
        self.product_frame.forget()
        self.bill_frame.forget()
        
        
        self.staff_frame.pack(expand = TRUE, fill = BOTH)

    def show_staff_list(self):
        self.clear_frame()
        
        for i in range(len(self.staffs)):
            for j in range(len(self.staffs[0])):
                self.e = Label(self.staff_wrk_frame,bd = 5, width = 12, bg = '#FFFFFA', text = self.staffs[i][j], fg='#141204',font=('Montserrat Bold',14))
                self.e.grid(row=i, column=j)
    
    def delete_staff(self):
        self.clear_frame()

        self.add_staff_id = Label(self.staff_wrk_frame, text = "Delete staff", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 0, column = 0)
        self.add_staff_id = Label(self.staff_wrk_frame, text = "ID", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 1, column = 0)
        self.add_staff_id_e = Entry(self.staff_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_staff_id_e.grid(row = 1, column = 1)
        self.submit = Button(self.staff_wrk_frame, text = "Submit", fg = '#FFFFFA', bg = '#D64045', font=('Montserrat Bold',16), command = self.delete_staff_data).place(x = 140, y = 350)

    def search_staff(self):
        self.clear_frame()

        self.add_staff_id = Label(self.staff_wrk_frame, text = "Search staff", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 0, column = 0)
        self.add_staff_id = Label(self.staff_wrk_frame, text = "ID", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 1, column = 0)
        self.add_staff_id_e = Entry(self.staff_wrk_frame,width = 12 ,fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_staff_id_e.grid(row = 1, column = 1)
        self.submit = Button(self.staff_wrk_frame, text = "Submit", fg = '#FFFFFA', bg = '#D64045', font=('Montserrat Bold',16), command = self.search_staff_data).place(x = 140, y = 350)
    
    def delete_staff_data(self):
        id = self.add_staff_id_e.get()
        if id == "ID":
            mes = Label(self.staff_wrk_frame, text = "Id dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.place(x = 500, y = 33)
            mes.after(3000,lambda:mes.destroy())
            return
        
        for i in range(len(self.staffs)):
            if self.staffs[i][0] == id:
                self.staffs.pop(i)
                mes = Label(self.staff_wrk_frame, text = "Success", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
                mes.place(x = 450, y = 33)
                mes.after(3000,lambda:mes.destroy())
                return
        mes = Label(self.staff_wrk_frame, text = "Id dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
        mes.place(x = 450, y = 33)
        mes.after(3000,lambda:mes.destroy())

    def search_staff_data(self):
        id = self.add_staff_id_e.get()
        if id == "ID":
            mes = Label(self.staff_wrk_frame, text = "Id dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.place(x = 500, y = 33)
            mes.after(3000,lambda:mes.destroy())
            return
        
        for i in range(len(self.staffs)):
            if self.staffs[i][0] == id:
                for j in range(len(self.staffs[0])):
                    self.e = Label(self.staff_wrk_frame, bd = 5, width = 12, wraplength = 100, bg = '#FFFFFA',text = self.staffs[0][j], fg='#141204',font=('Montserrat Bold',16))
                    self.e.grid(row=2, column=j)
                    self.e = Label(self.staff_wrk_frame, bd = 5, width = 12, wraplength = 100, bg = '#FFFFFA',text = self.staffs[i][j], fg='#880808',font=('Montserrat Bold',16))
                    self.e.grid(row=3, column=j)
                return
        mes = Label(self.staff_wrk_frame, text = "Id dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
        mes.place(x = 500, y = 33)
        mes.after(3000,lambda:mes.destroy())

    
    #product function
    def display_product(self):
        self.clear_frame()
        self.staff_frame.forget()
        self.customer_frame.forget()
        self.bill_frame.forget()

        self.product_frame.pack(expand = TRUE, fill = BOTH)

    def show_product_list(self):
        self.clear_frame()
        
        for i in range(len(self.products)):
            for j in range(len(self.products[0])):
                self.e = Label(self.product_wrk_frame,bd = 5, width = 10, bg = '#FFFFFA' ,text = self.products[i][j], fg='#141204',font=('Montserrat Bold',16))
                self.e.grid(row=i, column=j)
    
    def add_product(self):
        self.clear_frame()

        self.add_product_tittle = Label(self.product_wrk_frame, text = "Add product", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 0, column = 0)
        self.add_product_id = Label(self.product_wrk_frame, text = "ID", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 1, column = 0)
        self.add_product_id_e = Entry(self.product_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_product_id_e.grid(row = 1, column = 1)
        self.add_product_name = Label(self.product_wrk_frame, text = "Name", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 2, column = 0)
        self.add_product_name_e = Entry(self.product_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_product_name_e.grid(row = 2, column = 1)
        self.add_product_cpu = Label(self.product_wrk_frame, text = "CPU", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 3, column = 0)
        self.add_product_cpu_e = Entry(self.product_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_product_cpu_e.grid(row = 3, column = 1)
        self.add_product_ram = Label(self.product_wrk_frame, text = "RAM", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 4, column = 0)
        self.add_product_ram_e = Entry(self.product_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_product_ram_e.grid(row = 4, column = 1)
        self.add_product_hard_disk = Label(self.product_wrk_frame, text = "Hard Disk", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 5, column = 0)
        self.add_product_hard_disk_e = Entry(self.product_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_product_hard_disk_e.grid(row = 5, column = 1)
        self.add_product_os = Label(self.product_wrk_frame, text = "OS", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 6, column = 0)
        self.add_product_os_e = Entry(self.product_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_product_os_e.grid(row = 6, column = 1)
        self.add_product_cost = Label(self.product_wrk_frame, text = "Cost", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 7, column = 0)
        self.add_product_cost_e = Entry(self.product_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_product_cost_e.grid(row = 7, column = 1)

        self.submit = Button(self.product_wrk_frame, text = "Submit", fg = '#FFFFFA', bg = '#D64045', font=('Montserrat Bold',16), command = self.add_product_data).place(x = 140, y = 350)

    def delete_product(self):
        self.clear_frame()

        self.add_product_id = Label(self.product_wrk_frame, text = "Delete product", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 0, column = 0)
        self.add_product_id = Label(self.product_wrk_frame, text = "ID", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 1, column = 0)
        self.add_product_id_e = Entry(self.product_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_product_id_e.grid(row = 1, column = 1)
        self.submit = Button(self.product_wrk_frame, text = "Submit", fg = '#FFFFFA', bg = '#D64045', font=('Montserrat Bold',16), command = self.delete_product_data).place(x = 140, y = 350)

    def search_product(self):
        self.clear_frame()

        self.add_product_id = Label(self.product_wrk_frame, text = "Search product", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 0, column = 0)
        self.add_product_id = Label(self.product_wrk_frame, text = "ID", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 1, column = 0)
        self.add_product_id_e = Entry(self.product_wrk_frame,width = 12 ,fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_product_id_e.grid(row = 1, column = 1)
        self.submit = Button(self.product_wrk_frame, text = "Submit", fg = '#FFFFFA', bg = '#D64045', font=('Montserrat Bold',16), command = self.search_product_data).place(x = 140, y = 350)

    def add_product_data(self):
        id = int(self.add_product_id_e.get()) 
        name = self.add_product_name_e.get()
        cpu = self.add_product_cpu_e.get()
        ram = self.add_product_ram_e.get()
        hard_disk = self.add_product_hard_disk_e.get()
        os = self.add_product_os_e.get()
        cost = self.add_product_cost_e.get()

        try:
            id = int(id)
        except:
            mes = Label(self.product_wrk_frame, text = "Invalid", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.grid(row = 8, column = 1)
            mes.after(3000,lambda:mes.destroy())           

        if id < 0 or id == '' or name == '' or os == '' or cpu == '' or ram == '' or hard_disk == '' or cost == '':
            mes = Label(self.product_wrk_frame, text = "Invalid", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.grid(row = 8, column = 1)
            mes.after(3000,lambda:mes.destroy())
        else:
            self.products.append([id, name, cpu, ram, hard_disk, os, cost])
            self.add_product_id_e.delete(0, END)
            self.add_product_name_e.delete(0, END)
            self.add_product_cpu_e.delete(0, END)
            self.add_product_ram_e.delete(0, END)
            self.add_product_hard_disk_e.delete(0, END)
            self.add_product_os_e.delete(0, END)
            self.add_product_cost_e.delete(0, END)
            mes = Label(self.product_wrk_frame, text = "Success", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.grid(row = 8, column = 1)
            mes.after(3000,lambda:mes.destroy())

    def delete_product_data(self):
        id = self.add_product_id_e.get()
        if id == "ID":
            mes = Label(self.product_wrk_frame, text = "Id dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.place(x = 500, y = 33)
            mes.after(3000,lambda:mes.destroy())
            return
        
        for i in range(len(self.products)):
            if self.products[i][0] == id:
                self.products.pop(i)
                mes = Label(self.product_wrk_frame, text = "Success", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
                mes.place(x = 500, y = 33)
                mes.after(3000,lambda:mes.destroy())
                return
        mes = Label(self.product_wrk_frame, text = "Id dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
        mes.place(x = 500, y = 33)
        mes.after(3000,lambda:mes.destroy())

    def search_product_data(self):
        id = self.add_product_id_e.get()
        if id == "ID":
            mes = Label(self.product_wrk_frame, text = "Id dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.place(x = 500, y = 33)
            mes.after(3000,lambda:mes.destroy())
            return
        
        for i in range(len(self.products)):
            if self.products[i][0] == id:
                for j in range(len(self.products[0])):
                    self.e = Label(self.product_wrk_frame, bd = 5, width = 12, wraplength = 100, bg = '#FFFFFA' ,text = self.products[0][j], fg='#141204',font=('Montserrat Bold',16))
                    self.e.grid(row=2, column=j)
                    self.e = Label(self.product_wrk_frame, bd = 5, width = 12, wraplength = 100, bg = '#FFFFFA' ,text = self.products[i][j], fg='#880808',font=('Montserrat Bold',16))
                    self.e.grid(row=3, column=j)
                return
        mes = Label(self.product_wrk_frame, text = "Id dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
        mes.place(x = 500, y = 33)
        mes.after(3000,lambda:mes.destroy())

    #customer function
    def display_customer(self):
        self.clear_frame()
        self.staff_frame.forget()
        self.product_frame.forget()
        self.bill_frame.forget()

        self.customer_frame.pack(expand = TRUE, fill = BOTH)
    
    def show_customer_list(self):
        self.clear_frame()
        
        for i in range(len(self.customers)):
            for j in range(len(self.customers[0])):
                self.e = Label(self.customer_wrk_frame,bd = 5, width = 20, wraplength = 200, bg = '#FFFFFA' ,text = self.customers[i][j], fg='#141204',font=('Montserrat Bold',16))
                self.e.grid(row=i, column=j)
    
    def add_customer(self):
        self.clear_frame()
        
        self.add_customer_tittle = Label(self.customer_wrk_frame, text = "Add customer", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 0, column = 0)
        self.add_customer_id = Label(self.customer_wrk_frame, text = "ID", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 1, column = 0)
        self.add_customer_id_e = Entry(self.customer_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_customer_id_e.grid(row = 1, column = 1)
        self.add_customer_name = Label(self.customer_wrk_frame, text = "Name", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 2, column = 0)
        self.add_customer_name_e = Entry(self.customer_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_customer_name_e.grid(row = 2, column = 1)
        self.add_customer_dob = Label(self.customer_wrk_frame, text = "Dob", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 3, column = 0)
        self.add_customer_dob_e = Entry(self.customer_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_customer_dob_e.grid(row = 3, column = 1)
        self.add_customer_contact_number = Label(self.customer_wrk_frame, text = "Contact Number", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 4, column = 0)
        self.add_customer_contact_number_e = Entry(self.customer_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_customer_contact_number_e.grid(row = 4, column = 1)

        self.submit = Button(self.customer_wrk_frame, text = "Submit", fg = '#FFFFFA', bg = '#D64045', font=('Montserrat Bold',16), command = self.add_customer_data).grid(row = 7, column = 0)

    def delete_customer(self):
        self.clear_frame()

        self.add_customer_id = Label(self.customer_wrk_frame, text = "Delete customer", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 0, column = 0)
        self.add_customer_id = Label(self.customer_wrk_frame, text = "ID", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 1, column = 0)
        self.add_customer_id_e = Entry(self.customer_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_customer_id_e.grid(row = 1, column = 1)
        self.submit = Button(self.customer_wrk_frame, text = "Submit", fg = '#FFFFFA', bg = '#D64045', font=('Montserrat Bold',16), command = self.delete_customer_data).place(x = 140, y = 350)

    def search_customer(self):
        self.clear_frame()

        self.add_customer_contact_number = Label(self.customer_wrk_frame, text = "Search customer", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 0, column = 0)
        self.add_customer_contact_number = Label(self.customer_wrk_frame, text = "Contact Number", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 1, column = 0)
        self.add_customer_contact_number_e = Entry(self.customer_wrk_frame,width = 12 ,fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_customer_contact_number_e.grid(row = 1, column = 1)
        self.submit = Button(self.customer_wrk_frame, text = "Submit", fg = '#FFFFFA', bg = '#D64045', font=('Montserrat Bold',16), command = self.search_customer_data).place(x = 140, y = 350)

    def add_customer_data(self):
        id = self.add_customer_id_e.get()
        name = self.add_customer_name_e.get()
        dob = self.add_customer_dob_e.get()
        contact_number = self.add_customer_contact_number_e.get()
        
        if id == '' and name == '' and dob == '' and contact_number == '':
            mes = Label(self.customer_wrk_frame, text = "Enter information", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'))
            mes.grid(row = 8, column = 1)
            mes.after(3000,lambda:mes.destroy())   
        
        try:
            id = int(id)
        except:
            mes = Label(self.customer_wrk_frame, text = "Invalid id", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'))
            mes.grid(row = 8, column = 1)
            mes.after(3000,lambda:mes.destroy()) 

        try:
            contact_number = int(contact_number)
        except:
            mes = Label(self.customer_wrk_frame, text = "Invalid contact number", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'))
            mes.grid(row = 8, column = 1)
            mes.after(3000,lambda:mes.destroy()) 
   
        if int(id) < 0 or id == '':
            mes = Label(self.customer_wrk_frame, text = "Invalid id", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.grid(row = 7, column = 1)
            mes.after(3000,lambda:mes.destroy())
        elif name == '':
            mes = Label(self.customer_wrk_frame, text = "Invalid name", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.grid(row = 7, column = 1)
            mes.after(3000,lambda:mes.destroy())
        elif dob == '':
            mes = Label(self.customer_wrk_frame, text = "Invalid dob", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.grid(row = 7, column = 1)
            mes.after(3000,lambda:mes.destroy())
        elif contact_number == '' or len(str(contact_number)) != 10 or int(contact_number) < 0:
            mes = Label(self.customer_wrk_frame, text = "Invalid contact number", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.grid(row = 7, column = 1)
            mes.after(3000,lambda:mes.destroy())   
        else:
            self.customers.append([id, name, dob, contact_number])
            self.add_customer_id_e.delete(0, END)
            self.add_customer_name_e.delete(0, END)
            self.add_customer_dob_e.delete(0, END)
            self.add_customer_contact_number_e.delete(0, END)
            mes = Label(self.customer_wrk_frame, text = "Success", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.grid(row = 7, column = 1)
            mes.after(3000,lambda:mes.destroy())
    
    def delete_customer_data(self):
        id = self.add_customer_id_e.get()
        if id == "ID":
            mes = Label(self.customer_wrk_frame, text = "Id dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.place(x = 500, y = 33)
            mes.after(3000,lambda:mes.destroy())
            return

        for i in range(len(self.customers)):
            if self.customers[i][0] == id:
                self.customers.pop(i)
                mes = Label(self.customer_wrk_frame, text = "Success", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
                mes.place(x = 500, y = 33)
                mes.after(3000,lambda:mes.destroy())
                return
        mes = Label(self.customer_wrk_frame, text = "Id dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
        mes.place(x = 500, y = 33)
        mes.after(3000,lambda:mes.destroy())

    def search_customer_data(self):
        contact_number = self.add_customer_contact_number_e.get()
        if contact_number == "Contact Number":
            mes = Label(self.customer_wrk_frame, text = "Contact Number dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.place(x = 500, y = 33)
            mes.after(3000,lambda:mes.destroy())
            return
        
        for i in range(len(self.customers)):
            if self.customers[i][3] == contact_number:
                for j in range(len(self.customers[0])):
                    self.e = Label(self.customer_wrk_frame, bd = 5, width = 20, wraplength = 200, bg = '#FFFFFA' ,text = self.customers[0][j], fg='#141204',font=('Montserrat Bold',16))
                    self.e.grid(row=2, column=j)
                    self.e = Label(self.customer_wrk_frame, bd = 5, width = 20, wraplength = 200, bg = '#FFFFFA' ,text = self.customers[i][j], fg='#880808',font=('Montserrat Bold',16))
                    self.e.grid(row=3, column=j)
                return
        
        mes = Label(self.customer_wrk_frame, text = "Contact Number dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
        mes.place(x = 500, y = 33)
        mes.after(3000,lambda:mes.destroy())
    # #880808: blue, #D64045: light blue, #880808: yellow
    #bill function
    def display_bill(self):
        self.clear_frame()
        self.staff_frame.forget()
        self.product_frame.forget()
        self.customer_frame.forget()

        self.bill_frame.pack(expand = TRUE, fill = BOTH)

    def show_bill_list(self):
        self.clear_frame()
        
        for i in range(len(self.bills)):
            for j in range(len(self.bills[0])):
                self.e = Label(self.bill_wrk_frame,bd = 5, width = 14, wraplength = 100, bg = '#FFFFFA' ,text = self.bills[i][j], fg='#141204',font=('Montserrat Bold',16))
                self.e.grid(row=i, column=j)
    
    def add_bill(self):
        self.clear_frame()
        
        self.add_bill_tittle = Label(self.bill_wrk_frame, text = "Add bill", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 0, column = 0)
        self.add_bill_id = Label(self.bill_wrk_frame, text = "Bill id", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 1, column = 0)
        self.add_bill_id_e = Entry(self.bill_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_bill_id_e.grid(row = 1, column = 1)
        self.add_bill_product_id = Label(self.bill_wrk_frame, text = "Product id", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 2, column = 0)
        self.add_bill_product_id_e = Entry(self.bill_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_bill_product_id_e.grid(row = 2, column = 1)
        self.add_bill_cost = Label(self.bill_wrk_frame, text = "Cost", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 3, column = 0)
        self.add_bill_cost_e = Entry(self.bill_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_bill_cost_e.grid(row = 3, column = 1)

        self.submit = Button(self.bill_wrk_frame, text = "Submit", fg = '#FFFFFA', bg = '#D64045', font=('Montserrat Bold',16), command = self.add_bill_data).grid(row = 4, column = 0)

    def delete_bill(self):
        self.clear_frame()

        self.add_bill_id = Label(self.bill_wrk_frame, text = "Delete bill", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 0, column = 0)
        self.add_bill_id = Label(self.bill_wrk_frame, text = "ID", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 1, column = 0)
        self.add_bill_id_e = Entry(self.bill_wrk_frame, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',16), textvariable = StringVar())
        self.add_bill_id_e.grid(row = 1, column = 1)
        self.submit = Button(self.bill_wrk_frame, text = "Submit", fg = '#FFFFFA', bg = '#D64045', font=('Montserrat Bold',16), command = self.delete_bill_data).place(x = 140, y = 350)

    def search_bill(self):
        self.clear_frame()

        self.add_bill_id = Label(self.bill_wrk_frame, text = "Search bill", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 0, column = 0)
        self.add_bill_id = Label(self.bill_wrk_frame, text = "ID", fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16)).grid(row = 1, column = 0)
        self.add_bill_id_e = Entry(self.bill_wrk_frame,width = 12 ,fg = '#141204', bg = '#FFFFFA', font=('Montserrat Bold',16), textvariable = StringVar())
        self.add_bill_id_e.grid(row = 1, column = 1)
        self.submit = Button(self.bill_wrk_frame, text = "Submit", fg = '#FFFFFA', bg = '#D64045', font=('Montserrat Bold',16), command = self.search_bill_data).place(x = 140, y = 350)

    def add_bill_data(self):
        id = self.add_bill_id_e.get()
        product_id = self.add_bill_product_id_e.get()
        cost = self.add_bill_cost_e.get()
        staff_id = self.staff_id
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        if id == '' or product_id == '' or cost == '':
            mes = Label(self.bill_wrk_frame, text = "Invalid", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.place(x = 500, y = 33)
            mes.after(3000,lambda:mes.destroy())
        else:
            self.bills.append([id, product_id, cost, staff_id, time])
            self.add_bill_id_e.delete(0, END)
            self.add_bill_product_id_e.delete(0, END)
            self.add_bill_cost_e.delete(0, END)


            mes = Label(self.bill_wrk_frame, text = "Success", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.place(x = 500, y = 33)
            mes.after(3000,lambda:mes.destroy())
    
    def delete_bill_data(self):
        id = self.add_bill_id_e.get()
        if id == "Bill_id":
            mes = Label(self.bill_wrk_frame, text = "Id dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.place(x = 500, y = 33)
            mes.after(3000,lambda:mes.destroy())
            return

        for i in range(len(self.bills)):
            if self.bills[i][0] == id:
                self.bills.pop(i)
                mes = Label(self.bill_wrk_frame, text = "Success", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
                mes.place(x = 500, y = 33)
                mes.after(3000,lambda:mes.destroy())
                return
        mes = Label(self.bill_wrk_frame, text = "Id dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
        mes.place(x = 500, y = 33)
        mes.after(3000,lambda:mes.destroy())

    def search_bill_data(self):
        id = self.add_bill_id_e.get()
        if id == "ID":
            mes = Label(self.bill_wrk_frame, text = "Id dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
            mes.place(x = 500, y = 33)
            mes.after(3000,lambda:mes.destroy())
            return
        
        for i in range(len(self.bills)):
            if self.bills[i][0] == id:
                for j in range(len(self.bills[0])):
                    self.e = Label(self.bill_wrk_frame, bd = 5, width = 15, wraplength = 110, bg = '#FFFFFA' ,text = self.bills[0][j], fg='#141204',font=('Montserrat Bold',14))
                    self.e.grid(row = 2, column = j)
                    self.e = Label(self.bill_wrk_frame, bd = 5, width = 15, wraplength = 110, bg = '#FFFFFA' ,text = self.bills[i][j], fg='#880808',font=('Montserrat Bold',14))
                    self.e.grid(row = 3, column=j)
                return
        mes = Label(self.bill_wrk_frame, text = "Id dont exist", fg = '#D64045', bg = '#FFFFFA', font=('Montserrat Bold',16))
        mes.place(x = 480, y = 33)
        mes.after(3000,lambda:mes.destroy())

if __name__ == "__main__":
    root = Tk()
    obj = Management(root, "1")
    root.mainloop()