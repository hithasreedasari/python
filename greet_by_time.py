from datetime import datetime
import tkinter as tk
from tkinter import ttk


def _parse_time_input(time_text):
    if not time_text:
        return None
    time_text = time_text.strip()
    for fmt in ("%H:%M", "%H:%M:%S"):
        try:
            parsed = datetime.strptime(time_text, fmt)
            now = datetime.now()
            return now.replace(hour=parsed.hour, minute=parsed.minute, second=parsed.second, microsecond=0)
        except ValueError:
            continue
    raise ValueError("Time must be in HH:MM or HH:MM:SS format")


def greet_by_time(dt=None, time_text=None):
    if dt is None:
        if time_text is not None:
            dt = _parse_time_input(time_text)
        if dt is None:
            dt = datetime.now()
    hour = dt.hour
    if 5 <= hour < 12:
        return "Good morning"
    if 12 <= hour < 17:
        return "Good afternoon"
    if 17 <= hour < 22:
        return "Good evening"
    return "Good night"


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Greeting by Time")
    root.geometry("360x180")
    root.resizable(False, False)

    main = ttk.Frame(root, padding=16)
    main.pack(fill="both", expand=True)

    ttk.Label(main, text="Enter time (HH:MM or HH:MM:SS):").pack(anchor="w")
    time_var = tk.StringVar()
    time_entry = ttk.Entry(main, textvariable=time_var, width=24)
    time_entry.pack(anchor="w", pady=(4, 8))

    result_var = tk.StringVar(value="Press Greet to use current time.")
    result_label = ttk.Label(main, textvariable=result_var)
    result_label.pack(anchor="w", pady=(4, 8))

    def on_greet():
        user_time = time_var.get().strip()
        try:
            if user_time:
                greeting = greet_by_time(time_text=user_time)
            else:
                greeting = greet_by_time()
            result_var.set(greeting)
        except ValueError as exc:
            result_var.set(str(exc))

    greet_button = ttk.Button(main, text="Greet", command=on_greet)
    greet_button.pack(anchor="w")

    time_entry.focus()
    root.mainloop()
