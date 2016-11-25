from unittest import TestCase
from io import StringIO

from weather_forecast_emailer import EmailListReader


class TestEmailListReader(TestCase):
    def test_obtains_an_empty_array_if_file_is_empty(self):
        readme = StringIO('')
        reader = EmailListReader(readme)
        self.assertEqual(reader.as_dictionary(''), {})

    def test_splits_by_separator(self):
        readme = StringIO('foo, bar\n')
        reader = EmailListReader(readme)
        self.assertEqual(reader.as_dictionary(','), {'foo': 'bar'})

    def test_strips_extra_spaces_from_key_and_value(self):
        readme = StringIO(' foo - bar  \n')
        reader = EmailListReader(readme)
        self.assertEqual(reader.as_dictionary('-'), {'foo': 'bar'})

    def test_reads_from_the_beginning_of_the_file(self):
        readme = StringIO('foo * bar\n')
        reader = EmailListReader(readme)
        readme.seek(1)
        self.assertEqual(reader.as_dictionary('*'), {'foo': 'bar'})
