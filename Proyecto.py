#Proyecto Final
#Autor Nelson Bolaños

import pandas as pd
from os import listdir
import csv
import time

files = listdir("C:/Users/NelsonEnriqueBolanos/Desktop/Python/Proyecto")
master = pd.DataFrame(columns=['Date','Case Number','Agent','Note','Comment'])
l1 = ['Date','Case Number','Agent','Note','Comment']
d1 = {}

for i in files:
    with open('C:/Users/NelsonEnriqueBolanos/Desktop/Python/Proyecto/' + str(i)) as f:
        reader = csv.reader(f)
        for x in reader:
            time.sleep(1)
        for n in range(len(l1)):
            d1[l1[n]]=x[n]
        master = master.append(d1, ignore_index=True)

print(master)
with open('C:/Users/NelsonEnriqueBolanos/Desktop/Python/Move/testfinal.csv','a',newline='') as t:
    master.to_csv(t, index=False, header=False)

"""

    with open('C:/Users/NelsonEnriqueBolanos/Desktop/Python/Move/testfinal.csv', 'a', newline='') as p:
        writer = csv.writer(p)
        writer.writerow(df)

"""