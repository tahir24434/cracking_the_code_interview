#!/usr/local/bin/python3


def exec_cmd(cmd, stack):
    op = cmd[0]
    if op == 1:
        # Push
        elem_to_push = cmd[1]
        stack.append(elem_to_push)
    elif op == 2:
        # Delete element
        stack.pop()
    elif op == 3:
        # Print Maximum element in stack
        print (max(stack))


if __name__ == "__main__":
    N = int(input())
    my_stack = []
    for i in range(N):
        cmd_arr = [int(x) for x in input().strip().split()]
        exec_cmd(cmd_arr, my_stack)
