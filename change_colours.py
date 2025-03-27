from PIL import Image, ImageOps, ImageTk
import tkinter as tk

# Bildpfad
input_image_path = "C:/Users/zilske/workspace/map_to_GPS/DJI_20240719094428_0050_T.jpg"  # Ersetze durch den Pfad deines Wärmebildes

# Funktion zur Umwandlung des Bildes
def convert_to_greyscale_with_red_highlights(input_path):
    # Bild öffnen
    image = Image.open(input_path)

    # In Graustufen umwandeln
    greyscale_image = ImageOps.grayscale(image)

    # Bild in RGB konvertieren, um Rot hinzuzufügen
    rgb_image = greyscale_image.convert("RGB")

    # Pixel bearbeiten
    pixels = rgb_image.load()
    width, height = rgb_image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Helle Bereiche hervorheben
            if r > 225:  # Schwellenwert für Helligkeit
                pixels[x, y] = (255, 0, 0)  # Rot

    return rgb_image

# Hauptprogramm
def main():
    # Bild umwandeln
    processed_image = convert_to_greyscale_with_red_highlights(input_image_path)

    # GUI erstellen
    root = tk.Tk()
    root.title("Wärmebild in Graustufen mit Rot")

    # Bild in tkinter anzeigen
    tk_image = ImageTk.PhotoImage(processed_image)
    label = tk.Label(root, image=tk_image)
    label.pack()

    # GUI starten
    root.mainloop()

main()