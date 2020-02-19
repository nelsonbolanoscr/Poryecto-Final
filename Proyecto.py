#Proyecto Final
#Autor Nelson Bolaños

import pandas as pd
from os import listdir
import csv

files = listdir("C:/Users/NelsonEnriqueBolanos/Desktop/Python/Proyecto")

with open('C:/Users/NelsonEnriqueBolanos/Desktop/Python/Move/testfinal.csv', 'w') as x:
    write = csv.writer(x)

    for i in files:
        print(i)
        with open('C:/Users/NelsonEnriqueBolanos/Desktop/Python/Proyecto/' + str(i)) as f:
            reader = csv.reader(f)
            test = list(reader)
            print(test)
        with open('C:/Users/NelsonEnriqueBolanos/Desktop/Python/Proyecto/Move/testfinal.csv', 'a', newline='') as p:
            writer = csv.writer(p)
            test2 = [
                [test]
            ]
