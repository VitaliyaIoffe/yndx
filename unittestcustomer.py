import unittest


class TestStringMethods(unittest.TestCase):

    def test_is_retired(self) -> None:
        """Test our person is retired or not

        Be careful with our change to new limits of being retired
        """
        # for i in range(0, 6):
        #             with self.subTest(i=i):
        #                 self.assertEqual(i % 2, 0)

        pass

# here is a lot of unittests, but im too lazy to implement them


if __name__ == '__main__':
    unittest.main()