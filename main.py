import random
from tkinter import *

# Array
numbers = [1, 2, 3, 4, 5, 6]

# Functions
def answer():
    return random.choice(numbers)

def roll():
    temp = answer()
    try:
        guess = int(input_field.get())
        if guess in numbers:
            if guess == temp:
                output_text.config(text="You won!")
                match temp:
                    case 1:
                        output_image.config(image=d1)
                    case 2:
                        output_image.config(image=d2)
                    case 3:
                        output_image.config(image=d3)
                    case 4:
                        output_image.config(image=d4)
                    case 5:
                        output_image.config(image=d5)
                    case 6:
                        output_image.config(image=d6)
            else:
                output_text.config(text="You lost. \nTry again.")
                match temp:
                    case 1:
                        output_image.config(image=d1)
                    case 2:
                        output_image.config(image=d2)
                    case 3:
                        output_image.config(image=d3)
                    case 4:
                        output_image.config(image=d4)
                    case 5:
                        output_image.config(image=d5)
                    case 6:
                        output_image.config(image=d6)
        else:
            output_text.config(text="Please enter\na number\nfrom 1 to 6.")
    except ValueError:
        output_text.config(text="Please enter\na number.")

def retry():
    window.update()
    window.update_idletasks()
    #answer()
    input_field.delete(0, "end")
    output_text.config(text="")
    output_image.config(image="")

# Main window
window = Tk()
window.title("Dice Roller")
window.geometry("300x300")
favicon = PhotoImage(file="Images/dice_favicon.png")
window.iconphoto(True, favicon)
window.resizable(False, False)
# Dice's images
d1 = PhotoImage(file="Images/d1.png")
d2 = PhotoImage(file="Images/d2.png")
d3 = PhotoImage(file="Images/d3.png")
d4 = PhotoImage(file="Images/d4.png")
d5 = PhotoImage(file="Images/d5.png")
d6 = PhotoImage(file="Images/d6.png")

# Caption
caption = Label(window, text="Dice Roller", font=("arial", 30, "bold"))
caption.pack()

# "Enter your guess here" label
label = Label(window, text="Enter your guess here", font=("arial", 12))
label.pack()

# Input entry box
input_field = Entry(window, font=("arial", 10), width=5)
input_field.place(x=116, y=75)

# Roll button
roll_button = Button(window, text="Roll", command=roll, width=5, height=2)
roll_button.place(x=90, y=100)

# Retry button
retry_button = Button(window, text="Retry", command=retry, width=5, height=2)
retry_button.place(x=140, y=100)

# Answer label
answer_label = Label(window, text="Answer", font=("arial", 12))
answer_label.place(x=110, y=160)

# Output text
output_text = Label(window)
output_text.place(x=110, y=180)

# Output image
output_image = Label(window)
output_image.place(x=105, y=215)

window.mainloop()