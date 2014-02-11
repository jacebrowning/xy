<!-- curmit: https://docs.google.com/document/d/1OHygs-Fhn7rT2hVctUilsciJ8BQLqwR5ZcqzDVowIyA/pub?embedded=true -->



# Name | CLI

TextToBlob | ttb

Chunky | chunk

Gob | gob

Globby | globby

? | dab

Dollop | lop

Blobby | blob, lob

? | xit ("exit")

Exit | xx

Xxit | xx

A SuperDuper Fileconverter | asdf

WordToFile | wtf

? | xyml, xy

X-to-Y | xy, xtoy

X2Yaml, XtoYaml, X2YAML | xy

ThereAndBack | hobbits, bilbo, baggins

# Similar Tools

 - [http://wizard.ae.krakow.pl/~jb/xls2txt/](http://wizard.ae.krakow.pl/~jb/xls2txt/)  
 - [http://manns.github.io/pyspread/](http://manns.github.io/pyspread/)  
# Notes

 - HTML can be embedded in Markdown for tables  
- GitHub flavored markdown includes tables?  
| Yes  |

|------|

|  it  |

| does |

# Basic Usage

 1. `ttb TextyFile.text`  
 2. ttb creates /tmp/BlobbyFile.binary or finds and old copy to update  
 3. ttb opens BlobbyFile.binary in its default editor  
 4. when the default editor closes, btt converts the content back to TextyFile.text  
# Supported Conversions

YAML to:

 - XLS  
 - XLSX  
 - CSV  
 - DOC  
 - DOCX  
# File Format

Notes:

 1. all text is Markdown  
Example:

   - format: XLS  
   - content:  
     - header:  
          abc  
          def  
     - row  
        - "hello"  
       - 42.0  
# Command-line Interface

Commands:

Very simple, pass in files. Those with a *.yml extension are converted to a
temp word/excel format and opened for editing. Files with *.docx and *.xlsx
are auto converted to a *.yml file of the same basename.
