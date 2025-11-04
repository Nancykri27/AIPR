def count_lines_in_file(file_path: str) -> int:
    if not file_path.lower().endswith('.txt'):
        raise ValueError("File must be a .txt file")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for _ in file)
        return line_count
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")

# Example usage:
if __name__ == "__main__":
    try:
        # Replace with your file path
        file_path = "Word.txt"
        lines = count_lines_in_file(file_path)
        print(f"Number of lines in the file: {lines}")
    except Exception as e:
        print(f"Error: {str(e)}")