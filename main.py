import tkinter as tk

# เซ็ตจอ
wn = tk.Tk()
wn.title("App Doo Grade")
wn.minsize(width=1280, height=520)


# สูตรคำนวน
def Show_output():
    gradeM4_1 = float(input_M4_1.get())
    gradeM4_2 = float(input_M4_2.get())
    gradeM5_1 = float(input_M5_1.get())
    gradeM5_2 = float(input_M5_2.get())
    gradeM6_1 = float(input_M6_1.get())
    gradeM6_2 = float(input_M6_2.get())
    term = int(input_title_term_Q1.get())

    grade = float(gradeM4_1 + gradeM4_2 + gradeM5_1 + gradeM5_2 + gradeM6_1 + gradeM6_2)
    GPAX = float(grade / term)
    a = eval(format(float(GPAX), '.2f'))

    output2 = tk.Label(master=wn, text="ได้", font=("Arial Bold", 30))
    output2.grid(column=1, row=10)
    output.configure(text=a)


# โหมด
title = tk.Label(master=wn, text="Calculater for GPAX", font=("Arial Bold", 50))
title.grid(column=1, row=0)

# ม.4
M4_1 = tk.Label(master=wn, text="\tใส่เกรดเฉลี่ย ม.4 เทอม 1 ", font=("Arial Bold", 20))
M4_1.grid(column=0, row=1)
input_M4_1 = tk.Entry(master=wn, width=50, font=("Arial Bold", 20))
input_M4_1.grid(column=1, row=1)

M4_2 = tk.Label(master=wn, text="\tใส่เกรดเฉลี่ย ม.4 เทอม 2 ", font=("Arial Bold", 20))
M4_2.grid(column=0, row=2)
input_M4_2 = tk.Entry(master=wn, width=50, font=("Arial Bold", 20))
input_M4_2.grid(column=1, row=2)

# ม.5
M5_1 = tk.Label(master=wn, text="\tใส่เกรดเฉลี่ย ม.5 เทอม 1 ", font=("Arial Bold", 20))
M5_1.grid(column=0, row=3)
input_M5_1 = tk.Entry(master=wn, width=50, font=("Arial Bold", 20))
input_M5_1.grid(column=1, row=3)

M5_2 = tk.Label(master=wn, text="\tใส่เกรดเฉลี่ย ม.5 เทอม 2 ", font=("Arial Bold", 20))
M5_2.grid(column=0, row=4)
input_M5_2 = tk.Entry(master=wn, width=50, font=("Arial Bold", 20))
input_M5_2.grid(column=1, row=4)

# ม.6
M6_1 = tk.Label(master=wn, text="\tใส่เกรดเฉลี่ย ม.6 เทอม 1 ", font=("Arial Bold", 20))
M6_1.grid(column=0, row=5)
input_M6_1 = tk.Entry(master=wn, width=50, font=("Arial Bold", 20))
input_M6_1.grid(column=1, row=5)

M6_2 = tk.Label(master=wn, text="\tใส่เกรดเฉลี่ย ม.6 เทอม 2 ", font=("Arial Bold", 20))
M6_2.grid(column=0, row=6)
input_M6_2 = tk.Entry(master=wn, width=50, font=("Arial Bold", 20))
input_M6_2.grid(column=1, row=6)

# ถามว่าจะเอากี่เฉลี่ยนกี่เทอม
title_term_Q1 = tk.Label(master=wn, text="\tเฉลี่ยกี่เทอม", font=("Arial Bold", 20))
title_term_Q1.grid(column=0, row=7)
input_title_term_Q1 = tk.Entry(master=wn, width=50, font=("Arial Bold", 20))
input_title_term_Q1.grid(column=1, row=7)

go_button = tk.Button(master=wn, text="คำนวณ", command=Show_output, font=("Arial Bold", 30))
go_button.grid(column=1, row=8)

output = tk.Label(master=wn, font=("Arial Bold", 30))
output.grid(column=1, row=11)

wn.mainloop()
