import re

list_of_inputs = []
with open('input.txt', 'r') as file:
    list_of_inputs = file.readlines()

print(list_of_inputs)

list_of_words = []
for a in list_of_inputs:
    temp = a.split()
    for b in temp:
        list_of_words.append(b)

print(list_of_words)

reserved_words = ['if', 'else', 'switch', 'case', 'default', 'break', 'int', 'float', 'char', 'double', 'long', 'for',
                'while', 'do', 'void', 'goto', 'auto', 'signed', 'const', 'extern', 'register', 'unsigned', 'return',
                'continue', 'enum', 'sizeof', 'struct', 'typedef', 'others', 'union', 'volatile']

keywords = [] # results 1
identifiers = []
id_pattern = "[a-z]+[A-Z]*[0-9]*(;|,)*"
mat_ops = ['=', '+', '-', '*', '/', '%', '++', '--']
math_operators = [] # results 3
log_ops = ['==', '!=', '>', '>=', '<', '<=', '&&', '||', '!']
logical_ops = [] # results 4
num_val = "^(\d*\.)?\d+$"
numerical_vals = []  # results 5
others = [',', ';', '(', ')', '{', '[', ']']

for i in list_of_words:
    if i in reserved_words:
        keywords.append(i)
    if re.search(id_pattern, i):
        if i not in identifiers and i not in keywords:
            identifiers.append(i)
    for j in mat_ops:
        if (j in i) and (j not in math_operators):
            math_operators.append(j)
    for k in log_ops:
        if (k in i) and (k not in logical_ops):
            logical_ops.append(k)

    m = i.strip(';,]})')
    if re.search(num_val, m) and m not in numerical_vals:
        numerical_vals.append(m)



identifiers_groomed = [] # results 2
for i in identifiers:
    j = i.strip(';,]})')
    if j not in identifiers_groomed:
        identifiers_groomed.append(j)


print(numerical_vals)





