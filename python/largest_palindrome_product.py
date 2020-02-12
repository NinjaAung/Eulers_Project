'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Palindrome:  A word or sequenc that is the same forward as it is backwards
'''

list_palid = []
for x in range(100,1000):
    for y in range(100,1000):
        if str(x*y)[::-1] == str(x*y):
            list_palid.append(x*y)
print(max(list_palid))            
