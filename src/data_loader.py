from typing import Any


class DataLoaderV1:
    def __init__(self, new_id, data_path=None):
        self.id = new_id
        self.data_path = data_path

    def read_data_from_file(self, file_name: str, obj_type: Any):
        # A string representing the name of the file to read from
        # A type (class) that will be used to create objects from the data in the file
        objects = [] # This list will hold the objects created from the data read from the file
        if self.data_path: # if data_path is not empty, the full file path is constructed by concatenating self.data_path, a forward slash (/), and file_name.
            file_path = self.data_path + '/' + file_name
        else:
            file_path = file_name


        with open(file_path, 'r') as file:
            for line in file:
                attributes = line.strip().split(',')
                #Dynamically create an object of type obj_type
                obj = obj_type(*attributes)
                objects.append(obj)
        return objects

## Singleton version1

class DataLoader:
    _instance = None

    def __new__(cls, new_id, data_path=None):
        if cls._instance is None: # cls means you don't need an instance, give access to static methods
        #Create a new instance of DataLoader
            cls._instance = super(DataLoader, cls).__new__(cls)
        return cls._instance

    def __init__(self, new_id, data_path=None):
        self._initialized = False
        if not hasattr(self, 'initialized'): #hasattr
            self._initialized = True
            self.id = new_id
            self.data_path = data_path
        else:
            print("f Warning: DataLoader class is singleton, your request is denied!")

    def read_data_from_file(self, file_name: str, obj_type: Any):
        objects = []
        if self.data_path:
            file_path = self.data_path + '/' + file_name
        else:
            file_path = file_name


        with open(file_path, 'r') as file:
            for line in file:
                attributes = line.strip().split(',')
                #Dynamically create an object of type obj_type
                obj = obj_type(*attributes)
                objects.append(obj)
        return objects