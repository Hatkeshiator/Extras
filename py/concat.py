# I just realized I can't just rizz my professors into giving me the highest grade for being handsome and dashing and need to actually submit proof of my work. Oh no!
# Thankfully, I *do*, have the work. But, it's in 198237 different files! Oh no!
# I *have* numbered them, but copy-pasting everything into one text file just sounds like hell. Whatever shall I do?
# Here's your answer. If you've numbered them, this script will concatenate them all into one file, in order. Just run it and you're good to go!
# Special thanks to GitHub Copilot and Google Gemini for teaching me how some of this stuff works.

import os
import re

def sort_numeric(filenames):
  """
  Sorts filenames numerically based on the number in the filename.
  """
  return sorted(filenames, key=lambda x: int(re.search(r'\d+', x).group()))

def concatenate_py_files(directory, output_file):
  """
  Concatenates all .py files in a directory to a single output file, 
  ordered by the number in the filename.
  """
  filenames = [f for f in os.listdir(directory) if f.endswith('.py')]
  filenames = sort_numeric(filenames)

  with open(output_file, 'w') as outfile:
    for filename in filenames:
      filepath = os.path.join(directory, filename)
      with open(filepath, 'r') as infile:
        outfile.write(infile.read() + '\n\n')  # Add a newline between files

def main():
  directory = 'C:/Users/admin/Documents/GitHub/Curricular/pythonlab'
  output_file = 'C:/Users/admin/Documents/GitHub/Curricular/pythonlab/concat.txt'
  concatenate_py_files(directory, output_file)
  print(f"Python files concatenated to {output_file}")

if __name__ == '__main__':
  main()
