class Printer:
    def __init__(self, output):
        self.output = output

    def write(self, message):
        self.output.write(message)

    def writeln(self, message):
        self.write(message + '\n')

    def write_header(self, message):
        self.write(self.header(message))

    def write_list(self, header, dictionary):
        self.write(self.format_list(header, dictionary))

    def format_list(self, message, dictionary):
        formatted = self.header(message)
        for key, value in dictionary.items():
            formatted += key + ': ' + str(value) + '\n'
        return formatted

    def header(self, message):
        formatted  = '\n----------------------------------------\n'
        formatted += message
        formatted += '\n----------------------------------------\n'
        return formatted
