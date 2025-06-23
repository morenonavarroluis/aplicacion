import tkinter as tk
from tkinter import messagebox
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageTk
import qrcode

def generate_barcode():
    data = entry.get()
    if not data:
        messagebox.showinfo("Info", "Please enter data to generate the barcode.")
        return
    try:
        barcode_obj = barcode.get('code128', data, writer=ImageWriter())
        filename = "barcode"
        barcode_obj.save(filename)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("barcode.png")
        image_path = filename + '.png'
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        barcode_label.config(image=photo)
        barcode_label.image = photo
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate barcode: {e}")

root = tk.Tk()
root.title("Barcode Generator")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

generate_btn = tk.Button(root, text="Generate Barcode", command=generate_barcode)
generate_btn.pack(pady=5)

barcode_label = tk.Label(root)
barcode_label.pack(pady=10)

root.mainloop()
