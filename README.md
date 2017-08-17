# the_Programmer
by TeeJ Lockwood

## Directory Blueprints

A directory is very important to a programmer. It is his library. His list of files, programs, pictures, and any other form of data or machine. So it is very important to have a clean directory, unless living dirty is your style. However not knowing what you have or where the things I use day to day is not my style. So I have decided to try to create a library. I suppose this is a list of the possible blueprints.

f a file:
    
    Let f be a file, then
    
      i)    f contains no elements - it cannot be a set, and it is always an element of a set
      ii)   f.parent() - belongs to a %folder%
      iii)  f.name() - f has a name
      iv)   f.path() - f has a path (within a directory which folders it is located)
      v)    f.date() - f has a due date
      vi)   f.size() - f has a size
      vii)  f.type() - f has a type
      viii) f.ldate() - f has a last edited date
      ix)   f.length() - f has a number of folders it is contained in

F a folder:
    
    Let F be a folder [f_1, f_2, f_3, f_4, ...], then
    
      i)    F_0 = [f_1, f_2, f_3, ...,
                   F_1, F_2, F_3  ...] - F contains files and folders
      ii)   F.contains() - is the list of files/folders
      iii)  F.size() - is the size of all of the files
      iv)   F.space() - is the maximum size it may have
      v)    F.length() - is the sum of the the length of every file's path
      vi)   F.count() - is the number of files within every folder of
      
    Note: Any folder may contain other folders
    We will call the set of all %folder%s the directory, or D for short.
 
Directory Types

1. Task-Oriented Directory
    A task oriented Directory is a directory that organizes all of the files based on some different tasks. Let us call this TO-D style directories for short. A TO-D style directory is good for a work scenario. The beauty of this type of Directory is that we can name the files and folders based on given dates. So whenever the files are sorted they can be sorted by the date they are produced for. Furthermore whenever these files/folders are sorted by name the most recent folder/file is on top. The older files are on the bottom and the list goes on. As the list grows large we can create an "Archive" folder at the bottom. We can then chop the list to any size that we feel by putting the excess files/folders into the archive folder. Hopefully they will be files so there will be less of a f.legnth(). Then the files will be sorted within the archive folder if any older dated files need to be retrieved. How exciting!
     
     An example of how the file names would look for a task called Lawn Mowing could be as follows:
     
       Lawn Mowing [Folder]
        
           
            
            2017 04-01_Lawn Mowing_Workbook.xlsx
            
            2017 03-01_Lawn Mowing_Workbook.xlsx
            
            2017 02-01_Lawn Mowing_Workbook.xlsx
            
            2017 01-01_Lawn Mowing_Workbook.xlsx
            
            
           Archive [Folder]
            
                2016 12-01_Lawn Mowing_Workbook.xlsx
                
                2016 11-01_Lawn Mowing_Workbook.xlsx
                
                2016 10-01_Lawn Mowing_Workbook.xlsx
                
                ...
                
                
As we can see the most recent files are on top whenever we sort the folders by name. As the list grows old the files stack towards the bottom. As the stack grows long we simply dump the lower end of the stack into the Archive folder. The Archive folder holds all of the prior files. They are sorted by date so there is a way to navigate around the folder.
    
As far as I know Microsoft hasn't implemented a method to shift the name to where we can switch workbook with the date, but that would make our folder even more organized. It would allow for sorting the files with more than just the date. However on the bright side microsoft does allow to sort by last changed date and size of the file.
    
This so far is my favorite way to name my financial reports. The reason is becaue it is super organized and it allows growth for optimizing each task. By splitting each folder into each task I must do it helps me keep all of my thoughts in one place. Of course the best way to organize data imo is on one big server and then pulling the report directly. However this can take very long for each report to pull. Thus this is the machine learning way of doing the report. It is quicker, but it lacks flexibility.
    
One day I would like to build a system where the information is in one place and any analysis I would like to pull can be pulled directly from the server. Like running a report with an sql statement. But I need the report to have pictures. Everything just makes more sense with pictures right?
