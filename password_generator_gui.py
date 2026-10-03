import tkinter as tk 
import password_generator
from tkinter import messagebox

class GUI :
    def __init__(self, root):
        self.root = root
        self.setup_gui()
    def setup_gui(self):
        self.root.title("Secure Password Generator")
        self.root.geometry("700x600")
        self.root.resizable(False, False)

        # Main container
        main_frame = tk.Frame(self.root, padx=30, pady=25)
        main_frame.pack(fill="both", expand=True)

        # Title
        title_label = tk.Label(
            main_frame,
            text="Secure Password Generator",
            font=("Arial", 20, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 25))

        # Password length
        length_label = tk.Label(main_frame, text="Password length:")
        length_label.grid(row=1, column=0, sticky="w", pady=5)

        self.length_entry = tk.Entry(main_frame, width=20)
        self.length_entry.grid(row=1, column=1, sticky="ew", pady=5)

        # Number of passwords
        amount_label = tk.Label(main_frame, text="Number of passwords:")
        amount_label.grid(row=2, column=0, sticky="w", pady=5)

        self.amount_entry = tk.Entry(main_frame, width=20)
        self.amount_entry.grid(row=2, column=1, sticky="ew", pady=5)

        # Character types
        types_label = tk.Label(
            main_frame,
            text="Character types:",
            font=("Arial", 10, "bold")
        )
        types_label.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(20, 5)
        )

        self.low_var = tk.BooleanVar()
        self.up_var = tk.BooleanVar()
        self.num_var = tk.BooleanVar()
        self.sym_var = tk.BooleanVar()

        low_checkbox = tk.Checkbutton(
            main_frame, text="Lowercase Letters", variable=self.low_var
        )
        low_checkbox.grid(row=4, column=0, sticky="w")

        up_checkbox = tk.Checkbutton(
            main_frame, text="Uppercase Letters", variable=self.up_var
        )
        up_checkbox.grid(row=4, column=1, sticky="w")

        num_checkbox = tk.Checkbutton(
            main_frame, text="Numbers", variable=self.num_var
        )
        num_checkbox.grid(row=5, column=0, sticky="w")

        sym_checkbox = tk.Checkbutton(
            main_frame, text="Symbols", variable=self.sym_var
        )
        sym_checkbox.grid(row=5, column=1, sticky="w")

        # Generate button
        generate_button = tk.Button(
            main_frame,
            text="Generate",
            command=self.generate,
            width=20
        )
        generate_button.grid(
            row=6,
            column=0,
            columnspan=2,
            pady=20
        )

        # Password output
        self.output_text = tk.Text(
            main_frame,
            height=12,
            width=60,
            state="disabled"
        )
        self.output_text.grid(
            row=7,
            column=0,
            columnspan=2,
            sticky="nsew"
        )

        # Entropy
        self.entropy_label = tk.Label(
            main_frame,
            text=""
        )
        self.entropy_label.grid(
            row=8,
            column=0,
            columnspan=2,
            pady=(10, 0)
        )

        # Allow columns to share available space
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
    
    def generate(self):
        length = None 
        errors =[]  
            
        if password_generator.validate_length(self.length_entry.get()):
            length = int(self.length_entry.get())
        else:
            errors.append("Invalid length.")

            
        if password_generator.validate_amount(self.amount_entry.get()):
            amount = int(self.amount_entry.get())
        else:
            errors.append("Invalid amount.")


        selection = set()

        if(self.low_var.get()):
            selection.add("low")
        if(self.up_var.get()):
            selection.add("up")
        if(self.num_var.get()):
            selection.add("num")
        if(self.sym_var.get()):
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

        self.output_text.config(state="normal")
        self.output_text.delete("1.0",tk.END)
        self.output_text.insert("1.0", "\n".join(passwords))
        self.output_text.config(state="disabled")

        self.entropy_label.config(text=f"\nPassword entropy : {entropy:.2f} bits")


def main():
    
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
