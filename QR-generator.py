"""
    Qr code generator
    Version: 1.0
    Program in improvement to generate a QR from information provided
    Created by: wilopg
"""
# Imports
import qrcode
import os

# Colors
c_black = (0, 0, 0)
c_white = (255, 255, 255)


def main_menu():
    """
    Function that shows the main menu and leads to the sub-functions.
    """
    while True:
        os.system("cls")
        print("__________________________________________")
        print("Welcome to program \"QR generator\"")
        print("Created by wilopg")
        print("__________________________________________")
        print("[1] Create QR web address")
        print("[2] Create QR vCard")
        print("[0] Exit")
        try:
            option = int(input(" > "))
        except ValueError:
            print("\n\n\nError: unrecognized value\n\n\n")
            continue

        if option == 1:
            menu_qr_web()
        if option == 2:
            menu_qr_vcard()
        if option == 0:
            print("Come back soon!")
            break


def menu_qr_web():
    """
    Function that shows the submenu to generate a QR from a website, collects the information and sends it to the generating function,
    if everything went well, it indicates that the QR was saved; if not, report an error (but don't show it).
    """
    os.system("cls")
    print("__________________________________________")
    print("Web address generator")
    print("__________________________________________")
    url = input(
        "Please enter full URL (example: https://www.miweb.com/):\n(Leave blank to go back)\n > ")
    if url:
        if qr_web(url):
            input("QR generated correctly\nSaved to script path\n(Enter to continue)")
        else:
            input("Unknown error (Enter to continue)")


def menu_qr_vcard():
    """
    Function that shows the submenu to generate a QR from a vCard, collects the information and sends it to the generating function,
    if everything went well, it indicates that the QR was saved; if not, please report a bug (but don't show it)
    """
    data = ["", "", "", "", ""]
    items = ['"Name"', '"Last name"', '"Phone"', '"E-mail"', '"personal web url (example: https://www.miweb.com/)"']
    os.system("cls")
    print("__________________________________________")
    print("vCard QR Generator")
    print("__________________________________________")
    for i in range(len(items)):
        print("Please enter " + items[i] + ":")
        if i > 1:
            print("(Enter to leave blank)")
            data[i] = input(" > ")
        else:
            print("(Leave blank to go back)")
            data[i] = input(" > ")
            if not data[i]:
                return
    if qr_vcard(data):
        input("QR generated correctly\nSaved to script path\n(Enter to continue)")
    else:
        input("Unknown error (Enter to continue)")


def qr_web(url):
    """
    Function in charge of generating and saving the QR of the web generated from the information received from the function
    \"menu_qr_web\", returns True if there were no errors, False otherwise.
    """
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=8,
        )
        qr.add_data(url)
        img = qr.make_image(fill_color=c_black, back_color=c_white)
        img.save("QR_Web.png")
        return True
    except:
        return False


def qr_vcard(data):
    """
    Function in charge of generating and saving the QR of the vCard generated from the information received from the function
    \"menu_qr_vcard\", returns True if there were no errors, False otherwise.
    """
    data_card = ["BEGIN:VCARD", "VERSION:3.0", "END:VCARD"]
    try:
        value = "N:" + data[1] + ";" + data[0] + ";;;"
        data_card.insert(2, value)
        value = "FN:" + data[0] + " " + data[1]
        data_card.insert(3, value)
        if data[2]:
            value = "TEL;TYPE=CELL,VOICE:" + data[2]
            data_card.insert(-1, value)
        if data[3]:
            value = "EMAIL;TYPE=HOME,PREF,INTERNET:" + data[3]
            data_card.insert(-1, value)
        if data[4]:
            value = "URL:" + data[4]
            data_card.insert(-1, value)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=5,
            border=14,
        )
        qr.add_data("\n".join(data_card))
        img = qr.make_image(fill_color=c_black,
                            back_color=c_white)
        img.save("QR_vCard.png")
        return True
    except:
        return False


# We launch the application
if __name__ == "__main__":
    main_menu()
