# Program to read and print the contents of a text file

def print_file_contents(file_path):
    """
    Reads and prints the contents of a text file.
    Handles errors like file not found or permission denied.
    """
    try:
        # Open the file in read mode with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            if content.strip() == "":
                print("The file is empty.")
            else:
                print("----- File Contents -----")
                print(content)
                print("-------------------------")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{file_path}'.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode '{file_path}'. Check file encoding.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Ask user for file path
    file_path = input("Enter the path to the text file: ").strip()
    print_file_contents(file_path)
