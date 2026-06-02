import tkinter as tk
from tkcalendar import Calendar
from datetime import date

class CalendarPopup:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback   # function to receive selected date

        # Disable parent window
        parent.attributes("-disabled", True)

        # Create popup
        self.win = tk.Toplevel(parent)
        self.win.title("Select Date")
        self.win.geometry("300x300")
        self.win.resizable(False, False)
        self.win.transient(parent)
        self.win.grab_set()

        # Center popup
        x = parent.winfo_x() + 80
        y = parent.winfo_y() + 100
        self.win.geometry(f"+{x}+{y}")

        # Calendar widget
        today = date.today()
        self.cal = Calendar(
            self.win,
            selectmode="day",
            year=today.year,
            month=today.month,
            day=today.day,
            date_pattern="yyyy-mm-dd"
        )
        self.cal.pack(pady=10)

        # Select button
        tk.Button(
            self.win,
            text="Select Date",
            command=self.select_date,
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            width=15,
            height=2
        ).pack(pady=10)

        # Close handler
        self.win.protocol("WM_DELETE_WINDOW", self.close)

    def select_date(self):
        selected = self.cal.get_date()
        self.callback(selected)
        self.close()

    def close(self):
        self.parent.attributes("-disabled", False)
        self.win.destroy()