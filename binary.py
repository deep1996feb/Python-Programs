#Write a program for binary search

pos = -1
def search(list, n):
    l = 0                 #lower bound
    u = len(list)-1       #upper bound

    while l<=u:
        mid = (l + u) // 2
    
        if list[mid] == n:
            globals()['pos'] = mid
            return True

        else:
            if list[mid] < n:
                l = mid;
            else:
                u = mid;

list = [4, 7, 8, 12, 45, 99, 102, 145, 183, 202]
n = 183
if search(list, n):
    print("Found at", pos+1)
else:
    print("Not found")
