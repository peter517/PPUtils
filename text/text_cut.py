#!/usr/bin/env python
# coding=utf8

s = 'hello'
print s.rfind('l')
try:
    text_cut_file = open("text_cut.txt", 'r')
    text_cut_lines = text_cut_file.readlines()
    ret_list = []
    for text_cut in text_cut_lines:
        text_cut_result = text_cut[0 : text_cut.rfind(',')]
        # print text_cut_result
        ret_list.append(text_cut_result + "\n")
finally:
    text_cut_file.close()

fo = open("text_cut_result.txt", "w")
fo.writelines(ret_list)
fo.close()