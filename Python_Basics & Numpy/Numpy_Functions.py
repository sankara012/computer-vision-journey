#Dealing with the python array
import array as arr;
a = arr.array('i',[10,5,7,7,7,7,2,4])
a.insert(2,100)
a.extend([10,9,45])
print(*a)
a.pop(7)
c = a[5:]
print(*c)
print(f"7 is found at index {a.index(7)}")
count = a.count(7)
print(f"the number of 7 into the array is {count}")

a.reverse()
print(f"the reversed of the array is {a}")