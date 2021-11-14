"""
	Problem: Kattis/Poker Hand https://open.kattis.com/problems/pokerhand
	@Auhtor: RidoineEl
"""

def main():
	ranks = [i[0] for i in input().split()]

	count_table = {}

	for i in ranks:
		if i not in count_table:
			count_table[i] = 1
		else:
			count_table[i] += 1

	print(max(count_table.values()))

if __name__ == "__main__":
	main()