from __future__ import annotations


alphabet = list("abcdefghijklmnopqrstuvwxyz")

def shift(text: str, amount: int, dir: str = "left") -> str:
	s = ""
	for c in text:
		if c in alphabet:
			offset = amount * (-1 if dir == "left" else 1)
			s += alphabet[(alphabet.index(c) + offset) % 26]
		else:
			s += c
	return s

def main():
	base_str = input("Enter text to shift: ")
	dir = input("Direction (left/right): ")
	for i in range(1, 26):
		print("Shifted %2i: %s" % (i, shift(base_str, i, dir)))



main()