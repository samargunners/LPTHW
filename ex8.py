formatter = "{} {} {} {} {}"

print(formatter.format(1 ,2, 3, 4, 5))
print(formatter.format("one", "two", "three", "four", "five"))
print(formatter.format(True, False, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter, formatter))
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear",
	"how you doing?"
))