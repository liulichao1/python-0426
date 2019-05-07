#!/user/bin/env python
# _*_ coding: UTF-8 _*_

"""This is a demo module..."""

__author__='Tom'

import sys


def _fn_private():
    print('This is a private function...')


def fn_test():
    print(sys.argv)
    _fn_private()

if __name__ == '__main__':
    fn_test()
