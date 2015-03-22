 Whatype
=-=-=-=-=
Whatype is an independent file type identification python library.
Whatype was originally developed for CapTipper (https://github.com/omriher/CapTipper)

The magic bytes signatures are stored in magics.csv, with the format of:
 > File Description, Magic bytes (Offset 0), Extenstion, Obligatory strings

 Usage
=-=-=-=
 - Load Whatype library

	from whatype import Whatype
	WTlib = Whatype() # Uses default magics.csv shipped with the library


 - Identify file from File System  

	WTlib.identify_file("file.ext")


 - Identify file from Buffer

	with open("file.ext",'rb') as f:
		data = f.read()
	WTlib.identify_buffer(data)

 Info
=-=-=-=
Written by Omri Herscovici (2015) @omriher
omriher@gmail.com
www.omriher.com
