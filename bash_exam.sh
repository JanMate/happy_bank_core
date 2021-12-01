#!/bin/bash

# Added color variables
RED='\033[0;31m'
NC='\033[0m'

# Add announcement that this script has just started with timestamp
echo "Script has started at $(date +%T)"

# Create a new "working_dir" variable and set it as a current directory
working_dir=$(pwd)
echo -e "Current working directory: ${RED} $working_dir ${NC}"

# In your working dir, create nested directory structure "src/main/module" (discover the -p argument in mkdir command)
mkdir -p src/main/module

# Create a new empty file ".gitkeep" in the "module" folder created in previous step
touch src/main/module/.gitkeep

# List the "module" directory mentioned in the previous step and the result store to a new variable
module_dir_list=$(ls -a src/main/module)

# Check if the "module" directory is empty. If so or not, show a meaningful message about it
if [[ -z "$module_dir_list" ]]; then
	echo -e "${RED}Module${NC} directory is empty"
else 
	echo -e "${RED}Module${NC} directory is not empty"
fi 

# In your working directory create a new empty file "setup.ini"
touch setup.ini

# You noticed you had wanted to create the "setup.ini" file to "module" folder, but you placed it to the working directory.
# So move the file there
mv setup.ini src/main/module

# Your teammate warned you that the "src/main" is not standardized path and he asked you to remove it.
# The content must be saved, and placed in the working directory
mv src/main/module "$working_dir"
rm -rf src

# Fill "setup.ini" file with "user=admin" value
cd module || exit
echo 'user=admin' > setup.ini
setup_ini_content=$(cat setup.ini)

# Print the content of the file from previous step for check and add a message about the file name before (A user always wants to be informed what's happening)
echo -e "Following content has been added to setup.ini file:\n${RED}$setup_ini_content ${NC}"

# Count a number of the lines of the file mentioned in previous step and verify if it's equal to 1. If not, show a warning to user.
number_of_lines=$(wc -l < setup.ini)

if [[ $number_of_lines != 1 ]]; then
	echo "Number of lines in setup.ini file is not equal to 1"
else 
	echo "Number of lines is equal to 1"
fi 

# Show a message about the script's processing and sleep for 5 seconds
echo "Script is processing, please wait"
sleep 5

# Remove "module" folder with its content and inform a user about it
cd "$working_dir" || exit
rm -rf module
echo -e "${RED}module${NC} folder has been removed"

# Add announcement that this script has just finished with timestamp
echo "Script ended at $(date +%T)"
