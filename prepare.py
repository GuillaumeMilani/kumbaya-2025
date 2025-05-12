import re

def regex_search_and_replace(input_file_path, output_file_path):
    # Read the contents of the file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Perform the regex search and replace operations
    # Replace ^# (.+) with \beginsong{$1}
    content = re.sub(r'^# (.+)', r'\\beginsong{\1}', content, flags=re.MULTILINE)

    # Replace \n\n## (.+) with [{Calogero (2017)}]
    content = re.sub(r'\n\n## (.+)', r'[by={\1}]', content)

    # Replace \n\n(\w) with \n\n\beginverse\n$1
    content = re.sub(r'\n\n(\w)', r'\n\n\\beginverse\n\1', content)

    # Add \endverse after the next \n\n when \beginverse is found
    content = re.sub(r'\\beginverse\n(.+?)\n\n', r'\\beginverse\n\1\n\\endverse\n\n', content, flags=re.DOTALL)

    # Add \endsong before the next \beginsong after the last \endverse
    content = re.sub(r'\\endverse\n\n\\beginsong{(.+?)}\n', r'\\endverse\n\\endsong\n\\beginsong{\1}\n', content, flags=re.DOTALL)

    # Replace \(\w+\) with \\[\1] only if \w+ is not only numbers
    content = re.sub(r'(?<!\{)\((\w+)\)(?!\})', r'\\[\1]', content)

    # Cleanup
    # Remove extra spaces before newlines
    content = re.sub(r'  \n', r'\n', content)

    # Write the modified content back to the file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print("Search and replace operations completed successfully.")

input_file_path = 'Paroles.md'
output_file_path = 'paroles.tex'
regex_search_and_replace(input_file_path, output_file_path)