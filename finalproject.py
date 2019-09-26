#Import Stuff
import pandas as pd
import numpy as np
import time
from sklearn.metrics.pairwise import cosine_similarity

#Import Data Frames (Do I really need this?)

# MATRIX_RATES = pd.read_csv('matrix_rates.csv')
# MATRIX_RATES.set_index('users', inplace=True)
#
# MATRIX_TL = pd.read_csv('matrix_tl.csv')
# MATRIX_TL.set_index('users', inplace=True)

#STEP 1
# I want my code to receive a new user through an input function:
# this will generate a dictionary where input value, key will be put into a dataframe

#Taking the inputs to generate a dict with skills and ratings for the 1st matrix
#def do_everything():
#return '\nHello! Shall we find a good learning/teaching partner for you?'

# time.sleep(3)
def do_everything():
    MATRIX_RATES = pd.read_csv('/Users/carolinasantoscarneiro/Desktop/final/matrix_rates.csv')
    MATRIX_RATES.set_index('users', inplace=True)

    MATRIX_TL = pd.read_csv('/Users/carolinasantoscarneiro/Desktop/final/matrix_tl.csv')
    MATRIX_TL.set_index('users', inplace=True)
    # user_id = input
    # a,b,c,d,e = input
    a, b, c, d, e = 'german', 'french', 'python', 'javascript', 'sewing'
    # a = input(f'\nPlease, from the list, give me 5 skills you would want to learn or teach: \n\n').lower()
    # b = input(f'\n').lower()
    # c = input(f'\n').lower()
    # d = input(f'\n').lower()
    # e = input(f'\n').lower()

    f, g, h, i, j = 1, 3, 4, 5, 1
    # f = input(f'\nPlease, tell me, from 1 to 5, how you rate yourself in {a}: \n')
    # g = input(f'{b}: \n')
    # h = input(f'{c}: \n')
    # i = input(f'{d}: \n')
    # j = input(f'{e}: \n')

    skills_dict = {a.lower(): float(f), b.lower(): float(g), c.lower(): float(h), d.lower(): float(i), e.lower(): float(j)}

    print('\nNow I would like to know if you want to teach or learn each skill.\n')
    # time.sleep(3)
    k, l, m, n, o = -1, 1, -1, 1, -1
    # k = input(f'Would you like to learn or teach {a}? \n')
    # l = input(f'Would you like to learn or teach {b}? \n')
    # m = input(f'Would you like to learn or teach {c}? \n')
    # n = input(f'Would you like to learn or teach {d}? \n')
    # o = input(f'Would you like to learn or teach {e}? \n')
    teach_learn_dict = {a.lower():float(k),b.lower():float(l),c.lower():float(m),d.lower():float(n),e.lower():float(o)}


    # return skills_dict, teach_learn_dict

    # Putting the dict into the matrix.
    # def dict_to_matrix(skills_dict, teach_learn_dict):

    skills_template = dict(zip(MATRIX_RATES.columns, np.zeros((len(MATRIX_RATES.columns),))))

    for key, value in skills_dict.items():
        skills_template[key] = value

    MATRIX_RATES.loc[-1] = skills_template

    tl_template = dict(zip(MATRIX_TL.columns, np.zeros((len(MATRIX_TL.columns),))))

    for key, value in teach_learn_dict.items():
        tl_template[key] = value

    MATRIX_TL.loc[-1] = tl_template


    # new_user1 = MATRIX_TL.loc[10000]
    # new_user = MATRIX_RATES.loc[10000]

    #Taking a new dict with skills, t or l for the second matrix.
    # def generate_dict_two():
    #     print('\nNow I would like to know if you want to teach or learn each skill.\n')

    # time.sleep(3)

    #     k = input(f'Would you like to learn or teach {a}? \n')
    #     l = input(f'Would you like to learn or teach {b}? \n')
    #     m = input(f'Would you like to learn or teach {c}? \n')
    #     n = input(f'Would you like to learn or teach {d}? \n')
    #     o = input(f'Would you like to learn or teach {e}? \n')

    #     skills_lot = {a.lower():float(k),b.lower():float(l),c.lower():float(m),d.lower():float(n),e.lower():float(o)}

    #Putting it into the matrix.

    #Generating cosine simimilarity from all users against all users.
    # def df_cosim_all():
    df1 = pd.DataFrame(cosine_similarity(MATRIX_RATES), index=MATRIX_RATES.index, columns=MATRIX_RATES.index)
    # return df1
    #Taking a sorted list of the 10 highest cosine similarities from the new user with others.
    # gen_top_ten_list(df1):
    cosim = dict(list(enumerate(df1.iloc[-1])))
    sorted_dict = {key : value for key, value in sorted(cosim.items(), key=lambda item: item[1], reverse=True)}
    top_10 = list(sorted_dict.keys())
    top_10 = top_10[1:10]
    print(f'\nThese are the most similar users to you: {top_10}\n')
    # return top_10

    #What things the most similar user wants to teach and what things they want to learn.
    # def most_similar_t_l(top_10):

    t_nw = []
    for k, v in dict(MATRIX_TL.iloc[-1] > 0).items():
        if v == True:
            t_nw.append(k)
            # print(f"New user wants to teach {t_nw}")
    t_nw
    l_nw = []
    for k, v in dict(MATRIX_TL.iloc[-1] < 0).items():
        if v == True:
            l_nw.append(k)
    l_nw
            # print(f"New user wants to learn {l_nw}")
    #
    # t_u = []
    # for k, v in dict(MATRIX_TL.iloc[top_10[0]] > 0).items():
    #     if v == True:
    #         t_nw.append(k)
    #         print(f"Top user wants to teach {t_nw}")
    #
    # l_u = []
    # for k, v in dict(MATRIX_TL.iloc[top_10[0]] < 0).items():
    #     if v == True:
    #         l_nw.append(k)
    #         print(f"Top user wants to learn {l_nw}")

    learn = {}
    teach = {}
    for i in top_10:

        dict_teaching = dict(MATRIX_TL.iloc[i] > 0)
        dict_learning = dict(MATRIX_TL.iloc[i] < 0)

        l1 = []
        for k, v in dict_teaching.items():
            if v == True and k in l_nw:
                l1.append(k.upper())

        l2 = []
        for k, v in dict_learning.items():
            if v == True and k in t_nw:
                l2.append(k.upper())

        learn[i] = l1
        teach[i] = l2

    data = {}
    data['learn'] = learn
    data['teach'] = teach

    return data
# def call_me():
#     d1, d2 = generate_dictionaries()
#     dict_to_matrix(d1, d2)
#     df1 = df_cosim_all()
#     top_10 = gen_top_ten_list(df1)
#     most_similar_t_l(top_10)
#     words = 'some words'
#     return words
# l_nw = []
# for k, v in dict(MATRIX_TL.iloc[-1] > 0).items():
#     if v == True:
#         l_nw.append(k)
#
# t_nw = []
# for k, v in dict(MATRIX_TL.iloc[-1] < 0).items():
#     if v == True:
#         t_nw.append(k)

# dict_to_matrix_one()
# generate_dict_two()
# dict_to_matrix_two()
# df_cosim_all()
# gen_top_ten_list()
# most_similar_t_l()
# if __name__ == '__main__':
#     d1, d2 = generate_dictionaries()
#     dict_to_matrix(d1, d2)
#     df1 = df_cosim_all()
#     top_10 = gen_top_ten_list(df1)
#     most_similar_t_l(top_10)
