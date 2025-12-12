import numpy as np

# occ = (2*line)  -1
# 3x3
coords_3 = np.array([5.0, 5.0, 5.0, 5.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0])
avg_3_coords = np.mean(coords_3)

# allo=ego is coords-1
allo_3 = np.zeros(10)
for i in range(0,10):
    allo_3[i] = coords_3[i]-1
avg_3_allo = np.mean(allo_3)

# 7x7
coords_7 = np.array([9.0, 9.0, 9.0, 9.0, 13.0, 9.0, 9.0, 13.0, 13.0, 9.0])
avg_7_coords = np.mean(coords_7)
# allo=ego is coords-1
allo_7 = np.zeros(10)
for i in range(0,10):
    allo_7[i] = coords_7[i]-1
avg_7_allo = np.mean(allo_7)


# 6x6
coords_6 = np.array([17.0, 19.0, 35.0, 29.0, 15.0, 21.0, 25.0, 11.0, 17.0, 21.0])
avg_6_coords = np.mean(coords_6)

# allo=ego is coords-1
allo_6 = np.zeros(10)
for i in range(0,10):
    allo_6[i] = coords_6[i]-1
avg_6_allo = np.mean(allo_6)


# 13x13
coords_13 = np.array([33.0, 37.0, 69.0, 57.0, 29.0, 41.0, 49.0, 21.0, 33.0, 41.0])
avg_13_coords = np.mean(coords_13)

# allo=ego is coords+1
allo_13 = np.zeros(10)
for i in range(0,10):
    allo_13[i] = coords_13[i]-1
avg_13_allo = np.mean(allo_13)


# 15x15
coords_15 = np.array([131.0, 69.0, 139.0, 57.0, 127.0, 101.0, 67.0, 79.0, 133.0, 47.0])
avg_15_coords = np.mean(coords_15)

allo_15 = np.array([130.0, 68.0, 138.0, 56.0, 126.0, 100.0, 66.0, 78.0, 132.0, 46.0])
avg_15_allo = np.mean(allo_15)
# ego is hetzelfde als allo



# 31x31
coords_31 = np.array([261.0, 137.0, 277.0, 113.0, 253.0, 201.0, 133.0, 157.0, 265.0, 93.0])
avg_31_coords = np.mean(coords_31)

allo_31 = np.array([260.0, 136.0, 276.0, 112.0, 252.0, 200.0, 132.0, 156.0, 264.0, 92.0])
avg_31_allo = np.mean(allo_31)
# ego is hetzelfde als allo


print('3x3 coords: ',avg_3_coords)
print('3x3 allo: ',avg_3_allo)
print('7x7 coords: ',avg_7_coords)
print('7x7 allo: ',avg_7_allo)
print('6x6 coords: ',avg_6_coords)
print('13x13 coords: ',avg_13_coords)
print('15x15 coords: ',avg_15_coords)
print('31x31 coords: ',avg_31_coords)

print('6x6 allo: ',avg_6_allo)
print('13x13 allo: ',avg_13_allo)
print('15x15 allo: ',avg_15_allo)
print('31x31 allo: ',avg_31_allo)


# print('allo 3',allo_3)
# print('allo 7', allo_7)