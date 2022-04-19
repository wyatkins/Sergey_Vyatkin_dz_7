#!/usr/bin/env python3

import os
import sys
import time

size = {}

def scan_mem(pth):

    for root, _, files in os.walk(pth):
        for file in files:
            correct_file = os.path.join(root, file)
            mem = 10 ** len(str(os.stat(correct_file).st_size))
            size[mem] = size.get(mem, 0) + 1


def scan_mem_recursion(pth):

    if not os.path.exists(pth):
        return
    with os.scandir(pth) as files:

        for node in files:

            if os.path.isfile(node):

                mem = 10 ** (len(str(os.stat(node).st_size)) - 1)
                size[mem] = size.get(mem, 0) + 1
            elif os.path.isdir(node):
                scan_mem(os.path.join(pth, node))


if __name__ == "__main__":

    if len(sys.argv) == 2:
        pth = sys.argv[1]
    else:
        pth = os.getcwd()
    print(f"{'soution with os.walk':^39}")
    time_now = time.perf_counter()
    scan_mem(pth)
    print(size, f"\n as { time.perf_counter() - time_now}")

    size = {}
    print(f"{'soution with resursion':^39}")
    time_now = time.perf_counter()
    scan_mem_recursion(pth)
    print(size, f"\n as { time.perf_counter() - time_now}")