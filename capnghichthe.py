from collections import defaultdict

def sortByFreq(arr, n):
    cnt = 0
    for i in range (0,n):
        for j in range (i+1,n):
            if arr[i]>arr[j]:
                cnt+=1
    return cnt
 
# if __name__ == "__main__":
n = int(input())
lst = input().split()
lst = list(map(lambda x: int(x) if x.isdigit() else 0, lst))
solution = sortByFreq(lst, n)
print(solution)