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
        "Alter": 9,
        "Hobbies": ["Reiten", "Spielen"],
}

n = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
primes = {2, 3, 4, 7}

primes.add(11)  # Element wird hinzugefuegt (solange nicht vorhanden)
# .add veraendert den set

x = n.intersection(primes)
# gibt set zurueck mit Elementen, die in beiden sets vorkommen

n.intersection_update(primes)
# Vergleichbar mit:
# y = n.intersection(primes)
# n = y

y = n.difference(primes)
# gibt set zurueck mit Elementen, die nur in "n" vorkommt

n.difference_update(primes)
# Vergleichbar mit:
# y = n.difference(primes)
# n = y

buch = {
        "Titel": "Call of the wild",
        "Autor": "J.R.R.Tolkien",
        "ISBN": 112358132144,
        "Preis": "22.50 CHF",
}

buch["Erscheinungsjahr"] = 1980  # wird ueberschrieben
print(buch["Titel"])

zahl = buch.get("Seitenzahl", 0)

zahl1 = input("1. Zahl: ")

start = 0
stop = 6
step = 1
range(stop) == range(0, stop, 1)
range(start, stop) == range(start, stop, 1)
range(start, stop, step)
