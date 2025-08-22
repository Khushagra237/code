import matplotlib.pyplot as plt
students_names = ["Rahul", "Kanak", "Yug", "Vartik", "Ramesh", "Aarav", "Aakarsh", "Aarav", "Abhinav"]
students_marks=[35, 50, 20, 45, 25, 40, 25, 40, 30]
marks_perc= []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)

print(marks_perc)
def marks_line_chart():
    plt.plot(students_names, marks_perc)
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.title("Students Marks Graph")
    plt.show()

marks_line_chart()

def percentage_bar_chart():
    plt.bar(students_names, marks_perc)
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.title("Students Percentage Graph")
    plt.show()

percentage_bar_chart()