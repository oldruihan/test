list_a = [1,2,3,4,5,6,7]
list_b = ["one","two","three"]
list_c = ['a','b','c']
list_d = [1,"one",'a',3.1415926]
list_e = list_a + list_d

print(list_a[0:-3])

print(8 not in list_a)
print([1,8] in list_a)
print(len(list_a))

list_f = list_a
list_a[0] = 10
print(list_f)