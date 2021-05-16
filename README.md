# Obsidian File Link Converter (To standard Markdown style)

When inserting image in Obsidian, default format will be:

```
![[image.png]]
```

This code is able to convert the file link with Obsidian style into standard Markdown style

``` 
![[image.png]] => !()[image.png]
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