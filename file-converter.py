import markdown
import sys

def markdown_to_html(md_text):
    extensions = ['extra', 'sane_lists', 'fenced_code', 'codehilite']
    html_output = markdown.markdown(md_text, extensions=extensions)
    return html_output

def read_file(pathname):
    with open(pathname, 'r') as file:
        return file.read()

def write_file(pathname, contents):
    with open(pathname, 'w') as file:
        file.write(contents)

command = sys.argv[1]
print(sys.argv[3][-5:])
print(sys.argv[2][-3:])
if command == 'markdown' and sys.argv[2][-3:] == '.md' and sys.argv[3][-5:] == '.html':
    sample_md = read_file(sys.argv[2])
    print(sample_md)
    html_content = markdown_to_html(sample_md)
    write_file(sys.argv[3], html_content)
else:
    print(f"不明なコマンド: {command}")
    sys.exit()

