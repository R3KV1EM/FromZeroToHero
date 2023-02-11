new_list = ['a', 'b', 'c']
print(new_list[1]) #here print b
print(new_list[-2]) #here print b
print(new_list[1:3]) # here print b c
new_list[0] = 'z'
print(new_list) #here print z b c

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list) # z 2 3
print(bonus) # z 2 3 5
