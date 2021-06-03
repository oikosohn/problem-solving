# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

size = int(input())
numbers = list(map(int, input().split()))

# selection sort
for i in range(size-1):
    min_idx = i
    # from sorted value to length of list
    for j in range(i+1, size):
        # if numbers[j] is smaller than numbers[min_idx]
        if numbers[j] < numbers[min_idx]:
            # swap idx, set min_idx on j
            min_idx = j
    # swap values
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    
def median(numbers, size):
    if size % 2 == 0:
        return (numbers[size//2-1]+numbers[size//2])/2
    else:
        return numbers[size//2]
    
def mode(numbers, size):
    max_num = numbers[-1]
    tmp = [0]*(max_num+1)
    for i in numbers:
        tmp[i] += 1
    return tmp.index(max(tmp))
            
med = median(numbers, size)
mod2 = mode(numbers, size)

print(sum(numbers)/size)
print(med)
# cnt = Counter(numbers)
# print(cnt.most_common(1)[0][0])
print(mod2)
