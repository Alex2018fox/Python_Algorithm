##----9.-桶排序
def bucket_Sort(nums):

# 选择一个最大的数
    max_num=max(nums)
# 创建一个元素全是0的列表, 当做桶
    bucket=[0]*(max_num+1)
# 把所有元素放入桶中, 即把对应元素个数加一
    for i in nums:
         bucket[i]+=1
# 存储排序好的元素
    sort_nums=[]
# 取出桶中的元素
    for j in range(len(bucket)):
        if bucket[j]!=0:
            for y in range(bucket[j]):
                sort_nums.append(j)
    return sort_nums

if __name__=='__main__':
  
    list1 = [5, 6, 7,7,5,9,4, 9, 11, 20, 1]
    print(list1)
    b=bucket_Sort(list1)
    print(b)