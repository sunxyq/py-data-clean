#coding=utf-8
def count_lines(file_name):
    file = open(file_name, 'r')
    return len(file.readlines())
