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
    print("the button is clicked")

photo1 = PhotoImage(file='pic1.png').subsample(9, 9)
button = Button(window,
                text="convert",
                command=click,
                font=("Comic Sans", 10),
                fg="#34908B", bg="#FDF4AF",
                activebackground="#6FBEB2",
                activeforeground="#A5E9DD",
                state=ACTIVE,
                image=photo1,
                compound='center')

button.pack()


window.mainloop()