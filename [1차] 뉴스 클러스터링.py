# https://school.programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    s1, s2 = "", ""
    for char in str1:
        # if char.isalpha():
        s1 += char.lower()
    for char in str2:
        # if char.isalpha():
        s2 += char.lower()
    
    len1, len2 = len(s1), len(s2)
    l1, l2 = [], []
    for i in range(len1-1):
        if s1[i].isalpha() and s1[i+1].isalpha():
            l1.append(s1[i] + s1[i+1])
    for i in range(len2-1):
        if s2[i].isalpha() and s2[i+1].isalpha():
            l2.append(s2[i] + s2[i+1])
    
    print(l1, l2)
    if len(l1) == 0 and len(l2) == 0:
        return 65536
    # print(l1, l2)


    d1, d2 = {}, {}
    c1, c2 = 0, 0
    for item in l1:
        if item not in d1.keys():
            c1 = l1.count(item)
            d1[item] = c1
    for item in l2:
        if item not in d2.keys():
            c2 = l2.count(item)
            d2[item] = c2
    union = {}
    comp = {}
    for k, v in d1.items():
        union[k] = v
    
    # print("start", union)
    # print(d1, d2)
    for k, v in d2.items():
        # print(union)
        if k in union.keys():
            # union[k] = union[k] + d2[k]
            union[k] = max(union[k], d2[k])
        else:
            union[k] = d2[k]

    for k in d1.keys():
        if k in d2.keys():
            # print(comp)
            comp[k] = min(d1[k], d2[k])
    

    print("union: ", union)
    print("comp: ", comp)
    print("-----------------------------------")
    t1, t2 = 0, 0
    for v in union.values():
        t1 += v
    for v in comp.values():
        t2 += v
    
    return int((65536 * t2) / t1)
