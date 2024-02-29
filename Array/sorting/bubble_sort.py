'''
Bubble sort: 
- Compare adjecent numbers and 
- swap if the second number is smallest than first else no swap
- move pointer to the next element and again compare two adjecent elements
- if swapcnt is >= 1
- repeate same swappning process 
'''

array = [22, 34, 45, 90, 78, 3]
swapCnt = 0
passes = 1
print("original array: ", array)
def bubble_sort(array):
    global passes
    global swapCnt
    swapCnt = 0
    for i in range(len(array) - 1):
        j = i + 1
        if(array[j] < array[i]):
            # swap the elements
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            swapCnt += 1
       
    if swapCnt >= 1:
        print("pass : ", passes , " - ", array)
        passes += 1
        bubble_sort(array)
    else:
        return

       
bubble_sort(array)
print("----final array when no swappning needed-----")
print("pass: ", passes, " - ", array)
