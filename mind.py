# https://github.com/teacherRay/mind.git
import random
import tkinter as tk


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

pix=('cup.png','negative.png','destined.png','do_something.png')

#randomly choose affirmations and images to display
choose_quote=random.choice(list(affirmations.values()))
choose_pix=random.choice(list(pix))

#make the window
root = tk.Tk()
root.title('Affirmation of the Day')
root.iconbitmap("clouds.ico")

canvas=tk.Canvas(root, height = 550, width = 1000)
canvas.pack()

background_image = tk.PhotoImage(file =choose_pix)
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

lower_frame = tk.Frame(root)
lower_frame.place(relx = 0.5, rely = 1, relwidth = 1, relheight = 0.1, anchor = 's')

label = tk.Label(lower_frame, font = ('Courier', 14))
label.place(relwidth = 1, relheight = 1)


label['text'] = choose_quot

root.mainloop()
