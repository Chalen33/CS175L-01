import matplotlib.pyplot as plt
import numpy as np

    
def dataLists():
    mainList=[]
    names=[]
    cost=[]
    try:
        expenses= open('expenses.txt','r')
    except IOError:
        print('File not found')
    else:
        for line in expenses:
            line= line.strip('\n')
            mainList.append(line.split('\t'))
        for x in mainList:
            names.append(x[0])
            cost.append(x[1])
        expenses.close()
    return names,cost

def main():
    n,c= dataLists()
    plt.pie(c,labels=n)
    plt.show()

if __name__ == "__main__":
    main()
