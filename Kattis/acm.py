"""
	Problem: Kattis/ACM Contest Scoring https://open.kattis.com/problems/acm
	@Author: RidoineEl
"""

import sys

def main():

	score = {}
	
	for line in sys.stdin:
		line = line.strip()

		if line == "-1":
			break

		t, name, status = line.split()
		t = int(t)

		#datas.append((t, name, status))

		if name not in score:
			score[name] = [t, 0, False]
		else:
			score[name][0] = max(t, score[name][0])

		if status == "right":
			score[name][2] = True
		else:
			score[name][1] += 20

	prob = [t + penality for name, (t, penality, j) in score.items() if j]

	print(len(prob), sum(prob))	



if __name__ == "__main__":
	main()