def solution(n, arr1, arr2):
    arr1_list=[]
    arr2_list=[]
    for i in range(n):
        temp1=[]
        temp2=[]
        for j in range(n):
            temp1.append(arr1[i]%2)
            temp2.append(arr2[i]%2)
            arr1[i]=arr1[i]//2
            arr2[i]=arr2[i]//2
        temp1.reverse()
        temp2.reverse()
        arr1_list.append(temp1)
        arr2_list.append(temp2)
    # print(arr1_list, "---", arr2_list
    answer = []
    for i in range(n):
        temp_str=""
        for j in range(n):
            if arr1_list[i][j]==1 or arr2_list[i][j]==1:
                temp_str = temp_str+"#"
            else:
                temp_str = temp_str+" "
        answer.append(temp_str)
    return answer
