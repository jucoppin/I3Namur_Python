# https://regex101.com/
# https://regex101.com/r/pVHSjB/1
"""
\d => digit => 0-9
[0-9]
\s => Any whitespace
. => N'importe quel char
a => Juste a
abcdefg => Chaîne abcdefg

() => Groupements
[] => Une valeur dans la range
[a-z] => Une lettre en miniscule
[A-Z] => Une lettre en majuscule
[a-zA-Z]
[a-zA-Z0-9]

Quantifier
? => 0-1
* => 0-n
+ => 1-n
{min,max}  => {1, 3} => de 1 à 3 
{equal}    => {2}    => exactement 2
pomme[s]+ => pommesssssssssssssssssssssssssssssssssssssss

pomme
pommes
min s : 0
max s : 1
regex : pomme[s]{?}
"""

"""
format adresse email : char@char.char
char1 :
    min : 1
    max : n
"""

"""
[a-zA-Z]{,8}
MotDePasse
\d+-\d+-\d+
2021-12-01
\d+/\d+/\d+
\d{2}/\d{2}/\d{4}
01/01/2015
12345678/12345678/39282055580155
\d+
012331255
\d{2}\.\d{2}\.\d{2}-\d{3}\.\d{2}
01.01.01-123.11
[a-zA-Z.\-_+\d]+@[a-zA-Z.]+\.[a-zA-Z]+
julien.coppin@bstorm.be
julien.coppin_42@bstorm.be
julien.coppin@fr.bstorm.be

pomme[s]?
pomme
pommes
pommesssssss
(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{8,}
Pomme123

N_\d{4}_[A-Z]\d{2}[a-z]{2}
N_2020_E12ab
N_2021_E89mn

Explications :
N_
ANNEE_
E
2 chiffres
2 lettres miniscules
"""
import re
text = input("Texte : ")
# <re.Match object; span=(0, 12), match='N_2020_E12ab'>
PATTERN = r"N_\d{4}_[A-Z]\d{2}[a-z]{2}"
print(re.match(PATTERN, text)) # "N_2020_E12ab"
# Soit un object contenant la réponse ou None si pas trouvé