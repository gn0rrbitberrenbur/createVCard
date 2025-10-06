import tkinter as tk
from tkinter import filedialog


from create_qrcode import create_vCard

class VCardApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("vCard Creator")
        self.window.geometry("700x700")
        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        # Row 0: Name - Last name
        self.labelName = tk.Label(self.window, text="Name")
        self.entryName = tk.Entry(self.window, width=15, font=("Arial", 17), justify=tk.CENTER)
        self.labelLastName = tk.Label(self.window, text="Last name")
        self.entryLastName = tk.Entry(self.window, width=15, font=("Arial", 17), justify=tk.CENTER)
        self.labelName.grid(row=0, column=0, padx=8, pady=8)
        self.entryName.grid(row=0, column=1, padx=8, pady=8)
        self.labelLastName.grid(row=0, column=2, padx=8, pady=8)
        self.entryLastName.grid(row=0, column=3, padx=8, pady=8)

        # Row 1: Postcode - City
        self.labelPostCode = tk.Label(self.window, text="Postcode")
        self.entryPostCode = tk.Entry(self.window, width=15, font=("Arial", 17), justify=tk.CENTER)
        self.labelCity = tk.Label(self.window, text="City")
        self.entryCity = tk.Entry(self.window, width=15, font=("Arial", 17), justify=tk.CENTER)
        self.labelPostCode.grid(row=1, column=0, padx=8, pady=8)
        self.entryPostCode.grid(row=1, column=1, padx=8, pady=8)
        self.labelCity.grid(row=1, column=2, padx=8, pady=8)
        self.entryCity.grid(row=1, column=3, padx=8, pady=8)

        # Row 2: State - Country
        self.labelState = tk.Label(self.window, text="State")
        self.entryState = tk.Entry(self.window, width=15, font=("Arial", 17), justify=tk.CENTER)
        self.labelCountry = tk.Label(self.window, text="Country")
        self.entryCountry = tk.Entry(self.window, width=15, font=("Arial", 17), justify=tk.CENTER)
        self.labelState.grid(row=2, column=0, padx=8, pady=8)
        self.entryState.grid(row=2, column=1, padx=8, pady=8)
        self.labelCountry.grid(row=2, column=2, padx=8, pady=8)
        self.entryCountry.grid(row=2, column=3, padx=8, pady=8)

        # Row 3: Mobile number - Email
        self.labelMobileNumber = tk.Label(self.window, text="Mobile number")
        self.entryMobileNumber = tk.Entry(self.window, width=15, font=("Arial", 17), justify=tk.CENTER)
        self.labelEmail = tk.Label(self.window, text="Email")
        self.entryEmail = tk.Entry(self.window, width=15, font=("Arial", 17), justify=tk.CENTER)
        self.labelMobileNumber.grid(row=3, column=0, padx=8, pady=8)
        self.entryMobileNumber.grid(row=3, column=1, padx=8, pady=8)
        self.labelEmail.grid(row=3, column=2, padx=8, pady=8)
        self.entryEmail.grid(row=3, column=3, padx=8, pady=8)

        # Row 4: URL
        self.labelURL = tk.Label(self.window, text="URL")
        self.entryURL = tk.Entry(self.window, width=40, font=("Arial", 17), justify=tk.CENTER)
        self.labelURL.grid(row=4, column=0, padx=8, pady=8, columnspan=1)
        self.entryURL.grid(row=4, column=1, padx=8, pady=8, columnspan=3)

        # Row 5: Path to save QR code
        self.labelPath = tk.Label(self.window, text="Save QR-Code to:")
        self.entryPath = tk.Entry(self.window, width=40, font=("Arial", 17), justify=tk.CENTER)
        self.labelPath.grid(row=5, column=0, padx=8, pady=8, columnspan=1)
        self.entryPath.grid(row=5, column=1, padx=8, pady=8, columnspan=3)

        self.buttonFileDialog = tk.Button(self.window, text="...", command=self.browse_path)
        self.buttonFileDialog.grid(row=5, column=4, padx=8, pady=8)

        # Row 6: Create QR code button
        self.buttonCreateQR = tk.Button(
            self.window,
            text="Create QR-Code",
            command=self.create_qr_code
        )
        self.buttonCreateQR.grid(row=6, column=0, columnspan=4, pady=16)

        # Row 7: QR code display
        self.qr_label = tk.Label(self.window)
        self.qr_label.grid(row=7, column=0, columnspan=5, pady=16)

    def browse_path(self):
        path = filedialog.askdirectory()
        if path:
            self.entryPath.delete(0, tk.END)
            self.entryPath.insert(0, path)


    def create_qr_code(self):
        create_vCard(
            self.entryName,
            self.entryLastName,
            self.entryCity,
            self.entryState,
            self.entryPostCode,
            self.entryCountry,
            self.entryMobileNumber,
            self.entryEmail,
            self.entryURL,
            self.entryPath,
            self.qr_label
        )


if __name__ == "__main__":
    VCardApp()