import sys
import os


class ReplaceStringStep:
    def __init__(self, file_path, search, replace):
        self.file_path = file_path
        self.search = search
        self.replace = replace

    def process(self):
        with open(self.file_path, 'r') as fd:
            file_content = fd.readlines()
            for i in range(len(file_content)):
                file_content[i] = file_content[i].replace(self.search, self.replace)
            with open(self.file_path, 'w') as fr:
                fr.writelines(file_content)


def run(file_path, search, replace):
    try:
        string_replacer = ReplaceStringStep(file_path, search, replace)
        string_replacer.process()
    except Exception as e:
        print(e)
        exit(0)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("File path is empty")
        print("Search is empty!")
        print("Replace is empty!")
        exit(1)
    if sys.argv[1] == "":
        print("File path is empty")
        exit(1)
    if sys.argv[2] == "":
        print("Search is empty!")
        exit(1)
    if sys.argv[3] == "":
        print("Replace is empty!")
        exit(1)
    run(sys.argv[1], sys.argv[2], sys.argv[3])