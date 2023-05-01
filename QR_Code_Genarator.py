import qrcode
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

class QRGenerator:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")

        # Create URL input label and entry box
        self.url_label = Label(master, text="Enter URL:")
        self.url_label.pack(pady=10)
        self.url_entry = Entry(master)
        self.url_entry.pack(fill=X, padx=10)

        # Create Generate QR button
        self.generate_button = Button(master, text="Generate QR", command=self.generate_qr)
        self.generate_button.pack(pady=10)

        # Create Quit button
        self.quit_button = Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=10)

    def generate_qr(self):
        # Get URL from entry box
        url = self.url_entry.get()

        # Generate QR code
        QR = qrcode.make(url)

        # Display QR code in a new window
        qr_window = Toplevel(self.master)
        qr_window.title("QR Code")

        # Display QR code image
        qr_image = ImageTk.PhotoImage(QR)
        qr_label = Label(qr_window, image=qr_image)
        qr_label.image = qr_image
        qr_label.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        # Create Save button
        save_button = Button(qr_window, text="Save QR Code", command=lambda: self.save_qr(QR))
        save_button.pack(pady=10)

    def save_qr(self, QR):
        # Get file path from user
        file_path = filedialog.asksaveasfilename(defaultextension=".png")

        # Save QR code to file
        if file_path:
            QR.save(file_path)

# Create Tkinter window
root = Tk()

# Create QRGenerator object
qr_generator = QRGenerator(root)

# Set window minimum size
root.minsize(300, 200)

# Run Tkinter event loop
root.mainloop()
