import tkinter
window=tkinter.Tk()
window.title("BMI CALCULATOR")
window.geometry("500x500")
window.config(bg="pink")

def click_button():
         weight_input=weight_entry.get()
         height_input=height_entry.get()
         result_entry.delete(0, tkinter.END)
         try:
             w=float(weight_input)
             h=float(height_input)/100
             BMI=w/(h*h)

             if BMI<18.5:
                 result_entry.insert(0,f"BMI: {BMI:.2f}-You are underweight")
             elif 18.5<=BMI<25:
                 result_entry.insert(0,f"BMI: {BMI:.2f}-You are normal")
             elif 25<=BMI<30:
                 result_entry.insert(0,f"BMI: {BMI:.2f}-You are overweight")
             elif 30<=BMI<40:
                 result_entry.insert(0,f"BMI: {BMI:.2f}-You are obese")
             else:
                 result_entry.insert(0,"NO COMMENT!!!")

         except ValueError:
             result_entry.insert(0,"Please enter both weight and height correctly")



weight_label=tkinter.Label(text="Please Enter Your Weight",bg="pink",fg="black",font=("Times New Roman",25))
weight_entry=tkinter.Entry(width=15,font=("Times New Roman",15,))
weight_label.pack()
weight_entry.pack()
height_label=tkinter.Label(text="Please Enter Your Height",bg="pink",fg="black",font=("Times New Roman",25))
height_entry=tkinter.Entry(width=15,font=("Times New Roman",15))
height_label.pack()
height_entry.pack()
button=tkinter.Button(text="Click for Result",command=click_button)
result_entry=tkinter.Entry(width=34,font=("Times New Roman",15))
button.pack(pady=20)
result_entry.pack()

window.mainloop()

