# https://github.com/teacherRay/mind.git
import random
import tkinter as tk

from PIL import Image
import requests
from io import BytesIO

import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_Wheeler_Dealers_episodes'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
rows = soup.find_all('tr')
#print(rows[:10])
print(rows)
# containers = soup.findAll('tr')
# print (containers)

#container = containers[0]
#print(soup.prettify(containers[0]))
#affirmation = container.find_all('{"<div id="th0ths_quotes_sc_quote" style="font-style: oblique;"}')
#print(affirmation)


pixurl = "https://picsum.photos/500/500"
response = requests.get(pixurl)
img = Image.open(BytesIO(response.content))

#print(img)
#img.show()
img.save('tmp.png')
#my dictionary of affirmations
affirmations={
'health':'All the cells and atoms of my body are working together to create perfect health.', 
'mind':'I stay calm and relaxed by reqular meditation.',
'strength':'I enjoy exercises that strengthen my body and mind',
'life':'What would it look like to be living my ideal life?',
'inside':'I have everything I need inside me now.',
'abundant':'I am abundant.',
'forgiveness':'I forgive myself for what I have done, and I forgive all those who have harmed me.',
'teachers':'My teachers are everyone I encounter.',
'gratitude':'I am grateful for everything I have.'
}

#my list of images
#pix=('cup.png','negative.png','destined.png','do_something.png','tmp.png')

#randomly choose affirmations and images to display
choose_quote=random.choice(list(affirmations.values()))
#choose_pix=random.choice(list(pix))
choose_pix='tmp.png'

#make the window
root = tk.Tk()
root.title('Affirmation of the Day')
root.iconbitmap("clouds.ico")

canvas=tk.Canvas(root, height = 550, width = 600)
canvas.pack()

background_image = tk.PhotoImage(file = choose_pix)
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

lower_frame = tk.Frame(root)
lower_frame.place(relx = 0.5, rely = 1, relwidth = 1, relheight = 0.1, anchor = 's')

label = tk.Label(lower_frame, font = ('Courier', 14), wraplength=500)
label.place(relwidth = 1, relheight = 1)


label['text'] = choose_quote

root.mainloop()
