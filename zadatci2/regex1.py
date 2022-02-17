import re

primjer = re.match('Umjetna',r'Umjetna inteligencija')
print(primjer)
print(primjer.group(0))

primjer = re.search('igra',r'Marko igra nogomet')
print(primjer)
print(primjer.group(0))

primjer = re.findall('igra',r'Marko igra nogomet. On igra u obrani.')
print(primjer)

primjer = re.sub('abc', 'bca', 'abcdesf')
print(primjer)

str = r'Marko igra nogomet'
x = re.findall(r"met\b", str)
print(x)

str = "2021 godina je završila prije 2 mjeseca."
x = re.findall("\d", str)
print(x)

str = "2021 godina je završila prije 2 mjeseca."
x = re.findall("\d+", str)
print(x)

str = "2021 godina je završila prije 2 mjeseca."
x = re.findall("\D", str)
print(x)

x = re.findall("\D+", str)
print(x)

str = "2021 godina je završila prije _2 mjeseca."
x = re.findall("\w+",str)
print(x)

str = "2021 godina je završila prije _2 mjeseca."
x = re.findall("\W", str)
print(x)

str = "2021 godina je završila prije _2 mjeseca."
x = re.findall("\s", str)
print(x)

str = "2021 godina je završila prije _2 mjeseca."
x = re.findall("\S", str)
print(x)


str = "Marko igra nogomet!"
x = re.findall("go.", str)           
x2 = re.findall("go...", str)
print(x)
print(x2)

str = "Marko igra nogomet!"
x = re.findall(".go", str)           
x2 = re.findall("..go", str)
print(x)
print(x2)

str = "Umjetna inteligencija"
x = re.findall("^Umj", str)
print(x)

str = "Umjetna inteligencija"
x = re.findall("cija$", str)
print(x)

str = "Ivan Ivana Ivano"
x = re.findall("Ip*", str)
print(x)

x = re.findall("Ip+", str)
print(x)

str = "Marko igra nogomet"
x = re.findall("igr|marko", str)
print(x)

print(re.split('\s','Marko igra nogomet'))
