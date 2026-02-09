import sample as sp
import os

# ==========================================
# Main Function
# ==========================================
def main():
    """Main entry point"""
    print("=" * 50)
    print("Day-10: Lists Part-2 - Sample Code")
    print("=" * 50)
    
    # Run example 1: Converting string to list
    sp.convert_string_to_list()
    
    # Run example 2: Get user input
    print("\n" + "=" * 50)
    print("Running interactive example...")
    print("=" * 50)
    
    try:
        user_folders = input("\nEnter folder paths separated by spaces: ").split()
        
        if user_folders and user_folders[0]:  # Check if user entered something
            sp.list_files_in_multiple_folders(user_folders)
            
            # Optional: Filter by extension
            if user_folders:
                extension = input("\nEnter file extension to filter (e.g., 'py', 'txt'): ").strip()
                if extension:
                    sp.filter_files_by_extension(user_folders[0], extension)
        else:
            print("No folders provided. Running with sample paths...")
            # Demo with current directory
            demo_path = os.getcwd()
            print(f"Listing files in: {demo_path}")
            sp.list_files_in_multiple_folders([demo_path])
    
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


# ==========================================
# Entry Point
# ==========================================
if __name__ == "__main__":
    main()
