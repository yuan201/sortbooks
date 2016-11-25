import unittest

from booksorter import BookSorter


class BookSorterTest(unittest.TestCase):
    def test_scan_command(self):
        bs = BookSorter('sacn',
                        '--config config.json',
                        '--target ./books')
        bs.run()
        # test there is booktypes.json and it has proper information

    def test_sort_command(self):
        bs = BookSorter('sort',
                        '--config config.json',
                        '--report report.txt',
                        '--source ./inbox')
        bs.run()
        # test there is report.txt and it has sorting result

    def test_move_command(self):
        bs = BookSorter('move',
                        '--config config.json',
                        '--report report.txt',
                        '--source ./inbox',
                        '--target ./books')
        bs.run()
        # test the books have been moved and report updated

    def test_default_configs(self):
        bs = BookSorter('scan')
        # assert bs is properly configed by 'config.json'

    
