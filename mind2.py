# https://github.com/teacherRay/mind.git
import random
import tkinter as tk
import json
from PIL import Image
import requests
from io import BytesIO


pixurl = "https://picsum.photos/500/500"
response = requests.get(pixurl)
img = Image.open(BytesIO(response.content))
img.save('tmp.png')
choose_pix='tmp.png'

#Open affirmations.json into my dictionary of affirmations
with open("affirmations.json", "r") as read_file:
    affirmations = json.load(read_file)

#randomly choose affirmations and images to display
choose_quote=random.choice(list(affirmations.values()))

#make the window
root = tk.Tk()
root.title('Affirmation of the Day')
root.iconbitmap("clouds.ico")

canvas=tk.Canvas(root, height = 550, width = 600)
canvas.pack()
    
#randomly choose affirmations and images to display
choose_quote=random.choice(list(affirmations.values()))

background_image = tk.PhotoImage(file = choose_pix)
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

lower_frame = tk.Frame(root)
lower_frame.place(relx = 0.5, rely = 1, relwidth = 1, relheight = 0.1, anchor = 's')

label = tk.Label(lower_frame, font = ('Courier', 14), wraplength=500)
label.place(relwidth = 1, relheight = 1)

label['text'] = choose_quote

root.mainloop()
