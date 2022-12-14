import numpy as np
from polynomial_model_extended import add_polynomial_features


def main():
	x = np.arange(1, 11).reshape(5, 2)
	print(f'{x=}')

	# Example 1:
	result = add_polynomial_features(x, 3)
	answer = np.array([
		[1, 2, 1, 4, 1, 8],
		[3, 4, 9, 16, 27, 64],
		[5, 6, 25, 36, 125, 216],
		[7, 8, 49, 64, 343, 512],
		[9, 10, 81, 100, 729, 1000]
	])
	print(f'Example 1: {result}\n')
	assert np.allclose(result, answer)

	# Example 2:
	result = add_polynomial_features(x, 4)
	# Output:
	answer = np.array([
		[1, 2, 1, 4, 1, 8, 1, 16],
		[3, 4, 9, 16, 27, 64, 81, 256],
		[5, 6, 25, 36, 125, 216, 625, 1296],
		[7, 8, 49, 64, 343, 512, 2401, 4096],
		[9, 10, 81, 100, 729, 1000, 6561, 10000]
	])
	print(f'Example 2: {result}')
	assert np.allclose(result, answer)


if __name__ == '__main__':
	main()
