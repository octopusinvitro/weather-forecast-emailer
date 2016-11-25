class Printer:

    def __init__(self, output):
        self.output = output

    def print(self, message):
        self.output.write(message)

    def println(self, message):
        self.print(message + '\n')

    def print_header(self, message):
        self.print(self.header(message))

    def print_list(self, header, dictionary):
        self.print(self.format_list(header, dictionary))

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
