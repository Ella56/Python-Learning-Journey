#imports and global variables

from pathlib import Path

import shutil


base_dir = Path(r"D:\Test")
target_dir = base_dir / "sorted"

#Categories and Extensions

catgories = {
    "images":[".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "documents":[".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "vidoes":[".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "audio":[".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "archives":[".zip", ".rar", ".tar", ".gz", ".7z"]
    }



#Create Dir4ectories base on categories

def create_category_directories():
    
    for category,_ in catgories.items():
        (target_dir / category ).mkdir(parents=True,exist_ok=True)
    



#Searchin and categorizing files

def search_categorize_files():
   for file in  base_dir.rglob("*"):
       for category,extensions in catgories.items():
           if file.suffix in extensions:
               try:
                   shutil.copy(file, target_dir / category)
               except shutil.SameFileError:
                   pass



#Run the application

create_category_directories()
search_categorize_files()















