
##--------5- 快速排序
def quick_sort(lists, left, right):

    if left >= right:
        return lists
   
    key = lists[left]
    low = left
    high = right
##数据分割成两个独立的部分（左小右大），对left和right两部分进行排序   
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]

    lists[right] = key
#递归快速排序   
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists

if __name__=='__main__':
    lists=[46,6,7,48,8,3,15,3,46,7,2,30]
    print(lists)
    sortedLists=quick_sort(lists,0,len(lists)-1)
    print(sortedLists)