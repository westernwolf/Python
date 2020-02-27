objekt = 0.9  # float
ct = int

id(objekt)

type(objekt)  # returns Type
isinstance(objekt, ct)  # checks if

string1 = "Ich bin ein String"
string2 = 'Ich bin auch ein String!'
string3 = """Ich bin ein
mehrzeiliger String."""
string4 = '''Ich bin auch ein mehrzeiliger String!'''

liste1 = [1, 1, 2, 3, 'vier']
liste2 = [liste1, 5, 'sechs']

tuple1 = (1, 1, 2, 3, 'vier')
tuple2 = 1, 1, 2, 3, 'vier'

zahl1, zahl2, zahl3, zahl4, string1 = liste1  # oder tupel

start = 0
end = 5
step = 1
x = "Slice"
slice = x[start: end: step]

x[:end:step] == x[0:end:step]
x[start::step] == x[start:0:step]
x[start:end] == x[start:end:1]

set1 = {1, 1, 2, 3, 'vier'}
set2 = frozenset(set1)


steckbrief = {
        "Vorname": "Pippi",
        "Nachname": "Langstrumpf",
        "Alter" : 9,
        "Hobbies": ["Reiten", "Spielen"],
}
