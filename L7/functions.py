import csv
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