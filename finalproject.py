#Import Stuff

import pandas as pd
import numpy as np
import time
from sklearn.metrics.pairwise import cosine_similarity

#Import Data Frames (Do I really need this?)
matrix_rates = pd.read_csv('/Users/carolinasantoscarneiro/Documents/spiced_practice/SPICED/week11/matrix_rates.csv')
matrix_rates.set_index('users', inplace=True)

matrix_tl = pd.read_csv('/Users/carolinasantoscarneiro/Documents/spiced_practice/SPICED/week11/matrix_tl.csv')
matrix_tl.set_index('users', inplace=True)

#STEP 1
# I want my code to receive a new user through an input function:
# this will generate a dictionary where input value, key will be put into a dataframe

#Taking the inputs to generate a dict with skills and ratings for the 1st matrix
print('\nHello! Shall we find a good learning/teaching partner for you?')

time.sleep(3)

a = input(f'\nPlease, from the list, give me 5 skills you would want to learn or teach: \n\n').lower()
b = input(f'\n').lower()
c = input(f'\n').lower()
d = input(f'\n').lower()
e = input(f'\n').lower()

f = input(f'\nPlease, tell me, from 1 to 5, how you rate yourself in {a}: \n')
g = input(f'{b}: \n')
h = input(f'{c}: \n')
i = input(f'{d}: \n')
j = input(f'{e}: \n')

skills_tl = {a.lower(): float(f), b.lower(): float(g), c.lower(): float(h), d.lower(): float(i), e.lower(): float(j)}

# Putting the dict into the matrix.
template = dict(zip(matrix_rates.columns, np.zeros((len(matrix_rates.columns),))))

for key, value in skills_tl.items():
    template[key] = value

matrix_rates.loc[10000] = template
new_user = matrix_rates.loc[10000]

#Taking a new dict with skills, t or l for the second matrix.
print('\nNow I would like to know if you want to teach or learn each skill.\n')

time.sleep(3)

k = input(f'Would you like to learn or teach {a}? \n')
l = input(f'Would you like to learn or teach {b}? \n')
m = input(f'Would you like to learn or teach {c}? \n')
n = input(f'Would you like to learn or teach {d}? \n')
o = input(f'Would you like to learn or teach {e}? \n')

skills_lot = {a.lower():float(k),b.lower():float(l),c.lower():float(m),d.lower():float(n),e.lower():float(o)}

#Putting it into the matrix.
template1 = dict(zip(matrix_tl.columns, np.zeros((len(matrix_tl.columns),))))

for key, value in skills_lot.items():
    template1[key] = value

matrix_tl.loc[10000] = template1
new_user1 = matrix_tl.loc[10000]

#Generating cosine simimilarity from all users against all users.
df1 = pd.DataFrame(cosine_similarity(matrix_rates), index=matrix_rates.index, columns=matrix_rates.index)

#Taking a sorted list of the 10 highest cosine similarities from the new user with others.
cosim = dict(list(enumerate(df1.iloc[-1])))
sorted_dict = {key : value for key, value in sorted(cosim.items(), key=lambda item: item[1], reverse=True)}
top_10 = list(sorted_dict.keys())
top_10 = top_10[1:10]
print(f'\nThese are the most similar users to you: {top_10}\n')

#What things the most similar user wants to teach and what things they want to learn.
dict_teaching = dict(matrix_tl.iloc[top_10[0]] > 0)
dict_learning = dict(matrix_tl.iloc[top_10[0]] < 0)

for k, v in dict_teaching.items():
    if v == True: #and k not in skills_lot.values()<0:
        print(f"\nYou can learn {k.upper()} from {top_10[0]}!\n")

for k, v in dict_learning.items():
    if v == True:
        print(f"\nYou can teach {k.upper()} to {top_10[0]}!\n")
