#!/usr/bin/env python
# coding=utf8


file_object1 = open("diff_src.txt", 'r')
file_object2 = open("diff_target.txt", 'r')

try:
    src = file_object1.readlines()
    target = file_object2.readlines()
    ret_list = []
    target_no_spacial_char = []
    src_no_spacial_char = []

    for item in target:
        target_no_spacial_char.append(item.strip('\n'))
    for item in src:
        src_no_spacial_char.append(item.strip('\n'))

    for item in target_no_spacial_char:
        if item not in src_no_spacial_char:
            ret_list.append(item)
finally:
    file_object1.close()
    file_object2.close()


print len(src)
print len(target)

print len(ret_list)
print 1 - ((float)(len(ret_list)) / len(target))

fo = open("diff_not_include.txt", "w")
for item in ret_list:
    fo.write(item + "\n")
fo.close()

