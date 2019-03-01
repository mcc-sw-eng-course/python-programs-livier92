import unittest
from functions import *

class testClassSortedFile(unittest.TestCase):

    def test_correctExecution(self):
        fileMergeSort = sortedFile()
        fileMergeSort.set_input_data("eggs.csv")
        fileMergeSort.initMergeSort()
        fileMergeSort.set_output_data("output.csv")

    def test_ClassNoExistingFile(self):
        fileMergeSort = sortedFile()
        with self.assertRaises(FileNotFoundError):
            fileMergeSort.set_input_data("file2.txt")

    def test_ClassInvalidFile(self):
        fileMergeSort = sortedFile()
        with self.assertRaises(NotCSVFileException):
            fileMergeSort.set_input_data("invalidType.txt")

    def test_emptyCSVFile(self):
        fileMergeSort = sortedFile()
        with self.assertRaises(EmptyFileException):
            fileMergeSort.set_input_data("emptyFile.csv")

    def test_invalidParameter(self):
        fileMergeSort = sortedFile()
        with self.assertRaises(TypeError):
            fileMergeSort.set_input_data(23)

    def test_invalidParameterOutput(self):
        fileMergeSort = sortedFile()
        with self.assertRaises(TypeError):
            fileMergeSort.set_output_data(23)

    def test_incorrectOutputFileExt(self):
        fileMergeSort = sortedFile()
        with self.assertRaises(NotCSVFileException):
            fileMergeSort.set_output_data("file.txt")

    def test_incorrectOutputFile(self):
        fileMergeSort = sortedFile()
        with self.assertRaises(FileNotFoundError):
            fileMergeSort.set_output_data("file")

    def test_OutputIncorrectParameter(self):
        fileMergeSort = sortedFile()
        with self.assertRaises(TypeError):
            fileMergeSort.set_output_data(True)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testClassSortedFile)
    unittest.TextTestRunner(verbosity=0).run(suite)