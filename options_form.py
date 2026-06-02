from logging import root
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from calendar_popup import CalendarPopup

# Constructor creates the form and returns the selected values once closed
class OptionsForm:
    form_selections = None #placeholder for selected data

    def __init__(self, callback): 
        self.callback = callback     
        self.root = tk.Tk()
        self.root.title("Enhanced Registration Form")
        self.root.geometry("450x600")
        self.root.resizable(False, False)

        # Variables        
        self.name_var = tk.StringVar(value="Maki Zermalias")
        self.email_var = tk.StringVar(value="maki.zermalias@pecktech.com")
        self.password_var = tk.StringVar(value="fuckoff")
        self.country_var = tk.StringVar(value="Jia Na Da")
        self.gender_var = tk.StringVar(value="Male")
        self.dob_var = tk.StringVar()
		
		# Checkboxes for interests        
        self.interests = {
			"Programming": tk.BooleanVar(value=True),
			"Design": tk.BooleanVar(), 
			"Marketing": tk.BooleanVar(), 
			"Data Science": tk.BooleanVar() 
		}

        self.calendar_window = None
        self.create_widgets()

        # Close handler
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.root.mainloop()

    def on_close(self):
        self.root.destroy()
        self.callback(self.form_selections)

    def create_widgets(self):
		# Title
        tk.Label(self.root, text="Enhanced Registration Form",
                 font=("Arial", 16, "bold")).pack(pady=15)
			
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10, padx=30, fill="x")
		
        row = 0

        # Name        
        tk.Label(form_frame, text="Full Name:").grid(row=row, column=0, sticky="w", pady=6)
        tk.Entry(form_frame, textvariable=self.name_var, width=35).grid(row=row, column=1, pady=6)
        row += 1
        
        # Email        
        tk.Label(form_frame, text="Email:").grid(row=row, column=0, sticky="w", pady=6) 
        tk.Entry(form_frame, textvariable=self.email_var, width=35).grid(row=row, column=1, pady=6)
        row += 1

        # Password        
        tk.Label(form_frame, text="Password:").grid(row=row, column=0, sticky="w", pady=6)
        tk.Entry(form_frame, textvariable=self.password_var, width=35, show="•").grid(row=row, column=1, pady=6)
        row += 1

        # Date of Birth - Calendar popup        
        tk.Label(form_frame, text="Date of Birth:").grid(row=row, column=0, sticky="nw", pady=6)
        self.dob_entry = tk.Entry(form_frame, textvariable=self.dob_var, state="readonly", width=35)
        self.dob_entry.grid(row=row, column=1, pady=6)
        self.dob_entry.insert(0, "Click to select date...")

        # Bind click event to text field
        self.dob_entry.bind("<Button-1>", self.show_calendar_popup)
       
        row += 1
		
        # Country Dropdown        
        tk.Label(form_frame, text="Country:").grid(row=row, column=0, sticky="w", pady=6)
        countries = [
            "Canada", 
            "United States", 
            "Mexico", 
            "France", 
            "Germany",
            "Japan", 
            "Brazil", 
            "India", 
            "United Kingdom"
        ]
        country_combo = ttk.Combobox(
            form_frame, 
            textvariable=self.country_var,
            values=countries, 
            width=32, 
            state="readonly"
        )
        country_combo.grid(row=row, column=1, pady=6)
        country_combo.current(0)
        row += 1
		
        # Gender        
        tk.Label(form_frame, text="Gender:").grid(row=row, column=0, sticky="w", pady=6)
        gender_frame = tk.Frame(form_frame)
        gender_frame.grid(row=row, column=1, sticky="w", pady=6)
        tk.Radiobutton(
            gender_frame, 
            text="Male", 
            variable=self.gender_var, 
            value="Male"
        ).pack(side="left", padx=8) 
        tk.Radiobutton(
            gender_frame, 
            text="Female", 
            variable=self.gender_var, 
            value="Female"
        ).pack(side="left", padx=8)
        tk.Radiobutton(
            gender_frame, 
            text="Other", 
            variable=self.gender_var, 
            value="Other"
        ).pack(side="left", padx=8)
        row += 1
		
        # Interests (Checkboxes)        
        tk.Label(form_frame, text="Interests:").grid(row=row, column=0, sticky="nw", pady=6)
        interests_frame = tk.Frame(form_frame)
        interests_frame.grid(row=row, column=1, sticky="w", pady=6)
        for i, (interest, var) in enumerate(self.interests.items()):
            tk.Checkbutton(
                interests_frame, 
                text=interest, 
                variable=var
            ).grid(row=i//2, 
                   column=i%2, 
                   sticky="w", 
                   padx=5
                )
        row += 1
		
        # Submit Button        
        tk.Button(
            self.root, 
            text="Submit Form", 
            font=("Arial", 11, "bold"),
			bg="#4CAF50", 
            fg="white", 
            height=2, 
            width=20,
			command=self.submit_form
        ).pack(pady=25)
        
    def show_calendar_popup(self, event=None):
        CalendarPopup(self.root, self.set_dob)
    
    def set_dob(self, date_value):
        self.dob_var.set(date_value)
		
    def submit_form(self):
        if not self.name_var.get().strip():
            messagebox.showwarning("Error", "Name is required!")
            return
        if not self.email_var.get().strip():
            messagebox.showwarning("Error", "Email is required!")
            return

        # Get selected interests
        selected_interests = [interest for interest, var in self.interests.items() if var.get()]
        self.form_selections = {
            "Name": self.name_var.get(),
            "Email": self.email_var.get(),
            "Password": "••••••••" if self.password_var.get() else "Not provided",
            "Date of Birth": self.dob_var.get() or "Not selected",
            "Country": self.country_var.get(),
            "Gender": self.gender_var.get(),
            "Interests": selected_interests or "None selected"
        }

        self.on_close()
    
