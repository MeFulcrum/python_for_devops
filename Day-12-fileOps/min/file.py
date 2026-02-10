"""
File Operations Module for Students
Demonstrates common file operations used in DevOps and system administration.
"""

import os
import shutil
import json
import csv
from pathlib import Path


# ============================================================================
# 1. BASIC FILE READING OPERATIONS
# ============================================================================

def read_entire_file(file_path):
    """
    Read the entire file content as a single string.
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        str: The entire file content, or None if file not found
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


def read_file_lines(file_path):
    """
    Read file content line by line (returns a list).
    Useful for processing large files line-by-line.
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        list: List of lines, or empty list if file not found
    """
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []


def read_file_stripped(file_path):
    """
    Read file and strip whitespace from each line.
    Good for config files or data processing.
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        list: List of stripped lines
    """
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []


# ============================================================================
# 2. BASIC FILE WRITING OPERATIONS
# ============================================================================

def write_to_file(file_path, content):
    """
    Write content to a file (overwrites if exists).
    
    Args:
        file_path (str): Path to the file
        content (str): Content to write
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"✓ Successfully wrote to '{file_path}'")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False


def append_to_file(file_path, content):
    """
    Append content to a file (creates if not exists).
    Useful for logging.
    
    Args:
        file_path (str): Path to the file
        content (str): Content to append
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file_path, 'a') as file:
            file.write(content + '\n')
        print(f"✓ Successfully appended to '{file_path}'")
        return True
    except Exception as e:
        print(f"Error appending to file: {e}")
        return False


def write_lines_to_file(file_path, lines):
    """
    Write a list of lines to a file.
    
    Args:
        file_path (str): Path to the file
        lines (list): List of strings to write
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        print(f"✓ Successfully wrote {len(lines)} lines to '{file_path}'")
        return True
    except Exception as e:
        print(f"Error writing lines to file: {e}")
        return False


# ============================================================================
# 3. FILE INFORMATION & EXISTENCE CHECKS
# ============================================================================

def file_exists(file_path):
    """
    Check if a file exists.
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        bool: True if file exists, False otherwise
    """
    return os.path.isfile(file_path)


def get_file_size(file_path):
    """
    Get file size in bytes. Returns -1 if file doesn't exist.
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        int: File size in bytes
    """
    try:
        return os.path.getsize(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return -1


def get_file_size_mb(file_path):
    """
    Get file size in MB (human-readable).
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        float: File size in MB
    """
    size_bytes = get_file_size(file_path)
    if size_bytes == -1:
        return 0
    return size_bytes / (1024 * 1024)


def get_file_extension(file_path):
    """
    Get file extension (e.g., '.txt', '.json').
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        str: File extension
    """
    return os.path.splitext(file_path)[1]


# ============================================================================
# 4. FILE OPERATIONS (Copy, Delete, Move)
# ============================================================================

def copy_file(src, dst):
    """
    Copy a file from source to destination.
    
    Args:
        src (str): Source file path
        dst (str): Destination file path
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        shutil.copy2(src, dst)
        print(f"✓ Successfully copied '{src}' to '{dst}'")
        return True
    except Exception as e:
        print(f"Error copying file: {e}")
        return False


def delete_file(file_path):
    """
    Delete a file (use with caution!).
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        os.remove(file_path)
        print(f"✓ Successfully deleted '{file_path}'")
        return True
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return False
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False


def rename_file(old_name, new_name):
    """
    Rename a file.
    
    Args:
        old_name (str): Current file path
        new_name (str): New file path
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        os.rename(old_name, new_name)
        print(f"✓ Successfully renamed '{old_name}' to '{new_name}'")
        return True
    except Exception as e:
        print(f"Error renaming file: {e}")
        return False


# ============================================================================
# 5. DIRECTORY & FILE LISTING OPERATIONS
# ============================================================================

def list_files_in_directory(directory_path):
    """
    List all files in a directory (non-recursive).
    
    Args:
        directory_path (str): Path to the directory
    
    Returns:
        list: List of file names
    """
    try:
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return sorted(files)
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
        return []


def list_subdirectories(directory_path):
    """
    List all subdirectories in a directory.
    
    Args:
        directory_path (str): Path to the directory
    
    Returns:
        list: List of subdirectory names
    """
    try:
        dirs = [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]
        return sorted(dirs)
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
        return []


def find_files_by_extension(directory_path, extension):
    """
    Find all files with a specific extension in a directory.
    
    Args:
        directory_path (str): Path to the directory
        extension (str): File extension to search for (e.g., '.txt', '.py')
    
    Returns:
        list: List of matching file paths
    """
    matches = []
    try:
        for file in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path) and file.endswith(extension):
                matches.append(file_path)
        return sorted(matches)
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
        return []


# ============================================================================
# 6. JSON FILE OPERATIONS
# ============================================================================

def read_json_file(file_path):
    """
    Read and parse a JSON file.
    
    Args:
        file_path (str): Path to the JSON file
    
    Returns:
        dict or list: Parsed JSON object, or None if error
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{file_path}'.")
        return None


def write_json_file(file_path, data, indent=2):
    """
    Write data to a JSON file.
    
    Args:
        file_path (str): Path to the JSON file
        data (dict or list): Data to write
        indent (int): JSON indentation level
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=indent)
        print(f"✓ Successfully wrote JSON to '{file_path}'")
        return True
    except Exception as e:
        print(f"Error writing JSON file: {e}")
        return False


# ============================================================================
# 7. CSV FILE OPERATIONS
# ============================================================================

def read_csv_file(file_path):
    """
    Read a CSV file into a list of dictionaries.
    
    Args:
        file_path (str): Path to the CSV file
    
    Returns:
        list: List of row dictionaries
    """
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []


def write_csv_file(file_path, fieldnames, rows):
    """
    Write data to a CSV file.
    
    Args:
        file_path (str): Path to the CSV file
        fieldnames (list): Column headers
        rows (list): List of dictionaries (one per row)
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"✓ Successfully wrote CSV to '{file_path}' with {len(rows)} rows")
        return True
    except Exception as e:
        print(f"Error writing CSV file: {e}")
        return False


# ============================================================================
# 8. DEMO / TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("FILE OPERATIONS DEMO FOR STUDENTS")
    print("=" * 70)
    
    # Demo 1: Create and read a text file
    print("\n--- Demo 1: Text File Operations ---")
    demo_file = "demo.txt"
    write_to_file(demo_file, "Hello, DevOps World!\nThis is line 2.\nThis is line 3.")
    print("Content:", read_entire_file(demo_file))
    
    # Demo 2: Append to file
    print("\n--- Demo 2: Append Operations ---")
    append_to_file(demo_file, "Appended line!")
    print("Lines:", read_file_lines(demo_file))
    
    # Demo 3: File info
    print("\n--- Demo 3: File Information ---")
    print(f"File exists: {file_exists(demo_file)}")
    print(f"File size: {get_file_size(demo_file)} bytes ({get_file_size_mb(demo_file):.2f} MB)")
    print(f"File extension: {get_file_extension(demo_file)}")
    
    # Demo 4: JSON operations
    print("\n--- Demo 4: JSON Operations ---")
    sample_data = {
        "servers": [
            {"name": "server1", "ip": "192.168.1.1", "status": "active"},
            {"name": "server2", "ip": "192.168.1.2", "status": "inactive"}
        ]
    }
    write_json_file("demo_config.json", sample_data)
    loaded = read_json_file("demo_config.json")
    print("Loaded JSON:", loaded)
    
    # Demo 5: CSV operations
    print("\n--- Demo 5: CSV Operations ---")
    csv_data = [
        {"name": "Alice", "role": "DevOps", "salary": "80000"},
        {"name": "Bob", "role": "Developer", "salary": "75000"},
    ]
    write_csv_file("demo_employees.csv", ["name", "role", "salary"], csv_data)
    csv_read = read_csv_file("demo_employees.csv")
    print("Loaded CSV:", csv_read)
    
    # Clean up
    print("\n--- Cleanup ---")
    delete_file(demo_file)
    delete_file("demo_config.json")
    delete_file("demo_employees.csv")
    print("✓ Demo complete! All temporary files deleted.")
