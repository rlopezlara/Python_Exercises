'''
create an empty array 3x3       
'''

rows = 3
columns = 3

matriz = []

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(0)
    matriz.append(row)

print(matriz)
print("-----------------------")

for row in matriz:
    print(row)