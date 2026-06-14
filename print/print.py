#print append a new line by default
print("blah blah blah")
#we can disable it by redefining end parameter
print("blah blah blah", end=" ")
print("still on the same line")
#we can print multiple arguments with one print
print("blah blah blah", 6, "more stuff")
#arguments are separated with " " by default,
#we can change it by redefining sep
print("blah blah blah", 6, "more stuff", sep="\n")
#by default print prints to stdout,
#we can send it somewhere else by redefining file
import sys
print("printing to stderr", file=sys.stderr)
#by default prints are buffered,
#we can flush them immediately by redefining flush
print("blah blah blah", flush=True)
