
## 99 bottles using while loop..

n = 99
while n > 0:
    print(n,"bottles of beer on the wall,","Take one down, pass it around,")
    n = n - 1
print('No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall…')


"""

# 99 bottles using for loop (range), if else condition...


for i in range(99, 0, -1):
        if i == 1:
                print('1 bottle of beer on the wall, 1 bottle of beer!')
                print('So take it down, pass it around, no more bottles of beer on the wall!')
        elif i == 2:
                print('2 more bottles of beer on the wall, 2 more bottles of beer!')
                print('So take one down, pass it around, 1 more bottle of beer on the wall!')
        else:
                print('{0} bottles of beer on the wall, {0} bottles of beer!'.format(i))
                print('So take it down, pass it around, {0} more bottles of beer on the wall!'.format(i - 1))
              
"""
