# fruits = []
# fruits = fruits + ['apple', 'pear', 'bannana']
# print(fruits)

import time
start = time.time()

fruits = [""]*3
fruits = ['apple', 'pear', 'banna']


fruits = []
fruits = fruits + ['apple', 'pear', 'bannana']

print(fruits)
end = time.time()
print((end-start) * 1000)