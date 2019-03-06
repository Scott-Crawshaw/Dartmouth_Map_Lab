# Scott Crawshaw
# 3/6/19
# stack_extra.py
# Lab 4 Extra Credit


class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        return self.stack_list.pop()

    def __len__(self):
        return len(self.stack_list)
