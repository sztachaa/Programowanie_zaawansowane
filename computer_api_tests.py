# Plik computer_api_tests.py
import unittest
import requests

class APITest(unittest.TestCase):
    BASE_URL = 'http://mojastrona.net/api.php'

    # Test dla podstawowego komputera
    def test_get_basic_computer(self):
        computer_id = 12345
        response = requests.get(f'{self.BASE_URL}?computer_id={computer_id}&type=basic')
        self.assertEqual(response.status_code, 200)
        expected_data = {'response_code': '200', 'response_desc': 'Success', 'parts': ['Obudowę', 'Płytę główną', 'Procesor', 'RAM', 'Zasilacz']}
        self.assertEqual(response.json(), expected_data)

    # Test dla komputera do gier
    def test_get_gaming_computer(self):
        computer_id = 67890
        response = requests.get(f'{self.BASE_URL}?computer_id={computer_id}&type=gaming')
        self.assertEqual(response.status_code, 200)
        expected_data = {'response_code': '200', 'response_desc': 'Success', 'parts': ['Obudowę', 'Płytę główną', 'Procesor', 'RAM', 'Zasilacz', 'Kartę graficzną', 'System chłodzenia']}
        self.assertEqual(response.json(), expected_data)

    # Test dla nieprawidłowego ID komputera
    def test_invalid_computer_id(self):
        computer_id = 'abcde'
        response = requests.get(f'{self.BASE_URL}?computer_id={computer_id}&type=basic')
        self.assertEqual(response.status_code, 500)

    # Test dla nieistniejącego ID komputera
    def test_nonexistent_computer_id(self):
        computer_id = 99999
        response = requests.get(f'{self.BASE_URL}?computer_id={computer_id}&type=basic')
        self.assertEqual(response.status_code, 404)

    # Test dla nieprawidłowej ścieżki
    def test_invalid_path(self):
        response = requests.get(f'{self.BASE_URL}?computer_id=')
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main(exit=False)
