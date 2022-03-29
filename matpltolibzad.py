import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 3))

wybory = ["CDU/CSU",
          "SPD",
          "Greens",
          "FDP",
          "AfD",
          "Left Party",
          "Others"]

glosy = [241,257,148,115,103,49,86]

plt.pie(glosy, autopct='%1.2f%%', labels=wybory)


ax.legend(wybory,
          title="PKB krajów Unii Europejskiej 2016",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()
plt.close()

panstwa = ["Niemcy", "Francja", "Włochy", "Hiszpania", "Polska", "Rumunia","Holandia","Belgia","Grecja","Czechy","Portugalia","Szwecja","Węgry","Austria","Bułgaria","Dania","Finlandia","Słowacja","Irlanda","Chrowacja","Litwa","Słowenia","Łotwa","Estonia","Cypr","Luksemburg","Malta"]
PKB = [3134070, 2228857,1672438,1113851,424269,169578,697219,421611,175888,174412,184931,462057,112399,349344,47364,276805,214062,80958,265835,45557,38637,39769,25021,20916,17901,54195,9898]

plt.figure(figsize=(30, 3))  # width:20, height:3
plt.bar(panstwa, PKB, width=0.5)
plt.subplots_adjust(left=0.05,right=0.99)
plt.show()




ax.set_title("PKB w mln euro")