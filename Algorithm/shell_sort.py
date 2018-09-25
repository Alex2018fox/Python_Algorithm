##--4.--希尔排序
def shell_sort(lists):
    le=len(lists)
    gap=le//2
##----定义间隔序列至1（5，3，1）  
    while gap>0:
        for i in range(gap,le):
            j=i
            while j>=gap:
##----交换a[i]和a[i+gap]                
                if lists[j]<lists[j-gap]:

                    lists[j],lists[j-gap]=lists[j-gap],lists[j]
                    j-=gap
                else:
                    break
###-----重新定义间隔序列                   
        gap//=2
    return lists

if __name__=='__main__':
    lists=[3,46,6,3,6,46,8,3,15,2,30]
    print(lists)
    sortedLists=shell_sort(lists)
    print(sortedLists)