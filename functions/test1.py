#import pandas as pd
'''file = open("qwerty.txt", "w")
file.write("./check_pylint.sh")
file.close()

file = open("qwerty.txt", "r")
print(file.read())
file.close()

file = open("kavya.txt", "a")
file.write("this is append mode")
file.close()

file=open("keerthi.txt","w")
file.write("Hellooo everyoneee")
file.close()

file=open("keerthi.txt","r")
print(file.read())
file.close()

#with open(r"path of the readable file", "r") as f:
#   print(f.read())
#with open(r"path of the readable file", "w") as f:
#    f.write("this is write mode by akash")'''

import pandas as pd
path=r"C:\COLLEGE NOTES\house-prices.csv"
data=pd.read_csv(path)
print(data)
print(data.head())
print(data.tail())
print(data.describe())
print(data.info)