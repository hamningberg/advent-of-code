from pathlib import Path

class FS_Directory:
    def __init__(self, name, fs_parent_dir):
        self.name = name
        self.fs_parent_dir = fs_parent_dir
        self.fs_sub_dirs = {}
        self.fs_files = []
        self.size = 0

# The puzzle does not need objects for the files
#class FS_File:
#    def __init__(self, name, size):
#        self.name = name
#        self.size = size


# Root directory
fs_root = FS_Directory("/", None)

# This list of all directories is the poor man's substitute to traversing the directory tree
fs_dirs_all = [fs_root]

# Read input file and build directory tree
with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    fs_curr_dir = fs_root
    for line in input_file:
        # Lines starting with "$ ls" and "dir" are not relevant for the puzzle
        if line == "$ cd ..\n":
            fs_curr_dir = fs_curr_dir.fs_parent_dir
        elif line.startswith("$ cd "):
            new_dir_name = line[5:-1]
            if new_dir_name != "/":
                if not new_dir_name in fs_curr_dir.fs_sub_dirs:
                    fs_dir_new = FS_Directory(new_dir_name, fs_curr_dir)
                    fs_curr_dir.fs_sub_dirs[new_dir_name] = fs_dir_new
                    fs_dirs_all.append(fs_dir_new)
                fs_curr_dir = fs_curr_dir.fs_sub_dirs[new_dir_name]
        elif line[0].isdigit():
            file_size_and_name = line.split(" ")
#            fs_curr_dir.fs_files.append(FS_File(file_size_and_name[1], int(file_size_and_name[0])))
            sub_dir = fs_curr_dir
            while sub_dir:
                sub_dir.size += int(file_size_and_name[0])
                sub_dir = sub_dir.fs_parent_dir

# Part 1
sum_sizes_dirs_lt_100k = 0

# Part 2
space_needed = fs_root.size - 40000000
optimal_dir_size = fs_root.size

# Compute results
for d in fs_dirs_all:
    if d.size < 100000:
        sum_sizes_dirs_lt_100k += d.size
    if space_needed < d.size < optimal_dir_size:
        optimal_dir_size = d.size

print("Result Part 1: ", sum_sizes_dirs_lt_100k)
print("Result Part 2: ", optimal_dir_size)
