#-----8.基数排序

def radix_sort(array):
    bucket, digit = [[]], 0
    while len(bucket[0]) != len(array):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(array)):
            num = (array[i] // 10 ** digit) % 10
            bucket[num].append(array[i])
        array.clear()
        for i in range(len(bucket)):
            array += bucket[i]
        digit += 1
    return array
if __name__=='__main__':
    list1 = [5, 6, 7, 4, 9, 11, 20, 1]
    print(list1)
    b=radix_sort(list1)
    print(b)