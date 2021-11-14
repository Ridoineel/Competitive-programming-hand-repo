"""
	Problem: Kattis/Cetiri https://open.kattis.com/problems/cetiri
	@Auhtor: RidoineEl
"""

def main():
	seq = [int(i) for i in input().split()]
	seq.sort()

	diff1 = seq[1] - seq[0]
	diff2 = seq[2] - seq[1]

	if diff1 == diff2:
		print(seq[-1] + diff1)
	else:
		print(seq[0] + diff2)


if __name__ == "__main__":
	main()