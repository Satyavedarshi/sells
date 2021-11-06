# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import unittest, pytest

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


class testClass(unittest.TestCase):
    def test_test1(self):
        print('First test case')
        assert True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    unittest.main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
