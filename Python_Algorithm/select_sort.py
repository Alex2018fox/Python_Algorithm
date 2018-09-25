
##-----2.-选择排序

def  select_sort(lists):
    le=len(lists)
###假设i为最小值的索引，
    for i in range(le):
        minIndex=i
        for j in range(i+1,le):
##寻找最小数并把最小数的索引保存           
            if lists[minIndex]>lists[j]:
                lists[minIndex],lists[j]=lists[j],lists[minIndex]

    return lists
if __name__=='__main__':
    lists=[3,46,6,3,6,46,8,3,15,2,30]
    print(lists)
    sortedLists=select_sort(lists)
    print(sortedLists)