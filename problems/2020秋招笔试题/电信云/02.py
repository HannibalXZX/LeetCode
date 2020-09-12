# 打印数据
# AC

for a in range(9):
    for b in range(9):
        for c in range(9):
            for d in range(9):
                val_1 = a*1000+b*100+c*10+d*1
                val_2 = b*1000+c*100+d*10+a*1
                # print(val_1)
                if val_1 + val_2 == 8888:
                    print(a,b,c,d)