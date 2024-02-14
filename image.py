from PIL import Image, ImageTk
import tkinter as Tk
from tkinter import Tk, Label
root = Tk()
image = Image.open(r"C:\Users\Bushra\Downloads\COFFEE1.jpg");
image.show();
# Convert Image to PhotoImage
image_tk = ImageTk.PhotoImage(image)

# Create Tkinter window


# Create Tkinter Label and display the image
label = Label(root, image=image_tk)
label.pack()

# Run the Tkinter event loop
root.mainloop()