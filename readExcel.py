import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import os
import time

#                               STWORZ PLIK

if os.path.exists('excel.xlsx'):
    pass
else:
    open('excel.xlsx', 'a').close()
path = "excel.xlsx"

#                               TABELE

imie = np.array(["Tomasz", "Bartosz", "Marcel", "Łukasz", "Tymek","Oskar","Sebastian","Damian","Krystyna","Julia","Sylwia","Kasia","Monika"])
nazwisko = np.array(["Kurdel", "Strychacz", "Nowak","Stolka","Jęczarek","Odwojak","Kowal","Pasień","Rydza"])
srednie = np.array([])
dane = np.array([])

#                               UZUPELNIANIE TABEL

for i in range(10):
    dane = np.append(dane, random.choice(imie) + " " + random.choice(nazwisko))
    srednie = np.append(srednie, random.randint(100, 600)/100)

#                               TWORZENIE WAROSCI DLA EXCELA

writer = pd.ExcelWriter('excel.xlsx', engine='openpyxl') 
wb  = writer.book
df = pd.DataFrame({'Dane': dane, 'Średnie': srednie})
df.to_excel(writer)
wb.save('excel.xlsx')

#                              ZCZYWYANIE EXCELA

sheet = pd.read_excel(path)
dataSheet = pd.DataFrame(sheet, columns=['Dane', 'Średnie'])

#                               PRINT

print(dataSheet)

plt.figure(figsize=(30,3))
plt.bar(dataSheet['Dane'], dataSheet['Średnie'], width=0.5)
plt.subplots_adjust(left=0.05,right=0.99)
plt.title('Średnia na ucznia')
plt.show()

time.sleep(1)
writer.close()
os.remove(path)



