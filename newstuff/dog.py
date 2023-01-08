s = "dog"
t = "edgo"
z='a'
arr = [0] * len(t)

for i in range(len(s)):
    for j in range(len(t)):
        if (s[i]==t[j]):
            arr[j]=arr[j]+1

for i in range(len(arr)):
    if (arr[i]!=1):
        print(t[i])

 