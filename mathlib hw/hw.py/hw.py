import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Name': ['Rahul', 'Kanak', 'Yug', 'Vartik',  'Aarav'],
    'Maths': [45, 78, 89, 66, 55],
    'Science': [55, 90, 79, 68, 60],
    'English': [65, 88, 75, 85, 70]
}
df = pd.DataFrame(data)
print(df)
plt.plot(df['Name'], df['Maths'], marker = 'o')
plt.title('Maths Scores of Students')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()

plt.bar(df['Name'], df['Science'], color = 'orange')
plt.title('Science Scores of Students')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()

plt.bar(df['Name'], df['English'], color = 'green', edgecolor = 'black')
plt.title('English Scores of Students')
plt.xlabel('Students')
plt.ylabel('Marks Range')
plt.show()

plt.scatter(df['Maths'], df['Science'], color = 'red')
plt.title('Maths vs Science Performance')
plt.xlabel('Maths Marks')
plt.ylabel('Science Marks')
plt.show()

marks = [78, 88, 70]
subjects = ['Science', 'Maths', 'English']
plt.pie(marks, labels = subjects, autopct='%1.1f%%')
plt.title('Subject-wise Performance of Student A')
plt.show()