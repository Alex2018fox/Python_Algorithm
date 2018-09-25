##3.--插入排序

def insert_sort(lists):
    le=len(lists)

    for i in range(le):
        preIndex=i-1
        current=lists[i]
##构建有序序列，对未排序的数据，在已排序的序列中从后向前扫描，插入相应位置       
        while preIndex>=0 and lists[preIndex]>current:
            lists[preIndex+1]=lists[preIndex]
            preIndex-=1

        lists[preIndex+1]=current
  
    return lists
if __name__=='__main__':
    lists=[3,46,6,3,6,46,8,3,15,2,30]
    print(lists)
    sortedLists=insert_sort(lists)
    print(sortedLists)