'''
Created on May 6, 2021

@author: garycalvin
'''
import unittest
import basic


class TestBasic(unittest.TestCase):

    def test_token(self):
        token = basic.Token(basic.TT_INT, 1)
        assert basic.Token == type(token)
        assert token.type == basic.TT_INT
        assert token.value == 1
        assert repr(token) == 'TT_INT:1'

        token = basic.Token(basic.TT_LPAREN)
        assert repr(token) == 'LPAREN'


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'TestBasic.test_basic']
    unittest.main()
