from tkinter import *
import pyttsx3

# window
window = Tk()
window.geometry("720x720")
window.title("text to speech")

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)

window.config(background="#FFFAF3")

# label

photo = PhotoImage(file='pic2.png').subsample(2, 3)
label = Label(window, text="Start converting your text to speech",
              font=('Arial', 22, 'bold'),
              fg='#F62440', bg="#FFFAF3",
              image=photo, compound='center')
label.pack(pady=40)

# buttons

def click():
    text_to_speak = entry.get().strip()

    if text_to_speak:
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)
        engine.say(text_to_speak)
        engine.runAndWait()
    else:
        print("write some text first..")

#photo1 = PhotoImage(file='pic1.png').subsample(9, 9)
button = Button(window,
                text="convert",
                command=click,
                font=("Comic Sans", 14, "bold"),
                fg="grey", bg="#FFFAF3",
                activebackground="#ff6b81", activeforeground="white",
                bd=0, width=10, cursor="hand2")

button.pack(pady=40)

# entry - button

input_frame = Frame(window, bg='#FFFAF3')
input_frame.pack(pady=40)

entry = Entry(input_frame,
              font=("Arial", 14),
              fg="#F62440", bg="#FFF2DB",
              insertbackground="#F62440",
              relief=SOLID, bd=1, width=30)
entry.pack(ipady=5, padx=10)

buttons_frame = Frame(input_frame, bg="#FFFAF3")
buttons_frame.pack(pady=20)

# def submit():
#     username = entry.get()
#     print("hello", username)
#
# def delete():
#     entry.delete(0, END)
#
# submit_button = Button(buttons_frame, text="Submit", command=submit,
#                        font=("Arial", 11, "bold"),
#                        fg="#F62440", bg="#FFF2DB",
#                        activebackground="#6FBEB2", activeforeground="white",
#                        bd=0, width=10, cursor="hand2")
# submit_button.pack(side=LEFT, padx=10)
#
# delete_button = Button(buttons_frame, text="Delete", command=delete,
#                        font=("Arial", 11, "bold"),
#                        fg="#FFF2DB", bg="#F62440",
#                        activebackground="#ff6b81", activeforeground="white",
#                        bd=0, width=10, cursor="hand2")
# delete_button.pack(side=LEFT, padx=10)


window.mainloop()