#python code for functions


#making a function
def most_frequent(word):
    dictionary={}
    for i in word:
        if i not in dictionary:
            dictionary[i]=word.count(i)
    return dictionary

    
#getting output for the word mississippi
a=most_frequent('mississippi')
b={}

#sorting and adding the sorted values in new dictionary
for j in sorted(a.values(),reverse=True):
    for i in a:
        if a[i]!=j:
            continue
        else:
            b[i]=j

#output dictionary showing letters in decreasing order of frequency    
print(b)

