from tkinter import *

def calculate_bmi():
    gender = gender_var.get()
    mass = float(mass_entry.get())
    height = float(height_entry.get())
    bmi = mass / (height ** 2)
    bmi_label.config(text="BMI: {:.2f}".format(bmi))
    
    if gender == "m":
        if bmi < 20:
            classification_label.config(text="Untergewicht")
        elif bmi < 25:
            classification_label.config(text="Normalgewicht")
        else:
            classification_label.config(text="Übergewicht")
    else:
        if bmi < 19:
            classification_label.config(text="Untergewicht")
        elif bmi < 24:
            classification_label.config(text="Normalgewicht")
        else:
            classification_label.config(text="Übergewicht")

root = Tk()
root.title("BMI-Rechner")

gender_var = StringVar(value="m")

gender_label = Label(root, text="Geschlecht:")
gender_label.grid(row=0, column=0)

male_button = Radiobutton(root, text="männlich", variable=gender_var, value="m")
male_button.grid(row=0, column=1)

female_button = Radiobutton(root, text="weiblich", variable=gender_var, value="w")
female_button.grid(row=0, column=2)

mass_label = Label(root, text="Masse (kg):")
mass_label.grid(row=1, column=0)

mass_entry = Entry(root)
mass_entry.grid(row=1, column=1)

height_label = Label(root, text="Größe (m):")
height_label.grid(row=2, column=0)

height_entry = Entry(root)
height_entry.grid(row=2, column=1)

calculate_button = Button(root, text="Berechne BMI", command=calculate_bmi)
calculate_button.grid(row=3, column=0)

bmi_label = Label(root)
bmi_label.grid(row=3, column=1)

classification_label = Label(root)
classification_label.grid(row=4, column=1)

root.mainloop()
