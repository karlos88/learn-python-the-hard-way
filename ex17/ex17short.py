from sys import argv

srcipt, from_file, to_file = argv
open(to_file, 'w').write(open(from_file).read())
