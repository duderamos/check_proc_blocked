#!/usr/bin/env python

import getopt, sys
import os

def version():
        print 'check_proc_blocked.py 0.1'
        print 'Eduardo Ramos <eduardo@freedominterface.org>'
        sys.exit(3)

def usage():
        print 'check_proc_blocked.py [-v]'
        sys.exit(3)

def main():
        cmd = 'ps -eo state'
        count = 0

        try:
                opts, args = getopt.getopt(sys.argv[1:], 'vh')
        except getopt.GetoptError as err:
                print str(err)
                usage()
                sys.exit(3)
                
        for o, a in opts:
                if o == '-v':
                        version()
                else:
                        usage()
                        assert False, 'unhandled option'

        pd = os.popen(cmd, 'r', 10240)
        for line in pd:
                if 'D' in line:
                        count = count + 1

        print "# PROCS OK - {0} processes with STATE = D|Blocked={0}".format(count)
        sys.exit(0)

if __name__ == '__main__':
        main()
