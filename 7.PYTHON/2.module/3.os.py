import os

print(os.getcwd())
# print(os.mkdir("Hello"))
# print(os.rmdir("Hello"))

os.chdir("C:/src/SPC2026")
cwd = os.getcwd()

print(cwd)
print(os.listdir(cwd))

"""
C:\src\SPC2026\7.PYTHON\2.module
C:\src\SPC2026
['.git', '.vscode', '1.HTML', '10.VIBE', '2.CSS', '3.BOOTSTRAP', '4.TAILWIND', '5.DESIGN', '6.JS', '7.PYTHON', 'README.md']
"""