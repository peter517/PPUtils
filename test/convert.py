#!/usr/bin/env python
# -*- coding: utf-8 -*-


convert_test_output = []

try:
    fo = open("convert_test_output.txt", "w")
    file_object1 = open("convert_test.txt", 'r')
    convert_src_list = file_object1.readlines()
    for convert_src in convert_src_list:
        new = convert_src.decode('unicode_escape')
        fo.write(new.encode("utf-8"))
        convert_test_output.append(new)

finally:
    file_object1.close()
    fo.close()

print convert_test_output

