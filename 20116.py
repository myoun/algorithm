n, L = map(int, input().split())
box_x = [*map(int, input().split())]

centers = [box_x[0]]

for i in range(1, n):
    centers.append(centers[i-1]+box_x[i])


la = None
for i, v in enumerate(box_x):
    if i != 0:
        if not (la[0]-L < v < la[1]+L):
            print("unstable")
            break
        elif la[0] < (centers[-1]-centers[i-1])/(n-i) < la[1]:
            pass
        else:
            print("unstable")
            break
    la = (v-L, v+L)
    if i == n-1:
        print("stable")