#!/usr/bin/env Python

import re
import os
import sys
import platform

from src.util import Settings
from src.logreader import reader
from src.threadreader import threadreader

def display_usage():
  print '*' * 66
  print 'I/O evaluation with FIO for parallel I/Os on many-core system'
  print 'Author: Junjie Qian (jqian.unl@gmail.com)'
  print '-' * 66
  print 'Usage: %s [options]'%sys.argv[0]
  print '  "workload_file": Set the test workload file path required'
  print '  logreader: Read the logs (path predefined, but subject to change)'
  print '  threadreader: Read the logs (logs without group_reporting)'
  print '*' * 66
  return

def main():
  if os.path.isfile(sys.argv[1]):
    util = Settings(sys.argv[1])
    util.run()
  else if sys.argv[1] == "logreader":
    logreader = reader("./workload/workload_numjobs.csv", "./Logs", "./IOSTATs")
    logreader.perf_read()
    logreader.iostat_read()
  else if sys.argv[1] == "threadreader":
    tr = threadreader("./workload/workload_numjobs.csv", "./Logs", "./IOSTATs")
    tr.perf_read()
  else:
    display_usage()

if __name__ == "__main__":
  if not platform.system() == "Linux":
    sys.exit("OS version not supported\n")
  if len(sys.argv) < 2:
    display_usage()
    sys.exit()
  main()
