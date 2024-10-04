import pandas as pd
from datetime import datetime
pd.set_option('display.max_colwidth', None)

jeopardy_csv = pd.read_csv("c:/Users/Admin/Desktop/Py_project_AI/pandas/This_Is_Jeopardy/jeopardy.csv").rename(columns={' Answer':'answer',
                                                                                                                        ' Air Date': 'air_date',
                                                                                                                            ' Question': 'question',
                                                                                                                            ' Value':'value'})

def value_to_float(x):
    return None if x is None or x == 'no value' else float(x.replace('$', '').replace(',', ''))

def str_to_date(x):
    return datetime.strptime(x,'%Y-%m-%d')

def answer_counts(data):
    return data['answer'].value_counts()


jeopardy_csv['value'] = jeopardy_csv.value.apply(value_to_float)
jeopardy_csv['air_date'] = jeopardy_csv.air_date.apply(str_to_date)

def find_words_in_question(words,df):
    
    filter = lambda x: all(word.lower() in x.lower() for word in words)  # noqa: E731, F841
    
    return df.loc[df['question'].apply(filter)]
 

def compare(data,date,words):
    date = str_to_date(date)
    data_before = data[data.air_date<date]
    data_after = data[data.air_date>date]
    x = find_words_in_question(words,data_before)
    y = find_words_in_question(words,data_after)
    return f'words :"{words}" was used: {len(x)} times before {date.year}-{str(date.month).rjust(2,'0')}-{date.day}, and {len(y)} times after '
    

print(round(jeopardy_csv.value.mean(),2))
filtered = find_words_in_question(['King'],jeopardy_csv)
print(answer_counts(filtered))

print(find_words_in_question(['A silent movie title includes the last name of this 18th c'],jeopardy_csv))
print()
print()
print(compare(jeopardy_csv,'2004-01-01',['computer','King']))