"""
Unpacking list
"""

listx = ['Dani', 'John', "Maria", 1, 2, 3]
n1, n2, *otherlist, last = listx

print(n1, n2, otherlist, last)
