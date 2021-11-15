from tkinter import *

def calculateBMI(event):
    w = float(inputBox_weight.get())
    h = (float(inputBox_height.get())/100)**2
    cal_bmi = w/h

    if cal_bmi > 30:
        show_result_number.configure(text=(w/h))
        show_result_text.configure(text="อ้วนมาก")
    elif 29.9 > cal_bmi > 25:
        show_result_number.configure(text=(w / h))
        show_result_text.configure(text="อ้วน")
    elif 24.9 > cal_bmi > 23:
        show_result_number.configure(text=(w / h))
        show_result_text.configure(text="น้ำหนักเกิน")
    elif 22.9 > cal_bmi > 18.6:
        show_result_number.configure(text=(w / h))
        show_result_text.configure(text="น้ำหนักปกติ/เหมาะสม")
    elif cal_bmi < 18.5:
        show_result_number.configure(text=(w / h))
        show_result_text.configure(text="ผอมเกินไป")
    else:
        print('')

# GUI part
mainWindow = Tk()

# Height input
label_height = Label(mainWindow, text="Height (cm.)")
label_height.grid(row=0, column=0)
inputBox_height = Entry(mainWindow)
inputBox_height.grid(row=0, column=1)

# Weight input
label_weight = Label(mainWindow, text="Weight (kg.)")
label_weight.grid(row=1, column=0)
inputBox_weight = Entry(mainWindow)
inputBox_weight.grid(row=1, column=1)

# Calculate button
cal_button = Button(mainWindow, text="Calculate")
cal_button.bind('<Button-1>', calculateBMI)
cal_button.grid(row=3, column=1)

# Result
label_result = Label(mainWindow, text="Result =")
label_result.grid(row=4, column=0)
show_result_number = Label(mainWindow, text=" ")
show_result_number.grid(row=4, column=1)
show_result_text = Label(mainWindow, text=" ")
show_result_text.grid(row=5, column=1)

mainWindow.mainloop()
