
##--1.-冒泡排序
def bubble_sort(lists):
    le=len(lists)

    for i in range(le):
#---两两比较区间内的取值
        for j in range(i+1,le):
            if lists[i]>lists[j]:
                lists[i],lists[j]=lists[j],lists[i]

    return lists

if __name__=='__main__':
    lists=[3,46,6,3,6,46,8,3,15,2,30]
    print(lists)
    sortedLists=bubble_sort(lists)
    print(sortedLists)