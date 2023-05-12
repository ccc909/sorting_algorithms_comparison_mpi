import time
import random
import matplotlib.pyplot as plt
import tikzplotlib
from memory_profiler import memory_usage
import latextable
import texttable
from tqdm import tqdm
from sorting_techniques import pysort

sortObj = pysort.Sorting()


def generateRandom(n, x, y):
    return [random.randint(x, y) for _ in range(n)]

def generateSorted(n, x, y):
    return sorted(generateRandom(n, x, y))

def generateUniform(n, x, y):
    num = random.randint(x, y)
    return [num] * n


def sortmem(alg, l):
    mem_usage = max(memory_usage((alg, (l,), {}),interval=0.01))
    n = alg(l)
    return mem_usage

def sortTime(alg, l):
    start = time.time()
    n = alg(l)
    end = time.time()
    return end - start

def run(alg, genfunc, n, len1, x, y,memflag):
    total = 0
    for i in tqdm(range(n), desc=f"Running {alg.__name__}"):
        l = genfunc(len1, x, y)
        if memflag:
            tmp=sortmem(alg,l)
        else:
            tmp= sortTime(alg, l)
        total += tmp
    return total / n

bruh=[]
def plot(alg, genfunc, n, points, x, y,memflag):
    exectimes = []
    for len1 in points:
        avg=run(alg, genfunc, n, len1, x, y,memflag)
        exectimes.append(avg)
    bruh.append(exectimes)
    plt.plot(points, exectimes, label=alg.__name__)


if __name__ == '__main__':
    mem=0 #set to 0 to benchmark memory and 1 to benchmark time
    n = 1 #number of samples to generate a inmput at a point
    points = [1000,2000] #input array sizes at which to test the sorting algorithms
    x = 1 #lower bound for numbers to be generated
    y = 1000 #upper bound for nums to be generated
    table = texttable.Texttable()

    #all sorting algs available, remove as needed
    objs = [sortObj.bubbleSort,sortObj.insertionSort,sortObj.selectionSort,sortObj.heapSort,sortObj.msort4,sortObj.radixSort,sortObj.quicksort,sorted]


    names = ['elements'] + [x.__name__.replace("Sort","") for x in objs] #generating of list for latex table

    #choose whether to run on random, sorted or uniform list by uncommenting the selected line

    for kk in objs:
        plot(kk, generateRandom, n, points, x, y,mem)
        # plot(kk, generateSorted, n, points, x, y)
        # plot(kk, generateUniform, n, points, x, y)
    rotated = list(map(list,zip(*bruh))) #rotate matrix so it can be added to a table as rows
    i=0
    for n in rotated:
        n.insert(0,points[i]) #insert list size before each row
        i+=1
    rotated.insert(0,names) #insert header row
    table.add_rows(rotated) #add rows
    print(latextable.draw_latex(table)) #print table as latex


    plt.xlabel('List Length')
    plt.ylabel('Average Execution Time (s)')
    plt.legend() #remove if no legend needed
    tikzplotlib.save("test.tex") #save latex graph output equivalent to table to file
