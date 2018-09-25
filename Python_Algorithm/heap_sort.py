#---6.--堆排序
def heap_sort(array):
    def heap_adjust(parent):
        child = 2 * parent + 1 # left child
        while child < len(heap):
###找出左右孩子节点中较大的
            if child + 1 < len(heap):
                if heap[child + 1] > heap[child]:
                    child += 1 # right child
#判断是否为大顶堆                   
            if heap[parent] >= heap[child]:
                break
###子节点上移               
            heap[parent], heap[child] = heap[child], heap[parent]
##继续向下比较          
            parent, child = child, 2 * child + 1
##将原堆顶插入正确位置   
    heap, array = array.copy(), []
##建立大顶堆，最后一个非叶节点（完全二叉树中）
    for i in range(len(heap) // 2, -1, -1):
        heap_adjust(i)

    while len(heap) != 0:
#将大顶堆堆顶数放到最后，调整剩余数组成堆
        heap[0], heap[-1] = heap[-1], heap[0]
        array.insert(0, heap.pop())
        heap_adjust(0)
    return array

if __name__=='__main__':
    list1 = [46,6,7,48,8,3,15,3,46,7,2,30]
    print(list1)
    b=heap_sort(list1)
    print(b)