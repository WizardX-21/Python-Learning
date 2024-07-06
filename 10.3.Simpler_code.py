from pathlib import Path

path = Path('10.Files and Exceptions/pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
  pi_string += line.strip()

print(f"{pi_string[:5]}")
print(len(pi_string))  


