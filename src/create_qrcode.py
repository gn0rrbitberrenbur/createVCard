import qrcode
from tkinter import messagebox
from PIL import Image, ImageTk

from gui import *

def create_vCard(entryName, entryLastName, entryCity, 
                entryState, entryPostCode, entryCountry, 
                entryMobileNumber, entryEmail, entryURL, 
                entryPath, qr_label
                ):

    lastName = entryLastName.get()
    name = entryName.get()
    city = entryCity.get()
    state = entryState.get()
    postcode = entryPostCode.get()
    country = entryCountry.get()
    mobileNumber = entryMobileNumber.get()
    email = entryEmail.get()
    url = entryURL.get()

    VCARD = f"""BEGIN:VCARD
VERSION:3.0
N:{lastName};
FN:{name}
ADR;type=HOME:;;;{city};{state};{postcode};{country}
TEL;type=CELL:{mobileNumber}
EMAIL;type=PERSONAL,INTERNET:{email}
URL:{url}
END:VCARD"""

    createQRCode(VCARD, entryPath, name, lastName, qr_label)
    

def createQRCode(VCARD, entryPath, name, lastName, qr_label):
    path = entryPath.get()
    qrObject = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qrObject.add_data(VCARD)
    qrObject.make(fit=True)
    
    img = qrObject.make_image(fill_color="black", back_color="white").convert("RGBA")

    if not path:
        messagebox.showerror(title="Error", message="Please select a valid path to save the QR code.")
        return
    try:
        final_path = f"{path}/{name}{lastName}_vCard.png"
        img.save(final_path)

        messagebox.showinfo(title = "Success!",message = "The new filepath was saved.")
        display_qr_code(final_path, qr_label)

    except Exception as e:
        messagebox.showerror(title = "Error",message = f"Ein Fehler ist aufgetreten: {e}")

def display_qr_code(final_path, qr_label):
    try:
        img = Image.open(final_path)
        img = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)

        qr_label.config(image=img_tk)
        qr_label.image = img_tk
    except Exception as e:
        messagebox.showerror("Error", f"Could not display QR code: {e}")
        qr_label.config(text="Could not display QR code.")