from tabulate import tabulate

table=[
    ['cesar mayta','cesarmayta@gmail.com','758963451'],
    ['cesar mayta','cesarmayta@gmail.com','758963451']
]
columns=['nombre','email','celular']
print(tabulate(table,headers=columns,tablefmt='grid'))
