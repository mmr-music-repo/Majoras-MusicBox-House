#!/usr/bin/env python

# isghj 11/2023
# this script quickly converters zseq music sequence files for MMR to mmrs format

from os import path, listdir
from datetime import datetime
import zlib, zipfile

def convert_file(file_path):
  # rip filename into parts
  # zseq uses underscore delimited parsing to separate three pieces of information:
  # filename_bankNum_categories-separated-by-comma.zseq
  # where the equivlent mmrs is a named zip file:
  #   the categories get their own file,
  #   the instrument is moved to the name of the zseq

  filename = path.basename(file_path)

  if filename.count('_') != 2:
    print(f'file [{filename}] has the wrong count of underscore, and is not parsable.')
    exit

  split_name = filename.split('_')
  zip_filename = f'{split_name[0]}.mmrs'
  new_zseq_name = f'{split_name[1]}.seq' # instrument.zseq
  categories = split_name[2][:-5] # remove ".zseq" filetype data, keep the rest, categories.txt can support command and dash delimit

  # create new timestamp file with the current time and the creation/modification data of the OG file
  #modification_date = datetime.fromtimestamp(path.getmtime(file_path))
  #current_date = datetime.now().replace(second=0, microsecond=0)
  #timestamp_string = f'this file was converted by script on [{current_date}] \nold zseq file was last modified [{modification_date}]'
  
  # try to zip it all together
  with zipfile.ZipFile(zip_filename, 'w') as mmrs:
    # create new files with strings
    mmrs.writestr("categories.txt", categories)
    #mmrs.writestr("creation.txt", timestamp_string)
    # write zseq, but change the name
    mmrs.write(file_path, new_zseq_name)
  

if __name__ == "__main__":
  import sys

  target_dir = "."

  if len(sys.argv) > 1:
    parameter = sys.argv[1]
    # if parameter is file, convert the one file
    if path.isfile(parameter):
      convert_file(parameter) 
      sys.exit() 
    # if parameter is directory, change default directory to match
    if path.isdir(parameter):
      target_dir = parameter

  list_of_files_in_dir = [file for file in listdir(target_dir) if file.endswith('.zseq')]
  print(f'Attempting to convert files: {list_of_files_in_dir}')
  for target_file in list_of_files_in_dir:
    convert_file(target_file)
  

