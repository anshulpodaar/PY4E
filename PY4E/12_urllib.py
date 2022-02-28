import urllib.request, urllib.parse, urllib.error

print('\n')
counts = dict()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().rstrip())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

print('\n', counts, '\n')