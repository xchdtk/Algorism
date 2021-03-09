alpha       = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
input_alpha = input() 

for i in alpha:
    input_alpha = input_alpha.replace(i, 'c')

print(len(input_alpha))
