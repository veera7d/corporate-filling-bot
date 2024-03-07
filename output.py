#read ind_nifty500list.csv

import os
import time

#read ind_nifty500list.csv
nifty500 =open("ind_nifty500list.csv", "r").read()

# read CF-AN-equities-25-02-2024-to-03-03-2024.csv
corporate_actions=open("CF-AN-equities.csv", "r").read()

nifty500 = nifty500.split("\n")
corporate_actions=corporate_actions.split("\n")
heading = corporate_actions[0]
nifty500 = nifty500[1:]
corporate_actions = corporate_actions[1:]
nifty_500_symbols = []
for i in nifty500:
    nifty_500_symbols.append(i.split(",")[2].strip())
#print(nifty_500_symbols)

corporate_actions_symbols = []
for i in corporate_actions:
    corporate_actions_symbols.append(i.split(",")[0].split('"')[1].strip())
# print(corporate_actions_symbols)
out=[]
for i in heading.split(","):
    print(i,end=" ")
for i in nifty_500_symbols:
    for j in corporate_actions:
        if(j.split(",")[0].split('"')[1].strip() == i):
            print(j)
            out.append(j)
        #print("----------------------------------------")
#print(out)
