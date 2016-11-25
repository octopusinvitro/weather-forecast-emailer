from unittest import TestCase
from io import StringIO

from weather_forecast_emailer import Printer


class TestPrinter(TestCase):
    def setUp(self):
        self.output  = StringIO()
        self.printer = Printer(self.output)

    def test_prints_a_message(self):
        self.printer.write('message')
        self.assertEqual(self.output.getvalue(), 'message')

    def test_prints_a_line(self):
        self.printer.writeln('message')
        self.assertEqual(self.output.getvalue(), 'message\n')

    def test_prints_the_right_amount_of_lines_in_header(self):
        self.printer.write_header('')
        self.assertEqual(self.output.getvalue().count('\n'), 4)

    def test_prints_the_right_message_in_header(self):
        self.printer.write_header('message')
        self.assertTrue('message' in self.output.getvalue())

    def test_prints_all_keys_in_list(self):
        self.printer.write_list('', {'foo': 'bar', 'qux': 1})
        self.assertTrue('foo' in self.output.getvalue())
        self.assertTrue('qux' in self.output.getvalue())

    def test_prints_all_values_in_list(self):
        self.printer.write_list('', {'foo': 'bar', 'qux': 1})
        self.assertTrue('bar' in self.output.getvalue())
        self.assertTrue('1' in self.output.getvalue())

    def test_prints_header_before_list(self):
        self.printer.write_list('header', {'foo': 'bar', 'qux': 1})
        self.assertTrue('header' in self.output.getvalue())

    def test_prints_the_right_amount_of_lines_in_list(self):
        self.printer.write_list('header', {'foo': 'bar', 'qux': 1})
        self.assertEqual(self.output.getvalue().count('\n'), 6)
