#!/usr/bin/env python3

# BNF config yaml
#
# LANG  = NODES..
# NODES = ["\t"..] ( FILE | DIR )
# FILE  = NAME "." EXT "\n"
# DIR   = NAME ":\n"
# NAME  = char [ char | num ]..
# EXT   = ( char | num )..


def make_project(glb_tab, stryct, root):

    if glb_tab != -1 and not os.path.exists(root):
        os.mkdir(root)
    #print(f"make folder {root}")
    os.chdir(root)
    n_stryct = []
    inside_dir = None
    for i, (node_name, line_tab, is_dir) in enumerate(stryct):

        if inside_dir:
            if inside_dir[1] < line_tab:
                #print(f"in {inside_dir[0]} {node_name}")
                n_stryct.append((node_name, line_tab, is_dir))
                if i == len(stryct) - 1:
                    make_project(inside_dir[1], n_stryct,
                                 os.path.join(root, inside_dir[0]))
            elif inside_dir[1] == line_tab and is_dir:
                #print(f"put stack in {inside_dir[0]} in {root}")
                make_project(inside_dir[1], n_stryct,
                             os.path.join(root, inside_dir[0]))
                os.chdir(root)
                inside_dir = (node_name, line_tab)
                n_stryct = []

            else:
                #print(f"make folder {inside_dir[0]}")

                if not is_dir:
                    n_stryct.append((node_name, line_tab, is_dir))

                make_project(inside_dir[1], n_stryct,
                             os.path.join(root, inside_dir[0]))
                os.chdir(root)
                inside_dir = (node_name, line_tab) if is_dir else None

        elif is_dir:
            #print(f"find dir {node_name}")
            inside_dir = (node_name, line_tab)
        else:
            open(node_name, "a").close()
            #print(f"create file {node_name} in {root}")


if __name__ == "__main__":

    import sys
    import os

    # image if file not big
    with open("./config.yaml", "r", encoding="utf-8") as conf_text:
        conf = map(lambda x: (
            x.strip().replace("\t", "  ").replace(":", ""),
            x.rstrip().count(" "),
            x.find(":") > 0
        ), conf_text.readlines())

    make_project(-1, list(conf), os.getcwd())

    exit(0)