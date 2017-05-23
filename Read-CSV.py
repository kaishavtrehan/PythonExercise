import string
from openpyxl import load_workbook
import urllib.request
import json

nameCounts = dict()
nameGenderDict = dict()

wb = load_workbook(filename='students roster-17S-ECON103.xlsx')
sheets = wb['24_Feb_11-45_Grades-17S-ECON103']
for names in sheets['A']:
    if names.value == 'Student':
        continue
    strFullName = names.value.lower()
#   split first name
    firstName = strFullName.split()
#   Make dictionary of names
    nameCounts[firstName[0]] = nameCounts.get(firstName[0], 0)+1
#   print(firstName)

#   Print Dictionary
#   print(nameCounts)

lst = list()
for key, val in nameCounts.items():
    lst.append((val, key))
lst.sort(reverse=False)

#   Print List Size
#   print("List Size ",len(lst))


#   Using Gender-API
serviceurl = 'https://www.gender-api.com/get?'
servicekey = 'UlcyLptkYKgWZUYswt'


#   Try service with single name
#   uh = urllib.request.urlopen
#   ('https://www.gender-api.com/get?name=matthew&key=UlcyLptkYKgWZUYswt')
#   data = uh.read().decode()
#   js = json.loads(str(data))
#   print(js["name"],' ',js["gender"],' ',js["accuracy"])
#   nameGenderDict[js["name"]]=(js["gender"],js["accuracy"])
#   print(nameGenderDict)
#   Try service with single name


for count, fName in lst:
    url = serviceurl +
    urllib.parse.urlencode({'name': fName, 'key': servicekey})
    print('Retrieving', url, '\n')
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    js = json.loads(str(data))
    nameGenderDict[js["name"]] = (js["gender"], js["accuracy"])
    print(js["name"], ' ', js["gender"], ' ', js["accuracy"], '\n')

print(nameGenderDict)

for cells in tuple(sheets.rows):
    if cells[0].value == 'Student':
        continue
    strFullName = cells[0].value
    strFullName = strFullName.lower()
    splitName = strFullName.split()
    try:
        genderAccuracyPair = nameGenderDict[splitName[0]]
    except:
        genderAccuracyPair = None
    if genderAccuracyPair is not None:
        cells[4].value = genderAccuracyPair[0]
        cells[5].value = genderAccuracyPair[1]

wb.save('students roster-17S-ECON103.xlsx')
