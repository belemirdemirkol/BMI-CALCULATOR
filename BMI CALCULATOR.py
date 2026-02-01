import tkinter
window=tkinter.Tk()
window.title("MY BMI CALCULATOR")
window.minsize(width=500, height=500)
window.config(bg="pink")

def clickt_button():
    try:
        user_input=my_entry.get()
        user_input2=my_entry2.get()
        weight=float(user_input)
        height=float(user_input2)/100
        bmi=weight/(height*height)
        if bmi<18:
            my_label3.config(text="You are underweight")
        elif bmi<25:
            my_label3.config(text="You are normal")
        elif bmi<30:
            my_label3.config(text="You are overweight")
        elif bmi<35:
            my_label3.config(text="You are obese")
        else:
            my_label3.config(text="NO COMMENT!!!")
    except ValueError:
        my_label3.config(text="Please enter a number")

my_label=tkinter.Label(text="ENTER YOUR WEIGHT")
my_label.config(bg="pink",fg="white",font=("Times New Roman",18,"bold"))
my_label.pack()
my_entry=tkinter.Entry(width=30)
my_entry.pack()
my_label2=tkinter.Label(text="ENTER YOUR HEIGHT")
my_label2.config(bg="pink",fg="white",font=("Times New Roman",18,"bold"))
my_label2.pack()
my_entry2=tkinter.Entry(width=30)
my_entry2.pack()
my_label3=tkinter.Label(text="YOUR RESULT")
my_label3.config(bg="pink",fg="white",font=("Times New Roman",18,"bold"))
my_label3.pack()
my_button=tkinter.Button(text="Click Me",command=clickt_button)
my_button.pack()

window.mainloop()

