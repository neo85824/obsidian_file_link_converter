import os
import sys
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="output path", default="output")
parser.add_argument("path", help="foler/files location")

args = parser.parse_args()

def main():
    if not os.path.exists(args.output):
        os.mkdir(args.output) 

    if os.path.isdir(args.path):
        convert(args.path, args.output)
    else:
        convert_file(os.path.basename(args.path), os.path.dirname(args.path), args.output)

def convert(file_path, out_path):
    for root, dirs, files in os.walk(file_path):
        print("\nProcess Folder: ", root)
        sub_root = os.path.sep.join(root.split(file_path)[1].split(os.path.sep)[1:])
        tmp_out_path = os.path.join(out_path, sub_root)

        if not os.path.exists(tmp_out_path):
            os.mkdir(tmp_out_path)
            
        for file in files:
            if file.endswith(".md"):
                convert_file(file, root, tmp_out_path)
    

def convert_file(file_name, file_path, out_path):    
    link_pattern = re.compile("!\[\[(?P<url>.*)\]\]")

    lines = []
    with open(os.path.join(file_path, file_name), "r", encoding="utf-8") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            match = re.search(link_pattern, line)
            if match is not None:
                url = match.group("url")
                replaced = "![](" + url + ")"
                new_line = line.replace(match.group(), replaced)
                lines[i] = new_line

    with open(os.path.join(out_path, file_name), "w", encoding="utf-8") as f:
        f.writelines(lines)
        print("Write {} to {}".format(file_name, out_path))
        

if __name__ == '__main__':
    main()