# %%

arr = []
flag = True
for l in open("insurance.csv", "rt"):
    if flag:
        flag = False
        continue
    arr.append(float(l.split(",")[0]))

sum(arr)/len(arr)

# %%
arr.sort()

i = len(arr) // 2
if len(arr) % 2 == 0: # EVEN
    print((arr[i - 1] + arr[i])/2)
else:
    print(arr[i])

# %%
10 / 2

# %%
