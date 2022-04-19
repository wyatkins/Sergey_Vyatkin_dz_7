#!/usr/bin/env python3

import os

folder_struct = {
    "my_project": [
        {
            "settings": [{"bar": [], "foo":[]}],
            "mainapp": [],
            "adminapp": [],
            "authapp": []
        }]
}


def project_starter(pth, struct):

    for fold_node, ch_node in struct.items():

        test_path = os.path.join(pth, fold_node)

        if not os.path.exists(test_path):
            os.mkdir(test_path)

        if len(ch_node) > 0:
            for node in ch_node:
                project_starter(test_path, node)


if __name__ == "__main__":

    project_starter(os.getcwd(), struct=folder_struct)