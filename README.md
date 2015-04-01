# Whatype
Whatype is an independent file type identification python library.  
Whatype was originally developed for [CapTipper](https://github.com/omriher/CapTipper)

The magic bytes signatures are stored in magics.csv, with the format of:
> File Description, Magic bytes (Offset 0), Extenstion, Obligatory strings

## Usage
Load Whatype library
```python
from whatype import Whatype
WTlib = Whatype() # Uses default magics.csv shipped with the library
```

Identify file from FileSystem  
```python
print WTlib.identify_file("file.ext")
```

Identify file from Buffer
```python
with open("file.ext",'rb') as f:
  data = f.read()
print WTlib.identify_buffer(data)
```

Results returns in the form of a tuple:  
```python
(File Description, File Extenstion)
```

**Example**
```python
>>> from whatype import Whatype
>>> WTlib = Whatype()
>>> WTlib.identify_file("C:\\BinaryFile.exe")
('Windows executable file', 'EXE')

>>> with open(r"C:\\java-archive.jar",'rb') as f:
...     cont = f.read()
...
>>> WTlib.identify_buffer(cont)
('Java archive', 'JAR')
```

**Installation**
```python
setup.py install
```

## Info
Written by Omri Herscovici (@omriher)  
omriher@gmail.com  
[omriher.com](http://www.omriher.com)
