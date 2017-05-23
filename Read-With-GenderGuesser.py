import string
from openpyxl import load_workbook
import gender_guesser.detector as gender

nameCounts = dict()
nameGenderDict = dict()

wb = load_workbook(filename='students roster-17S-ECON103 -WithGG.xlsx')
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


#    Using Gender Guesser
d = gender.Detector(case_sensitive=False)

for count, fName in lst:
    d.get_gender(fName)
    nameGenderDict[fName] = d.get_gender(fName)

print(nameGenderDict)

for cells in tuple(sheets.rows):
    if cells[0].value == 'Student':
        continue
    strFullName = cells[0].value
    strFullName = strFullName.lower()
    splitName = strFullName.split()
    try:
        genderVal = nameGenderDict[splitName[0]]
    except:
        genderVal = None
    if genderVal is not None:
        cells[4].value = genderVal

wb.save('students roster-17S-ECON103.xlsx')
