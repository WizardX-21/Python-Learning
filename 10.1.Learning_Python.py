from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)
lines = contents.splitlines()

mark = ''
for line in lines:
  mark += line
print(mark)

