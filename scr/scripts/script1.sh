#!/bin/bash

# Functionality 1: Hello World
echo "Hello, welcome to ScriptSavvyHub!"

# Functionality 2: List files in the 'src' directory
echo "List of files in 'src' directory:"
ls src/

# Functionality 3: Create a new directory in the project
mkdir new_directory
echo "New directory 'new_directory' created."

# Functionality 4: Display system information
echo "System information:"
uname -a

# Functionality 5: Fetch current date and time
echo "Current date and time:"
date

# Functionality 6: Copy README.md to a backup file
cp README.md README_backup.md
echo "README.md copied to README_backup.md"

# Functionality 7: Print contents of main.py
echo "Contents of main.py:"
cat src/main.py

# Functionality 8: Process a sample CSV file (if available)
if [ -f data.csv ]; then
    echo "Processing data.csv file:"
    # Add your data processing commands here
    # Example: Calculate the number of lines in the file
    wc -l data.csv
else
    echo "No data.csv file found."
fi

# Functionality 9: Add more functionalities here...

#!/bin/bash

# Functionality 1: Hello World
echo "Hello, welcome to ScriptSavvyHub!"

# Functionality 2: List files in the 'src' directory
echo "List of files in 'src' directory:"
ls src/

# Functionality 3: Create a new directory in the project
mkdir new_directory
echo "New directory 'new_directory' created."

# Functionality 4: Display system information
echo "System information:"
uname -a

# Functionality 5: Fetch current date and time
echo "Current date and time:"
date

# Functionality 6: Copy README.md to a backup file
cp README.md README_backup.md
echo "README.md copied to README_backup.md"

# Functionality 7: Print contents of main.py
echo "Contents of main.py:"
cat src/main.py

# Functionality 8: Process a sample CSV file (if available)
if [ -f data.csv ]; then
    echo "Processing data.csv file:"
    # Add your data processing commands here
    # Example: Calculate the number of lines in the file
    wc -l data.csv
else
    echo "No data.csv file found."
fi

# Functionality 9: Display disk usage of the current directory
echo "Disk usage of the current directory:"
du -sh

# Functionality 10: List environment variables
echo "List of environment variables:"
printenv

# Functionality 11: Find and display all executable files in the project
echo "Executable files in the project:"
find . -type f -executable

# Functionality 12: Count the number of lines in all Python files in the 'src' directory
echo "Number of lines in Python files in 'src' directory:"
find src/ -name "*.py" -exec wc -l {} \; | awk '/total/{print $1}'

# Functionality 13: Add more functionalities here...

#!/bin/bash

# Functionality 1: Hello World
echo "Hello, welcome to ScriptSavvyHub!"

# Functionality 2: List files in the 'src' directory
echo "List of files in 'src' directory:"
ls src/

# Functionality 3: Create a new directory in the project
mkdir new_directory
echo "New directory 'new_directory' created."

# Functionality 4: Display system information
echo "System information:"
uname -a

# Functionality 5: Fetch current date and time
echo "Current date and time:"
date

# Functionality 6: Copy README.md to a backup file
cp README.md README_backup.md
echo "README.md copied to README_backup.md"

# Functionality 7: Print contents of main.py
echo "Contents of main.py:"
cat src/main.py

# Functionality 8: Process a sample CSV file (if available)
if [ -f data.csv ]; then
    echo "Processing data.csv file:"
    # Add your data processing commands here
    # Example: Calculate the number of lines in the file
    wc -l data.csv
else
    echo "No data.csv file found."
fi

# Functionality 9: Display disk usage of the project directory
echo "Disk usage of the project directory:"
du -sh

# Functionality 10: Check available memory
echo "Available memory:"
free -h

# Functionality 11: Display network information
echo "Network information:"
ifconfig -a

# Functionality 12: List running processes
echo "Running processes:"
ps aux

# Functionality 13: Show current user's home directory
echo "Current user's home directory:"
echo $HOME

# Functionality 14: Print system uptime
echo "System uptime:"
uptime

# Functionality 15: Show environment variables
echo "Environment variables:"
printenv

# Functionality 16: Show user login history
echo "User login history:"
last

# Functionality 17: Display the calendar
echo "Calendar:"
cal

# Functionality 18: Show users currently logged in
echo "Users currently logged in:"
who

# Functionality 19: Display file permissions for 'src' directory
echo "File permissions for 'src' directory:"
ls -l src/

# Functionality 20: Show the top CPU consuming processes
echo "Top CPU consuming processes:"
ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head

# Functionality 21: Check available disk space
echo "Available disk space:"
df -h

# Functionality 22: List installed packages (assuming Linux)
echo "Installed packages:"
dpkg -l

#!/bin/bash

# Functionality 1: Hello World
echo "Hello, welcome to ScriptSavvyHub!"

# Functionality 2: List files in the 'src' directory
echo "List of files in 'src' directory:"
ls src/

# Functionality 3: Create a new directory in the project
mkdir new_directory
echo "New directory 'new_directory' created."

# Functionality 4: Display system information
echo "System information:"
uname -a

# Functionality 5: Fetch current date and time
echo "Current date and time:"
date

# Functionality 6: Copy README.md to a backup file
cp README.md README_backup.md
echo "README.md copied to README_backup.md"

# Functionality 7: Print contents of main.py
echo "Contents of main.py:"
cat src/main.py

# Functionality 8: Process a sample CSV file (if available)
if [ -f data.csv ]; then
    echo "Processing data.csv file:"
    # Add your data processing commands here
    # Example: Calculate the number of lines in the file
    wc -l data.csv
else
    echo "No data.csv file found."
fi

# Functionality 9: Check available disk space
echo "Available disk space:"
df -h

# Functionality 10: Show top processes by CPU usage
echo "Top processes by CPU usage:"
ps -eo pid,ppid,cmd,%cpu --sort=-%cpu | head -n 5

# Functionality 11: List open ports
echo "Open ports:"
netstat -tuln

# Functionality 12: Display environment variables
echo "Environment variables:"
printenv

# Functionality 13: Show current user's login information
echo "Current user login information:"
who

# Functionality 14: Display memory usage information
echo "Memory usage information:"
free -m

# Functionality 15: List all installed packages
echo "Installed packages:"
if [ "$(command -v dpkg)" ]; then
    dpkg -l
elif [ "$(command -v rpm)" ]; then
    rpm -qa
else
    echo "Unable to determine the package manager."
fi

# Functionality 16: Show file permissions of main.py
echo "File permissions of main.py:"
ls -l src/main.py

# Functionality 17: Display the uptime of the system
echo "System uptime:"
uptime

# Functionality 18: Check the existence of a specific file or directory
if [ -d scripts/ ]; then
    echo "The 'scripts/' directory exists."
else
    echo "The 'scripts/' directory does not exist."
fi

# Functionality 19: Display the contents of a specific log file
log_file="app.log"
if [ -f "$log_file" ]; then
    echo "Contents of $log_file:"
    cat "$log_file"
else
    echo "The log file '$log_file' does not exist."
fi

# Functionality 20: Run a Python script
echo "Running a Python script:"
python src/script.py

# Functionality 21: Check system load average
echo "System load average:"
uptime | awk -F'average:' '{print $2}'

# Functionality 22: Create a symbolic link to a file
ln -s README.md symlink_readme.md
echo "Symbolic link 'symlink_readme.md' to README.md created."

# Functionality 23: Find and display all .txt files in the project
echo "Text files in the project:"
find . -type f -name "*.txt"

# Functionality 24: Display network interfaces
echo "Network interfaces:"
ip link show
