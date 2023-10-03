import tkinter as tk
from tkinter import messagebox

# Create a list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    contacts.append({"Name": name,
                    "Phone": phone, 
                    "Email": email, 
                    "Address": address})
    clear_fields()
    update_contact_list()

# Function to view all contacts
def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, contact["Name"] + " - " + contact["Phone"])

# Function to search for a contact
def search_contact():
    search_term = search_entry.get()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if search_term in contact["Name"] or search_term in contact["Phone"]:
            contact_list.insert(tk.END, contact["Name"] + " - " + contact["Phone"])

# Function to update a contact
def update_contact():
    selected_contact = contact_list.curselection()
    if not selected_contact:
        return
    selected_contact = selected_contact[0]
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    contacts[selected_contact] = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    clear_fields()
    update_contact_list()

# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.curselection()
    if not selected_contact:
        return
    selected_contact = selected_contact[0]
    del contacts[selected_contact]
    clear_fields()
    update_contact_list()

# Function to clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to update the contact list
def update_contact_list():
    view_contacts()

# Create the main window
root = tk.Tk()
root.title("Contact Manager")

# Create and configure widgets
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)

phone_label = tk.Label(root, text="Phone:")
phone_entry = tk.Entry(root)

email_label = tk.Label(root, text="Email:")
email_entry = tk.Entry(root)

address_label = tk.Label(root, text="Address:")
address_entry = tk.Entry(root)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
view_button = tk.Button(root, text="View Contacts", command=view_contacts)
search_label = tk.Label(root, text="Search:")
search_entry = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=search_contact)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)

contact_list = tk.Listbox(root, width=40, height=10)

# Arrange widgets using grid layout
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

phone_label.grid(row=1, column=0)
phone_entry.grid(row=1, column=1)

email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1)

address_label.grid(row=3, column=0)
address_entry.grid(row=3, column=1)

add_button.grid(row=4, column=0)
view_button.grid(row=4, column=1)
search_label.grid(row=5, column=0)
search_entry.grid(row=5, column=1)
search_button.grid(row=5, column=2)

contact_list.grid(row=0, column=2, rowspan=6)

update_button.grid(row=6, column=0)
delete_button.grid(row=6, column=1)

# Start the Tkinter main loop
root.mainloop()
