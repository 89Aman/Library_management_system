import tkinter as tk
from tkinter import messagebox, simpledialog,ttk
import datetime
import colorama
import csv


#sign out function
def sign_out():
    MsgBox = tk.messagebox.askquestion ('Sign Out','Are you sure you want to sign out',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
       
# Main screen function
def login_success():
    global root
    login_screen.destroy()
    root = tk.Tk()
    root.title("library Management System")

    frame = tk.Frame(root)
    frame.pack(pady=30)

    bottomframe = tk.Frame(root)
    bottomframe.pack( side = tk.BOTTOM, pady=10 )

    addButton = tk.Button(frame, text ="Add Records", command=add_record, padx=10, pady=5)
    addButton.pack( side = tk.LEFT, padx=5)

    updateButton = tk.Button(frame, text ="Update Records",command=update_records, padx=10, pady=5)
    updateButton.pack(side = tk.LEFT, padx=5 )

    view_button = tk.Button(frame, text="View Records", command=view_records,padx=10, pady=5)
    view_button.pack(side = tk.LEFT, padx=5)

    bookshelfButton = tk.Button(frame, text ="Bookshelf",command=bookshelf, padx=10, pady=5)
    bookshelfButton.pack(side = tk.LEFT, padx=5)

    signoutButton = tk.Button(bottomframe, text ="Sign Out", command=sign_out, bg="red", fg="white", padx=10, pady=5)
    signoutButton.pack(side = tk.RIGHT, padx=5)

    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timeLabel = tk.Label(bottomframe, text=time, relief=tk.SUNKEN)
    timeLabel.pack(side = tk.LEFT)

    root.mainloop()

# Add record function
def add_record():
    global add_screen, name, reg_id, issue_date, book_id, class_
    add_screen = tk.Toplevel(root)
    add_screen.title("Add Record")
    
    tk.Label(add_screen, text="Name").pack()
    name = tk.Entry(add_screen)
    name.pack()
    
    tk.Label(add_screen, text="Registration ID").pack()
    reg_id = tk.Entry(add_screen)
    reg_id.pack()
    
    tk.Label(add_screen, text="Issue Date").pack()
    issue_date = tk.Entry(add_screen)
    issue_date.pack()
    
    tk.Label(add_screen, text="Book ID").pack()
    book_id = tk.Entry(add_screen)
    book_id.pack()
    
    tk.Label(add_screen, text="Class").pack()
    class_ = tk.Entry(add_screen)
    class_.pack()
    
    submit_button = tk.Button(add_screen, text="Submit", command=submit)
    submit_button.pack(pady=10)

#show records
def view_records():
    show_screen = tk.Toplevel(root)
    show_screen.title("Records")
    tree = ttk.Treeview(show_screen, columns=('Name', 'Registration ID', 'Issue Date', 'Book ID', 'Class'), show='headings')
    tree.heading('Name', text='Name')
    tree.heading('Registration ID', text='Registration ID')
    tree.heading('Issue Date', text='Issue Date')
    tree.heading('Book ID', text='Book ID')
    tree.heading('Class', text='Class')
    tree.pack()
    with open('records.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            tree.insert('', 'end', values=row)

            
#show bookshelf
def bookshelf():
    bookshelf_screen = tk.Toplevel(root)
    bookshelf_screen.title("Bookshelf")
    tree = ttk.Treeview(bookshelf_screen, columns=('Title', 'Price', 'Author', 'Date of Publish', 'Genre'), show='headings')
    tree.heading('Title', text='Title')
    tree.heading('Price', text='Price')
    tree.heading('Author', text='Author')
    tree.heading('Date of Publish', text='Date of Publish')
    tree.heading('Genre', text='Genre')
    tree.pack()
    with open('bookshelf.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            tree.insert('', 'end', values=row)


# Submit function
def submit():
    with open('records.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name.get(), reg_id.get(), issue_date.get(), book_id.get(), class_.get()])
    add_screen.destroy()


#login screen
def verify_login():
    user = username_verify.get()
    password = password_verify.get()
    if user == "admin" and password =="123":
        login_success()
    else:
        messagebox.showerror("Error", "Wrong password , Try Again")


def update_records():
    update_screen = tk.Toplevel(root)
    update_screen.title("Update Records")
    tree = ttk.Treeview(update_screen, columns=('Name', 'Registration ID', 'Issue Date', 'Book ID', 'Class'), show='headings')
    tree.heading('Name', text='Name')
    tree.heading('Registration ID', text='Registration ID')
    tree.heading('Issue Date', text='Issue Date')
    tree.heading('Book ID', text='Book ID')
    tree.heading('Class', text='Class')
    tree.pack()
    with open('records.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            tree.insert('', 'end', values=row)
    delete_button = tk.Button(update_screen, text="Delete", command=lambda: delete_record(tree))
    delete_button.pack(padx=10, pady=10)
    back_button = tk.Button(update_screen, text="Back", command=update_screen.destroy)
    back_button.pack(padx=10, pady=10)

# Delete record function
def delete_record(tree):
    selected_item = tree.selection()[0]
    tree.delete(selected_item)
      with open('records.csv', 'a) as f:
        reader = csv.writer(f)
        for row in reader:
            
    
#login check   
login_screen = tk.Tk()
login_screen.title("Login")

username_verify = tk.StringVar()
password_verify = tk.StringVar()

tk.Label(login_screen, text="Username").pack()
username_entry = tk.Entry(login_screen, textvariable=username_verify)
username_entry.pack()

tk.Label(login_screen, text="Password").pack()
password_entry = tk.Entry(login_screen, textvariable=password_verify, show='*')
password_entry.pack()

tk.Button(login_screen, text="Login", command=verify_login).pack()

login_screen.mainloop()




