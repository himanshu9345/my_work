# import pandas as pd
# df = pd.read_csv("/home/spaceman/my_work/Most-Recent-Cohorts-Scorecard-Elements.csv")
# df=df[['STABBR']]
# print df['STABBR'].value_counts(normalize=True)
import random

all = ['a', 'b', 'c']
letters = dict(
    a = {1:'q', 2:'w', 3:'e'},
    b = {1:'f', 2:'g', 3:'h'},
    c = {1:'s', 2:'d', 3:'f'}
)


choice = input("enter a, b, or c: ")
randomVar = random.randint(1, 3)
answer = letters[str(choice)][randomVar] # this is the line in question
print(answer)