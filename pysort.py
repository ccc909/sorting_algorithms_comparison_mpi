# Necessary Imports
import random
from numba import njit
class Sorting:


    # Bubble Sort
    def bubbleSort(self,arr):
        n = len(arr)
        # optimize code, so if the array is already sorted, it doesn't need
        # to go through the entire process
        swapped = False
        # Traverse through all array elements
        for i in range(n - 1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.
            # Last i elements are already in place
            for j in range(0, n - i - 1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

            if not swapped:
                # if we haven't needed to make a single swap, we
                # can just exit the main loop.
                return

    # Selection Sort

    def selectionSort(self,arr):

        for i in range(len(arr)): 
        # Find the minimum element in remaining  
        # unsorted array 
            min_idx = i 
            for j in range(i+1, len(arr)): 
                if arr[min_idx] > arr[j]: 
                    min_idx = j 
            # Swap the found minimum element with  
            # the first element         
            arr[i], arr[min_idx] = arr[min_idx], arr[i] 

        return arr

    # Insertion Sort

    def insertionSort(self,arr):

        # Traverse through 1 to len(arr) 
        for i in range(1, len(arr)): 
            key = arr[i] 
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
            j = i-1
            while j >= 0 and key < arr[j] : 
                    arr[j + 1] = arr[j] 
                    j -= 1
            arr[j + 1] = key
        return arr
    
    # Shell Sort

    def shellSort(self,arr):
            # Start with a big gap, then reduce the gap 
        n = len(arr) 
        gap = n//2
        # Do a gapped insertion sort for this gap size. 
        # The first gap elements a[0..gap-1] are already in gapped  
        # order keep adding one more element until the entire array 
        # is gap sorted 
        while gap > 0: 
  
            for i in range(gap,n): 
    
                # add a[i] to the elements that have been gap sorted 
                # save a[i] in temp and make a hole at position i 
                temp = arr[i] 
    
                # shift earlier gap-sorted elements up until the correct 
                # location for a[i] is found 
                j = i 
                while  j >= gap and arr[j-gap] >temp: 
                    arr[j] = arr[j-gap] 
                    j -= gap 
    
                # put temp (the original a[i]) in its correct location 
                arr[j] = temp 
            gap //= 2

        return arr
    
    # Pegion Hole Sort

    def pigeonHoleSort(self,arr):
            # size of range of values in the list  
            # (ie, number of pigeonholes we need) 
        my_min = min(arr) 
        my_max = max(arr) 
        size = my_max - my_min + 1
  
        # our list of pigeonholes 
        holes = [0] * size 
    
        # Populate the pigeonholes. 
        for x in arr: 
            assert type(x) is int, "integers only please"
            holes[x - my_min] += 1
    
        # Put the elements back into the array in order. 
        i = 0
        for count in range(size): 
            while holes[count] > 0: 
                holes[count] -= 1
                arr[i] = count + my_min 
                i += 1
        return arr
    
    # Heap Sort

    def heapify(self,arr, n, i):
        # Find largest among root and children
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        # If root is not largest, swap with largest and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heapSort(self,arr):
        n = len(arr)

        # Build max heap
        for i in range(n // 2, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            # Swap
            arr[i], arr[0] = arr[0], arr[i]

            # Heapify root element
            self.heapify(arr, i, 0)

    # Gnome Sort

    def gnomeSort(self, arr): 
        index = 0
        n = len(arr)
        while index < n: 
            if index == 0: 
                index = index + 1
            if arr[index] >= arr[index - 1]: 
                index = index + 1
            else: 
                arr[index], arr[index-1] = arr[index-1], arr[index] 
                index = index - 1
  
        return arr

    # Stooage Sort
    def stoogeSort(self,arr,l,h): 
        
        if l >= h: 
            return
    
        # If first element is smaller 
        # than last, swap them 
        if arr[l]>arr[h]: 
            t = arr[l] 
            arr[l] = arr[h] 
            arr[h] = t 
    
        # If there are more than 2 elements in 
        # the array 
        if h-l + 1 > 2: 
            t = (int)((h-l + 1)/3) 
    
            # Recursively sort first 2 / 3 elements 
            self.stoogeSort(arr, l, (h-t)) 
    
            # Recursively sort last 2 / 3 elements 
            self.stoogeSort(arr, l + t, (h)) 
    
            # Recursively sort first 2 / 3 elements 
            # again to confirm 
            self.stoogeSort(arr, l, (h-t))
        return arr

    # Pancake Sorting

    # Reverses arr[0..i]  
    def flip(self,arr, i): 
        start = 0
        while start < i: 
            temp = arr[start] 
            arr[start] = arr[i] 
            arr[i] = temp 
            start += 1
            i -= 1
    
    # Returns index of the maximum 
    # element in arr[0..n-1] */ 
    def findMax(self,arr, n): 
        mi = 0
        for i in range(0,n): 
            if arr[i] > arr[mi]: 
                mi = i 
        return mi 
    
    # The main function that  
    # sorts given array  
    # using flip operations 
    def pancakeSort(self,arr): 
        
        # Start from the complete 
        # array and one by one 
        # reduce current size 
        # by one 
        curr_size = len(arr)
        while curr_size > 1: 
            # Find index of the maximum 
            # element in  
            # arr[0..curr_size-1] 
            mi = self.findMax(arr, curr_size) 
    
            # Move the maximum element 
            # to end of current array 
            # if it's not already at  
            # the end 
            if mi != curr_size-1: 
                # To move at the end,  
                # first move maximum  
                # number to beginning  
                self.flip(arr, mi) 
    
                # Now move the maximum  
                # number to end by 
                # reversing current array 
                self.flip(arr, curr_size-1) 
            curr_size -= 1
        return arr

    # Bogo (OR) Permutation Sort
    # Sorts array a[0..n-1] using Bogo sort 
    def bogoSort(self,arr): 
        n = len(arr) 
        while (self.is_sorted(arr)== False): 
            self.shuffle(arr) 
        return arr

    
    # To check if array is sorted or not 
    def is_sorted(self,arr): 
        n = len(arr) 
        for i in range(0, n-1): 
            if (arr[i] > arr[i+1] ): 
                return False
        return True
    
    # To generate permuatation of the array 
    def shuffle(self,arr): 
        n = len(arr) 
        for i in range (0,n): 
            r = random.randint(0,n-1) 
            arr[i], arr[r] = arr[r], arr[i]
    
    # Merge Sort

    def msort4(self,x):
        if len(x) < 20:
            return sorted(x)
        result = []
        mid = int(len(x) / 2)
        y = self.msort4(x[:mid])
        z = self.msort4(x[mid:])
        i = 0
        j = 0
        while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
        result += y[i:]
        result += z[j:]
        return result

    # Quick Sort
    def quicksort(self,array):
        if len(array) <= 1:
            return array

        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]

        return self.quicksort(left) + middle + self.quicksort(right)
    
    # Cocktail Sort

    def cocktailSort(self,arr): 
        n = len(arr) 
        swapped = True
        start = 0
        end = n-1
        while (swapped == True): 
    
            # reset the swapped flag on entering the loop, 
            # because it might be true from a previous 
            # iteration. 
            swapped = False
    
            # loop from left to right same as the bubble 
            # sort 
            for i in range (start, end): 
                if (arr[i] > arr[i + 1]) : 
                    arr[i], arr[i + 1]= arr[i + 1], arr[i] 
                    swapped = True
    
            # if nothing moved, then array is sorted. 
            if (swapped == False): 
                break
    
            # otherwise, reset the swapped flag so that it 
            # can be used in the next stage 
            swapped = False
    
            # move the end point back by one, because 
            # item at the end is in its rightful spot 
            end = end-1
    
            # from right to left, doing the same 
            # comparison as in the previous stage 
            for i in range(end-1, start-1, -1): 
                if (arr[i] > arr[i + 1]): 
                    arr[i], arr[i + 1] = arr[i + 1], arr[i] 
                    swapped = True
    
            # increase the starting point, because 
            # the last stage would have moved the next 
            # smallest number to its rightful spot. 
            start = start + 1

        return arr
    
    # Brick Sort
    def brickSort(self,arr): 
        # Initially array is unsorted 
        isSorted = 0
        n = len(arr)
        while isSorted == 0: 
            isSorted = 1
            temp = 0
            for i in range(1, n-1, 2): 
                if arr[i] > arr[i+1]: 
                    arr[i], arr[i+1] = arr[i+1], arr[i] 
                    isSorted = 0
                    
            for i in range(0, n-1, 2): 
                if arr[i] > arr[i+1]: 
                    arr[i], arr[i+1] = arr[i+1], arr[i] 
                    isSorted = 0
        return arr

    # Radix Sort

    def countingSort(self,array, place):
        size = len(array)
        output = [0] * size
        count = [0] * 10

        # Calculate count of elements
        for i in range(0, size):
            index = array[i] // place
            count[index % 10] += 1

        # Calculate cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Place the elements in sorted order
        i = size - 1
        while i >= 0:
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, size):
            array[i] = output[i]


    # Main function to implement radix sort
    def radixSort(self,array):
        # Get maximum element
        max_element = max(array)

        # Apply counting sort to sort elements based on place value.
        place = 1
        while max_element // place > 0:
            self.countingSort(array, place)
            place *= 10
