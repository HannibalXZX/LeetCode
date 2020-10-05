

while 1:
    s1 = input()
    s2 = input()
    s3 = input()

    n_list = s1.split(" ")
    a_list = s2.split(" ")
    b_list = s3.split(" ")

    num = int(n_list[0])
    n_list = [0] * (num)
    # a
    for a in a_list:
        n_list[int(a)-1] = 1

    for b in b_list:
        if n_list[int(b)-1] == 1:
            n_list[int(b)-1] = 3
        else:
            n_list[int(b)-1] = 2

    common = 0
    a_alone = 0
    b_alone = 0

    for element in n_list:
        if element == 1:
            a_alone += 1
        elif element == 2:
            b_alone += 1
        elif element == 3:
            common += 1
        else:
            continue


    print("%d %d %d" % (a_alone,b_alone,common))



