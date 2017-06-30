# the_Programmer
by TeeJ Lockwood

## Reading Index
  %word% - this denotes that "word" is a definition
  ... - means continue the process listed before (1, 2, 3, ... = 1, 2, 3, 4, ... <> 1, 2, 4, ... = 1, 2, 4, 8, ...)
  A_1, A_2, ... - this denotes there are multiple definitions of type A and are referenced by the index _1, _2, ...

## Directory Blueprints

A directory is very important to a programmer. It is his library. His list of files, programs, pictures, and any other form of data or machine. So it is very important to have a clean directory, unless living dirty is your style. However not knowing what you have or where the things I use day to day is not my style. So I have decided to try to create a library. I suppose this is a list of the possible blueprints.

f a %file%:
    
    Let f be a %file%, then
    
      i)    f contains no elements - it cannot be a set, and it is always an element of a set
      ii)   f.parent() - belongs to a %folder%
      iii)  f.name() - f has a name
      iv)   f.path() - f has a path (within a directory which folders it is located)
      v)    f.date() - f has a due date
      vi)   f.size() - f has a size
      vii)  f.type() - f has a type
      viii) f.ldate() - f has a last edited date
      ix)   f.length() - f has a number of folders it is contained in

F a %folder%:
    
    Let F be a %folder% [f_1, f_2, f_3, f_4, ...], then
    
      i)    F_0 = [f_1, f_2, f_3, ...,
                   F_1, F_2, F_3  ...] - F contains files and folders
      ii)   F.contains() - is the list of files/folders
      iii)  F.size() - is the size of all of the files
      iv)   F.space() - is the maximum size it may have
      v)    F.length() - is the sum of the the length of every file's path
      vi)   F.count() - is the number of files within every folder of
      
    Note: Any %folder% may contain other folders
    We will call the set of all %folder%s the directory, or D for short.
 
Directory Types

1. Task-Oriented Directory
    A task oriented Directory is a directory that organizes all of the files based on some different tasks. Let us call this TO-D style directories for short. A TO-D style directory is good for a work scenario.
    
    That is we have our directory D that contains all of our files and folders. We can distinguish every file and folder with a %key%
    key(f_i) = (type, date, ldate, size, path) 
    key(F_i) = (size, space, length, count, path)
     
