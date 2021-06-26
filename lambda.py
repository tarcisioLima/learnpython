"""
Lambda function: anonymous because doesn't have a name
"""

a = lambda x, y: x * y

print(a(2,2))

listx = [
    ['P1', 13],
    ['P2', 2],
    ['P3', 50],
    ['P4', 7],
    ['P5', 22],
]

listx.sort(key=lambda item: item[1], reverse=True)
# or
ordered = sorted(listx, key=lambda i: i[1], reverse=True)

print(listx)
print(ordered)