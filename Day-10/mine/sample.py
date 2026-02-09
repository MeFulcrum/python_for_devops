"""
Day-10: Lists Part-2
Demonstrates:
1. Converting strings to lists
2. Using main construct (__main__)
3. Listing files in folders
4. Error handling
"""

import os

# ==========================================
# 1. Converting String to List
# ==========================================
def convert_string_to_list():
    """Convert a space-separated string into a list"""
    print("\n--- 1. Convert String to List ---")
    
    # Using split() to convert string to list
    input_string = "folder1 folder2 folder3 folder4"
    folders = input_string.split()
    print(f"Input string: {input_string}")
    print(f"Converted list: {folders}")
    print(f"List length: {len(folders)}")
    
    # Another example with different delimiter
    csv_data = "apple,banana,orange,grape"
    fruits = csv_data.split(',')
    print(f"\nCSV string: {csv_data}")
    print(f"Fruits list: {fruits}")


# ==========================================
# 2. Interactive Input - String to List
# ==========================================
def interactive_input_example():
    """Get user input and convert to list"""
    print("\n--- 2. Interactive Input Example ---")
    
    user_input = input("Enter folder paths separated by spaces: ")
    folder_list = user_input.split()
    
    print(f"You entered {len(folder_list)} folders:")
    for idx, folder in enumerate(folder_list, 1):
        print(f"  {idx}. {folder}")


# ==========================================
# 3. List Files in Folder
# ==========================================
def list_files_in_folder(folder_path):
    """
    List all files in a given folder path
    Returns: (files_list, error_message)
    """
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, f"Folder not found: {folder_path}"
    except PermissionError:
        return None, f"Permission denied: {folder_path}"
    except Exception as e:
        return None, f"Error: {str(e)}"


# ==========================================
# 4. List Files in Multiple Folders
# ==========================================
def list_files_in_multiple_folders(folder_paths):
    """List files in multiple folders provided as input"""
    print("\n--- 3. List Files in Folders ---")
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        
        if files:
            print(f"\nFiles in '{folder_path}': ({len(files)} items)")
            for idx, file in enumerate(files, 1):
                print(f"  {idx}. {file}")
        else:
            print(f"Error in '{folder_path}': {error_message}")


# ==========================================
# 5. Filter Specific File Types
# ==========================================
def filter_files_by_extension(folder_path, extension):
    """Filter files by extension"""
    print(f"\n--- 4. Filter Files by Extension (.{extension}) ---")
    
    files, error = list_files_in_folder(folder_path)
    
    if files:
        filtered = [f for f in files if f.endswith(f'.{extension}')]
        print(f"Files with .{extension} extension in '{folder_path}':")
        if filtered:
            for file in filtered:
                print(f"  - {file}")
        else:
            print(f"  No files found with .{extension} extension")
    else:
        print(f"Error: {error}")


# # ==========================================
# # Main Function
# # ==========================================
# def main():
#     """Main entry point"""
#     print("=" * 50)
#     print("Day-10: Lists Part-2 - Sample Code")
#     print("=" * 50)
    
#     # Run example 1: Converting string to list
#     convert_string_to_list()
    
#     # Run example 2: Get user input
#     print("\n" + "=" * 50)
#     print("Running interactive example...")
#     print("=" * 50)
    
#     try:
#         user_folders = input("\nEnter folder paths separated by spaces: ").split()
        
#         if user_folders and user_folders[0]:  # Check if user entered something
#             list_files_in_multiple_folders(user_folders)
            
#             # Optional: Filter by extension
#             if user_folders:
#                 extension = input("\nEnter file extension to filter (e.g., 'py', 'txt'): ").strip()
#                 if extension:
#                     filter_files_by_extension(user_folders[0], extension)
#         else:
#             print("No folders provided. Running with sample paths...")
#             # Demo with current directory
#             demo_path = os.getcwd()
#             print(f"Listing files in: {demo_path}")
#             list_files_in_multiple_folders([demo_path])
    
#     except KeyboardInterrupt:
#         print("\n\nProgram interrupted by user.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# # ==========================================
# # Entry Point
# # ==========================================
# if __name__ == "__main__":
#     main()
