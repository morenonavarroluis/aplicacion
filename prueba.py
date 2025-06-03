import tkinter as tk
from tkinter import ttk

class ModalDialog(tk.Toplevel):
    def __init__(self, parent, title="Modal Dialog", message="This is a modal dialog"):
        super().__init__(parent)
        self.title(title)
        self.transient(parent)  # Keep dialog on top of parent
        self.grab_set()  # Make all other windows inactive

        self.parent = parent

        # Set window size and position relative to parent
        self.geometry("300x150")
        self.resizable(False, False)

        # Message label
        label = ttk.Label(self, text=message, wraplength=280, anchor="center", justify="center")
        label.pack(pady=20, padx=10)

        # OK button to close modal
        btn_ok = ttk.Button(self, text="OK", command=self.close)
        btn_ok.pack(pady=(0, 20))

        # Bind Escape key to close modal
        self.bind("<Escape>", lambda e: self.close())

        # Center the modal relative to the parent window
        self.center_window()

        self.protocol("WM_DELETE_WINDOW", self.close)

        # Wait for this window to be closed before returning control to parent
        self.wait_window(self)

    def center_window(self):
        self.update_idletasks()
        parent_x = self.parent.winfo_rootx()
        parent_y = self.parent.winfo_rooty()
        parent_width = self.parent.winfo_width()
        parent_height = self.parent.winfo_height()

        width = self.winfo_width()
        height = self.winfo_height()

        x = parent_x + (parent_width // 2) - (width // 2)
        y = parent_y + (parent_height // 2) - (height // 2)
        self.geometry(f"+{x}+{y}")

    def close(self):
        self.grab_release()
        self.destroy()

# Example usage of modal dialog
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    root.title("Main Window")

    def open_modal():
        ModalDialog(root, title="Info", message="This is a modal message!")

    btn_open = ttk.Button(root, text="Open Modal", command=open_modal)
    btn_open.pack(expand=True)

    root.mainloop()

