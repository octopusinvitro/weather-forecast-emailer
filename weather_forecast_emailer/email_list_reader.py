class EmailListReader:
    def __init__(self, file_to_read):
        self.file = file_to_read

    def as_dictionary(self, separator):
        self.file.seek(0, 0)
        contents = {}
        for line in self.file:
            (key, value) = line.split(separator)
            contents[key.strip()] = value.strip()
        return contents
