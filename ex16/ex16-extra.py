from sys import argv

script, filename = argv
target = open(filename, 'r')
print("Contents of file {0}:\n{1}".format(filename, target.read()))
target.close()
