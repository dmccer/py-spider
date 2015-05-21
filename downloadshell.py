#!/usr/bin/env python
# encoding: utf-8

# 简单地文件下载脚本

import os
import sys, re

def read_file(filename):
    down_links = []
    with open(filename, 'r') as my_file:
        for url in my_file:
            down_links.append(url.replace('\n', ''))

    return down_links

def main():
    if len(sys.argv) != 2:
        print 'Please input file name...'

    down_links = read_file(sys.argv[1])
    pdf_index = 1

    for index, link in enumerate(down_links):
      if link.find('pdf') != -1:
          os.system('curl ' + link + ' -o %d.pdf' % pdf_index)
          pdf_index += 1
      else:
          print '请自行不全下载命令...'

if __name__ == '__main__':
    main()


