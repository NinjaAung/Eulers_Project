import time
start_time = time.time()
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Notes:

3 or 5 of a X is valid, find valid x sum:

'''

def multiple_sum(loop):
    multiple = sum_of_multiples = 0
    for multiple in range(loop):
        if multiple%5==0 or multiple%3==0:
            sum_of_multiples += multiple
        else:
            # print(f"{multiple} is not a multiple of 3 and 5")
            pass
    return sum_of_multiples

#print(multiple_sum(1000))

'''
Or one liner
'''

print(sum(i for i in range(1000) if i%5 == 0 or i%3 == 0))
print(f"--- {time.time() - start_time} seconds ---")