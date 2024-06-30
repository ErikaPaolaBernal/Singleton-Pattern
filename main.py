from src.data_loader import DataLoader
from src.student import Student

def print_data(data):
    # print all  instances returned by data_loader
    for item in data:
        print(item)


def main():
    data_loader = DataLoader(new_id=1, data_path='data')
    print(f"DataLoader ID: {data_loader.id}")
    #Load students from file using the data_loader instance
    students = data_loader.read_data_from_file(file_name='students.txt', obj_type=Student)
    print_data(students)

    print('===============================================')
    print('Trying to create a new DataLoader with new ID')
    #Create a new DataLoader: checking if it is a new instance or not
    new_data_loader = DataLoader(new_id=2, data_path='data')
    print(f"DataLoader ID: {new_data_loader.id}")
    #Load students from file using the data_loader instance
    students = new_data_loader.read_data_from_file(file_name='students.txt', obj_type=Student)
    print_data(students)


if __name__ == '__main__':
    main()