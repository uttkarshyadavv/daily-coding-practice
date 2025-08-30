arr=[900,940,950,1100,1500,1800]
dept=[910,1200,1120,1130,1900,2000]
trains = list(zip(arr, dept))
trains.sort(key=lambda x: x[0])   # sort by arrival
print(trains)
atplatform=[]
n=len(trains)
platform=1
for i in range(0,n-1):
    atplatform.append(trains[i])
    for j in range(len(atplatform)):
        if atplatform[j][1] < trains[i+1][0]:
            atplatform.pop(j)
            break
    else:
        platform+=1
print(platform)


