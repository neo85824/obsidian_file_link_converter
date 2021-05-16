# Obsidian File Link Converter (To standard Markdown style)
Convert the file link with Obsidian style into standard Markdown style

``` 
![[url]] => !()[url]
```

## Installation
Requirements
* Python 3+

## Usage

Given the folder or file, convert them into standard Markdown style.

* If `file_path` is folder, it will convert all the `.md` files in the folder recursively.

```
python converter.py -o <output_path> <file_path>
```
