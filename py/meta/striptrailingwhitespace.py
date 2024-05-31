# I have a bunch of python files in a directory, and I want to remove trailing whitespace from all of them.
# Instead of doing it by hand, here's a script that does it for you.

import os

def remove_trailing_whitespace(directory: str) -> None:
    # Removes trailing whitespace from all .py files in a directory.
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            filepath = os.path.join(directory, filename)

        # Read the file content
        with open(filepath, "r") as infile:
            lines = infile.readlines()

        # Remove trailing whitespace from each line
        lines = [line.rstrip() for line in lines]

        # While last line is blank or contains only whitespace, remove it
        while lines and not lines[-1].strip():
            lines.pop()

        # Write the modified content back to the file
        with open(filepath, "w") as outfile:
            outfile.write("\n".join(lines))

    print(f"Successfully removed trailing whitespace from all .py files in '{directory}'.")