from tkinter import *

# window
window = Tk()
window.geometry("420x420")
window.title("text to voice")

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)

window.config(background="#FDF4AF")

# label

photo = PhotoImage(file='pic2.png').subsample(2, 2)
label = Label(window, text="put ur text",
              font=('Arial', 40, 'bold'),
              fg='#6FBEB2', bg="#FDF4AF",
              image=photo, compound='bottom')
label.pack()

# buttons

def click():
    print("u clicked the button")

button = Button(window,
                text="convert",
                command=click)
button.pack()


window.mainloop()