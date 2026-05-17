source = open("source.txt", "r")
dest = open("destination.txt", "w")

content = source.read()
dest.write(content)

words = content.split()

print("Total words copied:", len(words))

source.close()
dest.close()