"""
	Problem: Kattis/Scaling Recipes https://open.kattis.com/problems/recipes
	@Auhtor: RidoineEl
"""

def main():
	N = int(input())

	for k in range(N):

		ing_nb, t, r = map(int, input().split())

		datas = []
		principale = ["", 0, 0]

		for i in range(ing_nb):
			name, weight, percentage = input().split()
			weight = float(weight)
			percentage = float(percentage) / 100

			if percentage == 1:
				principale = [name, weight, percentage]

			datas.append((name, weight, percentage))

		scale_value = principale[1] * r/t


		print("Recipe #", k + 1)

		for name, weight, p in datas:
			print(f"{name} {scale_value * p:.1f}")

		print("-" * 40)



if __name__ == "__main__":
	main()