# Add an arbitrary comment to the end of all .py files in a folder

import os

def add_comment(folder_path: str, comment: str) -> None:
  """
  Adds the specified comment to the end of all .py files in a folder.

  arguments:
    folder_path: The path to the folder containing the .py files.
    comment: The comment string to be added.
  """

  for filename in os.listdir(folder_path):
    if filename.endswith(".py"):
      filepath = os.path.join(folder_path, filename)
      # Read the entire file content
      with open(filepath, "r") as infile:
        file_content = infile.read()

      # Add the comment at the end with a newline
      new_content = file_content + "\n# " + comment

      # Open the file again in write mode (overwrites existing content)
      with open(filepath, "w") as outfile:
        outfile.write(new_content)

  print(f"Successfully appended '\\n# {comment}' to all .py files in '{folder_path}'.")

folder_path = "C:/Users/admin/Documents/GitHub/Curricular/pythonlab "
comment = "Enhance your skills with more free code samples at example.com!"
add_comment(folder_path, comment)
