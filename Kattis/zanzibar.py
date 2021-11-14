"""
	Problem: kattis/Stand On Zanzibar https://open.kattis.com/problems/zanzibar
	@Author: RidoineEl
"""

def main():
	N = int(input())

	for _ in range(N):

		ls = [int(i) for i in input().split()]

		res = 0
		for i in range(len(ls) - 1):
			val = ls[i + 1] - 2*ls[i]

			if val > 0:
				res += val

		print(res)
if __name__ == "__main__":
	main()