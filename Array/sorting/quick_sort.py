def partition(array, low, high):
    """
    This function rearranges the array and returns the new index of the pivot element.

    Args:
        array: The array to be sorted.
        low: The starting index of the sub-array to partition.
        high: The ending index of the sub-array to partition.

    Returns:
        The new index of the pivot element after partitioning.
    """

    pivot = array[high]  # Choose the last element (high) as the pivot
    i = low - 1  # Index to keep track of the smaller element position

    # Loop through the sub-array (excluding the pivot)
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if array[j] <= pivot:
            i += 1  # Increment the smaller element position
            # Swap the current element with the element at the smaller position
            array[i], array[j] = array[j], array[i]

    # Swap the pivot (originally at high) with the element at the position after the smaller elements
    array[i + 1], array[high] = array[high], array[i + 1]

    # Return the new pivot index (i + 1)
    return i + 1

def quicksort(array, low=0, high=None):
    """
    This function sorts the given array using Quick Sort algorithm.

    Args:
        array: The array to be sorted.
        low: The starting index (default 0).
        high: The ending index (default None, representing the last element).
    """

    if low < high:  # Check if there are elements to sort (low < high)
        # Step 1: Partition the array
        pivot_index = partition(array, low, high)

        # Step 2: Recursively sort the sub-arrays left and right of the pivot
        quicksort(array, low, pivot_index - 1)  # Sort left sub-array (low to pivot-1)
        quicksort(array, pivot_index + 1, high)  # Sort right sub-array (pivot+1 to high)

# Example usage
my_array = [64, 2, 25, 12, 22, 11, 90, 5]
quicksort(my_array, 0, len(my_array) - 1)
print("Sorted array:", my_array)
