## 扑克按顺序输出
# 过了80% 用例

def  pokersort(pokers):
    dic = {"3":1, "4":2, "5":3, "6":4,
           "7":5,"8":6,"9":7,"10":8,"J":9,"Q":10,"K":11,
           "A":12,"2":13}
    d = sorted(pokers,key=lambda x:dic[x])
    print(d)
pokers = []
pokersort(pokers)

