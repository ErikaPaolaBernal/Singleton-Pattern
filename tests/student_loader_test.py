import unittest

from src.data_loader import DataLoader
from src.student import Student


class TestDataLoader(unittest.TestCase):

    def test_read_data_from_file(self):
        #Initialize DataLoader
        data_file_name = 'test_students.txt' # is the name of the test data file
        expected_data_loader_id = 1 # is the expected ID for the DataLoader instance
        expected_nb_students = 3 # is the expected number of student records to be read from the file

        # Action initializing DataLoader and Reading Data
        data_loader = DataLoader(
                                new_id=expected_data_loader_id,
                                data_path='test_data')
        students = data_loader.read_data_from_file(data_file_name, Student) # The method is called to read student data from the file
        # and create Student objects.
        self.assertEqual(len(students), expected_nb_students) # This assertion checks whether
        # the number of student objects read from the file matches the expected number
        # (expected_nb_students). If the condition is not met, the test will fail.

    def test_singleton_data_loader(self):
        #Initialize DataLoader
        data_file_name = 'test_students.txt'
        expected_data_loader_id = 1
        expected_nb_students = 3

        # Action
        data_loader = DataLoader(
                                new_id=expected_data_loader_id,
                                data_path='test_data')
        students = data_loader.read_data_from_file(data_file_name, Student)
        self.assertEqual(len(students), expected_nb_students)

        data_loader = DataLoader(
                                new_id=expected_data_loader_id,
                                data_path='test_data')
        students = data_loader.read_data_from_file(data_file_name, Student)
        self.assertEqual(len(students), expected_nb_students)

