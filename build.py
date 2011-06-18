#!/usr/bin/env python
import os
import optparse
from subprocess import check_call
import codecs

def main():
    p = optparse.OptionParser(usage='%prog [options]')
    (options, args) = p.parse_args()
    # check_call(['nosetests', '--with-doctest', '--doctest-extension=txt',
    #             './slides.txt'])
    output = './slides.html'
    check_call(['./custom_rst2s5.py', './slides.txt', './slides.html'])
    print "Wrote %s" % output

if __name__ == '__main__':
    main()
