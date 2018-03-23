import sys

nb = 0
for line in sys.stdin:
    nb += len(line.strip().split(" "))

print("nb word received: %s" % nb)
