'''
Selection sort:
- find smallest element and move to the front of the array 
- i.e find smallest element and move to 0th index at 1st iteration
again repeat same and put element to 2nd index (swapping)
if element already placed to it's desired position then no need to swap
pass : 1 - [3, 12, 9, 11, 7]
pass : 2 - [3, 7, 12, 11, 9]
pass : 3 - [3, 7, 9, 12, 11]
pass : 4 - [3, 7, 9, 11, 12]
pass : 5 - [3, 7, 9, 11, 12]
'''

array = [ 7, 12, 9, 11, 3]
# minVal = array[0]
passes = 1
swapCnt = 0
cnt = 0
def selection_sort(array):
    global cnt
    global passes
    global swapCnt
    swapCnt = 0
    for i in range(cnt + 1, len(array)):
        if(array[i] < array[cnt]):
            temp  = array[cnt]
            array[cnt] = array[i]
            array[i] =  temp
            swapCnt += 1
    if swapCnt >= 1:
        passes += 1
        cnt+= 1
        print(f"pass : {passes} - {array}")
        selection_sort(array)
            
    
selection_sort(array)
print(f"pass : {passes} - {array}")


