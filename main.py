BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *




#-----------------------GUI------------------------#
window=Tk()
window.config(width=500, height=500,bg=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=580)
card_side=PhotoImage(file="card_front.png")
canvas.create_image(400,320,image=card_side)
canvas.config(bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
canvas.create_text(400,250,text="hello",font=("Ariel", 40, "italic"))
canvas.create_text(400,363,text="hello again",font=("Ariel", 65, "bold"))


canvas.grid(column=1,row=1,columnspan=2,padx=10,pady=10)

right_image = PhotoImage(file="right.png")
buttonR = Button(image=right_image, highlightthickness=4,bg=BACKGROUND_COLOR)

buttonR.grid(column=1,row=2,padx=50,pady=50)

wrong_image = PhotoImage(file="wrong.png")
buttonW = Button(image=wrong_image, highlightthickness=4,bg=BACKGROUND_COLOR)
buttonW.grid(column=2,row=2,padx=50,pady=50)



#my_image = PhotoImage(file="path/to/image_file.png")













window.mainloop()