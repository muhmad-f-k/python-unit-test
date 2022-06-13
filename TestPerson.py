import unittest
from person import Person


class TestAllowedToEnter(unittest.TestCase):
    def setUp(self) -> None:
        self.__person = Person()

    def tearDown(self) -> None:
        del self.__person

    def test_age_to_enter(self):
        self.assertEqual(True, self.__person.allowed_to_enter(25))

    def test_age_to_deny(self):
        self.assertEqual(False, self.__person.allowed_to_deny(19))


if __name__ == "__main__":
    unittest.main()
