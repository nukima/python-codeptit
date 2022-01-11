from collections import defaultdict
import array
def mostFrequent(arr, n):
    arr.sort()
    max_count = 1; res = arr[0]; curr_count = 1
    cnt = 1
    for i in range(1, n):
        if (arr[i] == arr[i - 1]):
            curr_count += 1
             
        else :
            if (curr_count > max_count):
                max_count = curr_count
                res = arr[i - 1]
            curr_count = 1
 
    if (curr_count > max_count):
        max_count = curr_count
        res = arr[n - 1]
    
    if(max_count <= int(n/2)):
        print("NO")
    else:
        print(res)
def sortByFreq(a, n):
    mostFrequent(a,n)

if __name__ == "__main__":
    t=int(input())
    while(t!=0):
        n = int(input())
        lst = input().split()
        lst = list(map(lambda x: int(x) if x.isdigit() else 0, lst))
        sortByFreq(lst, n)
        t -= 1