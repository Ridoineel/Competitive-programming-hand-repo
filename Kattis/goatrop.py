"""
	Problem: Kattis/Goat Rope https://open.kattis.com/problems/goatrope
	@Author: RidoineEl
"""

def main():
	x, y, x1, y1, x2, y2 = map(int, input().split())
	dist = int()

	if y1 <= y <= y2: # EAST & WEST
		if x >= x2: # EAST
			dist = x - x2
		else: # WEST
			dist = x1 - x
	elif x1 <= x <= x2: # NORTH & SOUTH
		if y >= y2: # NORTH
			dist = y - y2
		else: # SOUTH
			dist = y1 - y
	elif y >= y2: 
		if x >= x2: # NORTH-EAST
			dist = ((x - x2)**2 + (y - y2)**2)**.5
		else: # NORTH-WEST
			dist = ((x - x1)**2 + (y - y2)**2)**.5
	else:
		if x >= x2: # SOUTH EAST
			dist = ((x - x2)**2 + (y - y1)**2)**.5
		else: # SOUTH-WEST
			dist = ((x - x1)**2 + (y - y1)**2)**.5

	print(f"{dist:.3f}")

if __name__ == "__main__":
	main()