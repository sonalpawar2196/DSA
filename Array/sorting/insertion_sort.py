'''
Example - sorting playing cards
- consider 0th position number is sorted array and start 
comparing from next elements
- you need to shift next elements in the correct position in the sorted array
- [ 7, 12, 9, 11, 3]
- pass 1(12): [7, 12, 9, 11, 3] - no swap
- pass 2(9): [7, 9, 12, 11, 3] move it between 7 and 12 
- pass 3(11): [7, 9, 11,12, 3] move between 9 and 12
- pass 4 (3):[3, 7, 9, 11,12] move it left to 7
'''

# approch
# need one outer loop for checking next elements
# inner loop will check elements before current element to insert 
array =  [7, 12, 9, 11, 3]
passes = 1

def insertion_sort(array):
    global passes
    for i in range(1, len(array)):
        for j in range(0, i):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

        print(f"Pass: {passes} - {array}")
        passes += 1

insertion_sort(array)