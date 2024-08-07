BACKGROUND_COLOR = "#B1DDC6"
from tkinter import*
import random
import pandas
import time
data_c={}

#-------------------setup data----------------#
with open("french_words.csv","r") as data:
    dataframe=pandas.read_csv(data)

print (dataframe)
data_dic = dataframe.to_dict(orient="records")
print(data_dic)

#---------Card--------------------#
def card_french():
    global data_c
    french_c=data_c.get("French")
    english_c=data_c.get("English")

    f_card="card_front.png"
    e_card="card_back.png"

    f_label="French"
    e_label="English"



    card_side = PhotoImage(file=f_card)
    canvas.create_image(400, 320, image=card_side)
    canvas.config(bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)

    canvas.itemconfig(lang_text,text=f_label)
    canvas.itemconfig(word_text,text=french_c)
    print(french_c)

def card_english():
    global data_c
    english_c=data_c.get("English")

    e_card="card_back.png"

    e_label="English"

    card_side = PhotoImage(file=e_card)
    canvas.create_image(400, 320, image=card_side)


    canvas.itemconfig(lang_text,text=e_label)
    canvas.itemconfig(word_text,text=english_c)
    print(english_c)



#------------------Random word------------------#

def word():
    global num
    global data_c
    canvas.delete("text")
    num=random.randint(0,(len(data_dic)-1))

    #card_side = PhotoImage(file="card_front.png")
    #canvas.create_image(400, 320, image=card_side)
   # canvas.config(bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)

    data_c=data_dic[num]







#--------------------Right--------------------------#
def right():
    global num
    word()
    card_french()
    data_dic.pop(num)
    print(len(data_dic))

    window.after(2000,card_english)






#------------------Wrong-----------------------------#

def wrong():
    word()
    card_french()
    window.after(2000, card_english)

#-----------------------GUI------------------------#
window=Tk()
window.config(padx=10,pady=10,bg=BACKGROUND_COLOR)


canvas=Canvas(width=800,height=580)
card_side=PhotoImage(file="card_front.png")
canvas.create_image(400,320,image=card_side)
canvas.config(bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
lang_text=canvas.create_text(400,250,text="hello",font=("Ariel", 40, "italic"))
word_text=canvas.create_text(400,363,text="hello again",font=("Ariel", 65, "bold"))



canvas.grid(column=1,row=1,columnspan=2,padx=10,pady=10)

right_image = PhotoImage(file="right.png")
buttonR = Button(image=right_image, highlightthickness=4,bg=BACKGROUND_COLOR,command=right)
buttonR.grid(column=1,row=2,padx=50,pady=50)

wrong_image = PhotoImage(file="wrong.png")
buttonW = Button(image=wrong_image, highlightthickness=4,bg=BACKGROUND_COLOR,command=wrong)
buttonW.grid(column=2,row=2,padx=50,pady=50)


#my_image = PhotoImage(file="path/to/image_file.png")






window.mainloop()