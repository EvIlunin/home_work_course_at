num = 379
num = str(num)
first_inx = 0
for i in range(0, len(num)):
    for j in range(9, int(num[0]), -1):
        new_num = num[:i] + str(j) + num[i+1:]
        print(new_num)
    new_num = num