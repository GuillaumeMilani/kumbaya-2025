import re

def regex_search_and_replace(input_file_path, output_file_path):
    # Read the contents of the file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Perform the regex search and replace operations

    # Remove unbreakable spaces
    content = re.sub(r'~', r'', content)

    # Dieses
    content = re.sub(r'\\#', r'#', content)
    content = re.sub(r'\\\*', r'*', content)
    content = re.sub(r'\\\!', r'!', content)
    content = re.sub(r'\’', r"'", content)
    content = re.sub(r' +\n', r'\n', content)
    
    # TODO
    # content = re.sub(r'«', r'\\guillemotleft', content)
    # content = re.sub(r'»', r'\\guillemotright', content)
    content = re.sub(r'«', r'"', content)
    content = re.sub(r'»', r'"', content)

    # Chords
    content = re.sub(r'\\\[([\w#-]+)\\\]', r'\\[\1]', content)

    # Replace ^# (.+) with \beginsong{$1}
    content = re.sub(r'^# (.+)', r'\\beginsong{\1}', content, flags=re.MULTILINE)

    # Replace \n\n## (.+) with [{Calogero (2017)}]
    content = re.sub(r'\n\n## (.+)', r'[by={\1}]', content)

     # Replace Refrain\n\w with \n\n\beginchorus\n$1
    content = re.sub(r'Refrain[ \t]*\n(\S)', r'\n\\beginchorus\n\1', content, flags=re.MULTILINE)

    # Add \endchorus after the next \n\n when \beginchorus is found
    content = re.sub(r'\\beginchorus\n(.+?)\n\n', r'\\beginchorus\n\1\n\\endchorus\n\n', content, flags=re.DOTALL)

    # Replace \n\n(\w) with \n\n\beginverse\n$1
    content = re.sub(r'\n\n(\w)', r'\n\n\\beginverse\n\1', content)

    # Add \endverse after the next \n\n when \beginverse is found
    content = re.sub(r'\\beginverse\n(.+?)\n\n', r'\\beginverse\n\1\n\\endverse\n\n', content, flags=re.DOTALL)

    # Add \endsong before the next \beginsong after the last \endverse
    content = re.sub(r'\n\\beginsong', r'\n\\endsong\n\\beginsong', content, flags=re.DOTALL)

    # Cleanup
    # Remove extra spaces before newlines
    content = re.sub(r'  \n', r'\n', content)

    # Finish with \endsong
    content = content.rstrip() + '\n\\endverse\n\n\\endsong\n'
    
    # Shift chords \[] from one letter to the left, add a space if already beginning of the line
    content = re.sub(r'(\W)(\\\[\w+\])', r'\1\2 ', content)
    content = re.sub(r'(\w)(\\\[\w+\])', r'\2\1', content)


    # Write the modified content back to the file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print("Search and replace operations completed successfully.")

input_file_path = 'Paroles.md'
output_file_path = 'paroles.tex'
regex_search_and_replace(input_file_path, output_file_path)