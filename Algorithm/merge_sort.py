#------7.---归并排序
##-----子序列排序--将两个有序表合并
def merge(left,right):
    i=0
    j=0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result
#----划分左右区间
def merge_sort(lsits):
    if len(lsits)<=1:
        return lsits
    num=int(len(lsits)/2)
    left=merge_sort(lsits[:num])
    right=merge_sort(lsits[num:])
    return merge(left,right)

if __name__=='__main__':
    list1 = [5, 6, 7, 4, 9, 11, 20, 1]
    print(list1)
    b=merge_sort(list1)
    print(b)