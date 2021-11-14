"""
	Problem: Kattis/Drunk Vigenère https://open.kattis.com/problems/drunkvigenere
	@Auhtor: RidoineEl
"""

from string import ascii_uppercase as letters

def main():
	msg_crypt = input()
	key = input()

	msg = ""

	for i in range(len(key)):
		if i % 2 == 1:
			msg += letters[(letters.index(msg_crypt[i]) + letters.index(key[i])) % 26]
		else:
			msg += letters[(letters.index(msg_crypt[i]) - letters.index(key[i])) % 26]

	print(msg)

if __name__ == "__main__":
	main()