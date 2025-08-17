import pandas as pd
import numpy as np
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no',
                 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
print("\n Display first 3 rows:")
print(df.head(3))
print("\n Display 'name' and 'score' columns:")
print(df[['name', 'score']])
print("\n Students who scored more than 15:")
print(df[df['score'] > 15])
print("\n Students who attemped more than 2 times:")
print(df[df['attempts'] > 2])
print("\n Rows where score is missing (NaN):")
print(df[df['score'].isnull()])
print("\n Fill missing scores with the mean:")
df['score'].fillna(df['score'].mean(), inplace=True)
print(df)