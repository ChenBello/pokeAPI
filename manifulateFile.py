class File:

    def __init__(self, data):
        self.data = data

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self.data))