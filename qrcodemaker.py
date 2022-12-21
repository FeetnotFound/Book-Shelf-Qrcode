import qrcode





BookName = str(input("Whats the book name?\n"))
Author = str(input("Who's the Author of the book?\n"))
Genre = str(input("What is the genre of the book?\n"))
DatePublished = str(input("Whats the date the book published? DD/MM/YYYY\n"))
Summary = str(input("What is the book about?\n"))

BookValue = f"""
    Book Name: {BookName},
    Author: {Author},
    Genre: {Genre},
    Date Published: {DatePublished},
    Summary: {Summary}
"""

qr = qrcode.QRCode(version= 6,
                    box_size= 4,
                    border= 10)

qr.add_data(BookValue) 

qr.make(fit = True)

img = qr.make_image(fill_color = 'blue',
                    back_color = 'black')


img.save(f"{BookName}.png")