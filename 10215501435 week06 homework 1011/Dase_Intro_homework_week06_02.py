import random
import time


# 插入排序和冒泡排序
def insertion_sort(arr):
    for i in range(1, len(arr)):  # 下标为0元素视作有序，所以从下标为1的元素开始排序（步骤1，步骤6）
        origin = arr[i]
        j = i
        while j > 0:  # 从后向前扫描（步骤2）
            if arr[j - 1] > origin:  # 如果有序的某元素大于待排序元素，则该元素向后移动一个位置（步骤3）
                arr[j] = arr[j - 1]
            else:  # 否则变量j的值就是待排序元素的插入位置（步骤4）
                break
            j -= 1
        arr[j] = origin  # 如果用内部循环采用for形式，一定要预先定义j的值，否则此语句中j的值未知


def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array) - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


arr1 = []
for i in range(10000):
    arr1.append(random.random())
arr2 = arr1.copy()  # 确保两个数组一样

t_a = time.perf_counter()
insertion_sort(arr1)
t_b = time.perf_counter()
print(t_b - t_a)

t_a = time.perf_counter()
bubble_sort(arr2)
t_b = time.perf_counter()
print(t_b - t_a)