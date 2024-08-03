BACKGROUND_COLOR = "#B1DDC6"
from tkinter import*
import random
import pandas
num=0

#-------------------setup data----------------#
with open("french_words.csv","r") as data:
    dataframe=pandas.read_csv(data)

print (dataframe)



#------------------Random word------------------#

def word():
    global num
    canvas.delete("text")
    num=random.randint(0,len(data_dic))

    #
    # data_dic=dataframe.to_dict(orient="records")
    # print(data_dic)
    data_c=data_dic[num]
    french_c=data_c.get("French")
    print(french_c)

    canvas.create_text(400,250,text="french",font=("Ariel", 40, "italic"))
    canvas.create_text(400,363,text=french_c,font=("Ariel", 65, "bold"),tags="text")






#--------------------Right--------------------------#
def right():
    global num
    word()
    data_dic.pop(num)
    print(len(data_dic))





#------------------Wrong-----------------------------#



#-----------------------GUI------------------------#
window=Tk()
window.config(padx=10,pady=10,bg=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=580)
card_side=PhotoImage(file="card_front.png")
canvas.create_image(400,320,image=card_side)
canvas.config(bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
#canvas.create_text(400,250,text="hello",font=("Ariel", 40, "italic"))
#canvas.create_text(400,363,text="hello again",font=("Ariel", 65, "bold"))
#text_f = canvas.create_text(400, 363, text="start", font=("Ariel", 65, "bold"))


canvas.grid(column=1,row=1,columnspan=2,padx=10,pady=10)

right_image = PhotoImage(file="right.png")
buttonR = Button(image=right_image, highlightthickness=4,bg=BACKGROUND_COLOR)
buttonR.grid(column=1,row=2,padx=50,pady=50)

wrong_image = PhotoImage(file="wrong.png")
buttonW = Button(image=wrong_image, highlightthickness=4,bg=BACKGROUND_COLOR,command=right)
buttonW.grid(column=2,row=2,padx=50,pady=50)

data_dic = dataframe.to_dict(orient="records")
print(data_dic)

#my_image = PhotoImage(file="path/to/image_file.png")






window.mainloop()