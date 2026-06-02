from options_form import OptionsForm
from tkinter import messagebox

if __name__ == "__main__":
    settings = None

    def set_settings(selections):
        if (selections):
            settings = selections
            result_text = "\n".join(f"• {k}: {v}" for k, v in settings.items())
    
            messagebox.showinfo("Success", f"Form submitted successfully!\n\n{result_text}")
        else:
            messagebox.showinfo("Failure", "Form failed to submit!")
  
    OptionsForm(set_settings)