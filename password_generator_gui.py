import tkinter as tk 
import password_generator
from tkinter import messagebox


def generate():
    length = None 
    errors =[]  
        
    if password_generator.validate_length(length_entry.get()):
        length = int(length_entry.get())
    else:
        errors.append("Invalid length.")

        
    if password_generator.validate_amount(amount_entry.get()):
        amount = int(amount_entry.get())
    else:
        errors.append("Invalid amount.")


    selection = set()

    if(low_var.get()):
        selection.add("low")
    if(up_var.get()):
        selection.add("up")
    if(num_var.get()):
        selection.add("num")
    if(sym_var.get()):
        selection.add("sym")
    
    
    
    if not selection:
        errors.append("No types selected.")

    if length is not None and length < len(selection):
        errors.append(f"Too many character types for a password of length {length}.")
    
    if errors:
        errors = "\n".join(errors)
        messagebox.showerror("Error", errors)
        return

    
    passwords = password_generator.generate_passwords(amount, length, selection)
    entropy = password_generator.get_entropy(length, selection)

    output_text.config(state="normal")
    output_text.delete("1.0",tk.END)
    output_text.insert("1.0", "\n".join(passwords))
    output_text.config(state="disabled")

    entropy_label.config(text=f"\nPassword entropy : {entropy:.2f} bits")
    

        

root = tk.Tk()

root.title("Secure Password Generator")

root.geometry("1000x600")

title_label = tk.Label(root, text="Secure Password Generator")
title_label.pack(anchor="nw")

length_label = tk.Label(root, text="Password length :")
length_label.pack(anchor="nw")
length_entry = tk.Entry(root)
length_entry.pack(anchor="nw")

amount_label = tk.Label(root, text="Number of passwords :")
amount_label.pack(anchor="nw")
amount_entry = tk.Entry(root)
amount_entry.pack(anchor="nw")

generate_button = tk.Button(root, text="Generate",command=generate)
generate_button.pack(anchor="se")

low_var = tk.BooleanVar()
up_var = tk.BooleanVar()
num_var = tk.BooleanVar()
sym_var = tk.BooleanVar()

low_checkbox = tk.Checkbutton(root, text="Lowercase Letters", variable=low_var)
low_checkbox.pack(anchor="nw")

up_checkbox = tk.Checkbutton(root, text="Uppercase Letters", variable= up_var)
up_checkbox.pack(anchor="nw")

num_checkbox = tk.Checkbutton(root, text="Numbers", variable=num_var)
num_checkbox.pack(anchor="nw")

sym_checkbox = tk.Checkbutton(root, text="Symbols", variable=sym_var)
sym_checkbox.pack(anchor="nw")

output_text = tk.Text(root, height=10, width=60)
output_text.pack()

entropy_label = tk.Label(root, text="")
entropy_label.pack()





root.mainloop()