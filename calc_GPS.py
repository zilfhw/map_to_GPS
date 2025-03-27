from tkinter import Tk, Canvas
from PIL import Image, ImageTk

# GPS-Koordinaten der Ecken
top_left = (54.333770, 8.557424)  # Oben links
bottom_right = (54.308226, 8.604160)  # Unten rechts

# Bildpfad
image_path = "C:/Users/zilske/workspace/map_to_GPS/map_to_GPS/sankt_peter.jpg"

# Funktion zur Berechnung der GPS-Koordinaten
def calculate_gps(x, y, img_width, img_height):
    lat_diff = top_left[0] - bottom_right[0]
    lon_diff = bottom_right[1] - top_left[1]

    latitude = top_left[0] - (y / img_height) * lat_diff
    longitude = top_left[1] + (x / img_width) * lon_diff

    return latitude, longitude

# Funktion, die bei einem Klick aufgerufen wird
def on_click(event):
    latitude, longitude = calculate_gps(event.x, event.y, img_width, img_height)
    print(f"GPS-Koordinaten: {latitude:.6f}, {longitude:.6f}")

# Hauptprogramm
root = Tk()
root.title("GPS-Koordinaten Rechner")

# Bild laden
image = Image.open(image_path)
img_width, img_height = image.size
photo = ImageTk.PhotoImage(image)

# Canvas erstellen und Bild anzeigen
canvas = Canvas(root, width=img_width, height=img_height)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=photo)

# Klick-Event binden
canvas.bind("<Button-1>", on_click)

# GUI starten
root.mainloop()