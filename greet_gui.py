import tkinter as tk
from tkinter import ttk

from greet_by_time import greet_by_time


def main():
    root = tk.Tk()
    root.title("Greeting by Time")
    root.geometry("360x180")
    root.resizable(False, False)

    main_frame = ttk.Frame(root, padding=16)
    main_frame.pack(fill="both", expand=True)

    ttk.Label(main_frame, text="Enter time (HH:MM or HH:MM:SS):").pack(anchor="w")
    time_var = tk.StringVar()
    time_entry = ttk.Entry(main_frame, textvariable=time_var, width=24)
    time_entry.pack(anchor="w", pady=(4, 8))

    result_var = tk.StringVar(value="Press Greet to use current time.")
    ttk.Label(main_frame, textvariable=result_var).pack(anchor="w", pady=(4, 8))

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

    ttk.Button(main_frame, text="Greet", command=on_greet).pack(anchor="w")

    time_entry.focus()
    root.mainloop()


if __name__ == "__main__":
    main()
