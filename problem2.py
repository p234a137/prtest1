import sys
from collections import Counter
import pandas

def EditDistance(s1, s2):
    if s1 == s2:
        return 0
    elif len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)
    else:
        return min(
            EditDistance(s1[:-1], s2[:-1]) + (s1[-1] != s2[-1]),
            EditDistance(s1[:-1], s2)+1,
            EditDistance(s2, s2[:-1])+1
        )

def EditMatrix(source, target):
    vowels = "aeiouAEIOU"
    # initialize everything to zero
    eMatrix = [[0 for i2 in range(0,len(target)+1)] for i1 in range(0,len(source)+1)]
    # fill 0th columns and row
    for i1 in range(1,len(source)):
        eMatrix[i1][0] = i1
    for i2 in range(1,len(target)):
        eMatrix[0][i2] = i2
    # fill rest
    for i2 in range(1,len(target)):
        for i1 in range(1,len(source)):
            if source[i1] == target[i2]:
                eMatrix[i1][i2] = eMatrix[i1-1][i2-1] # no operation
            else:
                # calculate the different costs
                deletion_cost = eMatrix[i1-1][i2] + 2.
                insertion_cost = eMatrix[i1][i2-1] + 3.
                e1 = source[i1-1]
                e2 = target[i2-1]
                if e1 in vowels and e2 in vowels:
                    replacement_cost = eMatrix[i1-1][i2-1] + 0.5
                else:
                    replacement_cost = eMatrix[i1-1][i2-1] + 1.
                #
                costs = [replacement_cost, deletion_cost, insertion_cost]
                icost = costs.index(min(costs))
                if icost == 0:
                    #print "replacing"
                    eMatrix[i1][i2] = insertion_cost
                elif icost == 1:
                    #print "deleting"
                    eMatrix[i1][i2] = deletion_cost
                else: # could check here more just to make sure icost does not go crazy
                    #print "inserting"
                    eMatrix[i1][i2] = replacement_cost

                # eMatrix[i1][i2] = min(
                #     eMatrix[i1-1][i2] + 1, # deletion
                #     eMatrix[i1][i2-1] + 1, # insertion
                #     eMatrix[i1-1][i2-1] + 1 # replacement
                #)

    #return eMatrix[len(source)-1][len(target)-1]
    return eMatrix


# get file name from arguments and open file
string1 = sys.argv[1]
string2 = sys.argv[2]
print "the strings:", string1,",", string2
#allowed = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

print EditDistance(string1, string2)
EM = EditMatrix(string1, string2)
#df = pandas.DataFrame(EditMatrix(string1, string2))
cols=list(string2)
cols.insert(0,"-")
rows = list(string1)
rows.insert(0,"-")
df = pandas.DataFrame(EM, columns = cols)
df['*'] = rows
print df
print EM[len(string1)-1][len(string2)-1]