import csv
import math
from pathlib import Path

class NotCSVFileException(Exception):
    pass

class EmptyFileException(Exception):
    pass

class sortedFile:

    def __init__(self):
        self.input = ""
        self.output = ""
        self.arrayFile = []
        self.checkInput = False
        self.checkOutput = False

    def initMergeSort(self):
        if self.checkInput:
            self.mergeSort(self.arrayFile)


    def mergeSort(self, input_array):
        if len(input_array)>1:
            mid = len(input_array)//2
            lefthalf = input_array[:mid]
            righthalf = input_array[mid:]

            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)

            i=0
            j=0
            k=0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    input_array[k]=lefthalf[i]
                    i=i+1
                else:
                    input_array[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf):
                input_array[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                input_array[k]=righthalf[j]
                j=j+1
                k=k+1

    def set_output_data(self, file_path_name):
        self.output = file_path_name
        path_instance = Path(file_path_name)
        if path_instance.is_file():
            if path_instance.suffix == '.csv':
                output = []
                for item in self.arrayFile:
                    output.append(str(item))
                with open(file_path_name, 'w', newline='') as file:
                    writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(output)
                file.close()
                self.checkOutput = True
            else:
                raise NotCSVFileException
        else:
            raise FileNotFoundError

    def set_input_data(self, file_path_name):
        self.input = file_path_name
        path_instance = Path(file_path_name)
        if path_instance.is_file():
            if path_instance.suffix == '.csv':
                with open(file_path_name, 'r') as csvfile:
                    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                    for row in spamreader:
                        for item in row:
                            if item.isdigit():
                                self.arrayFile.append(float(item))
                            else:
                                raise TypeError
                csvfile.close()

                if(not(self.arrayFile)):
                    raise EmptyFileException
                self.checkInput = True
            else:
                raise NotCSVFileException
        else:
            raise FileNotFoundError

    def heapify(self, arr, n, i):
            largest = i  # Initialize largest as root
            l = 2 * i + 1  # left = 2*i + 1
            r = 2 * i + 2  # right = 2*i + 2

            # See if left child of root exists and is
            # greater than root
            if l < n and arr[i] < arr[l]:
                largest = l

                # See if right child of root exists and is
            # greater than root
            if r < n and arr[largest] < arr[r]:
                largest = r

                # Change root, if needed
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # swap

                # Heapify the root.
                self.heapify(arr, n, largest)

                # The main function to sort an array of given size

    def execute_heap_sort(self, input_array):
        n = len(input_array)

        # Build a maxheap.
        for i in range(n, -1, -1):
            self.heapify(input_array, n, i)

            # One by one extract elements
        for i in range(n - 1, 0, -1):
            input_array[i], input_array[0] = input_array[0], input_array[i]  # swap
            self.heapify(input_array, i, 0)


    def __quick_sort(self, input_array, leftIndex, rightIndex):

        if(len(input_array) > 1):
            pivotIndex = self.__partition(input_array, leftIndex, rightIndex)

            if(leftIndex < pivotIndex - 1):
                self.__quick_sort(input_array, leftIndex, pivotIndex - 1)

            if(pivotIndex < rightIndex):
                self.__quick_sort(input_array, pivotIndex, rightIndex)

        return input_array

    def __swap(self, input_array, leftPointer, rightPointer):
        temp = input_array[leftPointer]
        input_array[leftPointer] = input_array[rightPointer]
        input_array[rightPointer] = temp

    def __partition(self, input_array, left, right):
        pivot = input_array[math.floor((right + left) / 2)]
        l = left
        r = right

        while(l <= r):
            while(input_array[l] < pivot):
                l += 1

            while (input_array[r] > pivot):
                r -= 1

            if (l <= r):
                self.__swap(input_array, l, r)
                l += 1
                r -= 1

        return l


    def execute_quick_sort(self, input_array):
        rightRef = len(input_array) - 1
        leftRef = 0
        self.__quick_sort(input_array, leftRef, rightRef)

    def initHeapSort(self):
        if self.checkInput:
            self.execute_heap_sort(self.arrayFile)

    def initQuickSort(self):
        if self.checkInput:
            self.execute_quick_sort(self.arrayFile)
