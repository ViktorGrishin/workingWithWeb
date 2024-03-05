import os

print(os.name)

print(os.getcwd())

# os.chdir('C:\\Program Files')
# print(os.getcwd())


os.chdir('..')
print(os.getcwd())

print(os.listdir())

for currentdir, dirs, files in os.walk(r'C:\Users\IT-1\Desktop\GriViktor\human'):
    print(currentdir, dirs, files)

print(os.access('Меня нет', os.F_OK))