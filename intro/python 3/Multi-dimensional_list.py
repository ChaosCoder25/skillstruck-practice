# n = 5 
# list = []
# for i in range(n):
#     list.append(0)
# print(list)

# rows = [1, 2, 3]
# cols = ["red", "orange", "yellow", "green"]
# list = []
# for i in rows:
#     col = []
#     for j in cols:
#         col.append(j)
#         list.append(col)
# print(list)

# rows = 5
# cols = 5
# list = []
# for i in range(cols):
#     col = []
#     for j in range(rows):
#         col.append(5)
#         list.append(col)
# print(list)

rows = [1, 2, 3]
cols = ["red", "orange", "yellow", "green"]
list = []
for i in rows:
    col = []
    for j in cols:
        col.append(j)
        list.append(rows+cols)
print(list)