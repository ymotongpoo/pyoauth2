# -*- coding: utf-8 -*-

import sys
from subprocess import Popen, STDOUT
import os.path

def suite():
    cmd = ['py.test', '-r']
    
    cmd.append(os.path.dirname(os.path.abspath(__file__)))
    errno = Popen(cmd, stdout=sys.stdout, stderr=STDOUT).wait()
    raise SystemExit(errno)

if __name__ == '__main__':
    suite()
