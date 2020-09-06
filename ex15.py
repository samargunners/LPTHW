from sys import argv

script, filename = argv
prompt = '> '

txt = open(filename, encoding="utf-8")

print(f"Here's your file {filename}.")
print(txt.read())



txt.close()
