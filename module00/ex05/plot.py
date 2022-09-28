import numpy as np
from matplotlib import pyplot as plt


def accepts(*types):
	def check_accepts(f):
		assert len(types) == f.__code__.co_argcount

		def new_f(*args, **kwargs):
			if not args or any(not isinstance(arg, t) for arg, t in zip(args, types)):
				return None
			return f(*args, **kwargs)
		# new_f.__name__ = f.__name__
		return new_f
	return check_accepts


@accepts(np.ndarray, np.ndarray)
def predict_(x: np.ndarray, theta: np.ndarray) -> np.ndarray | None:
	"""Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
	Args:
	x: has to be a numpy.ndarray, a vector of dimension m * 1.
	theta: has to be a numpy.ndarray, a vector of dimension 2 * 1.
	Returns:
	y_hat as a numpy.ndarray, a vector of dimension m * 1.
	None if x and/or theta are not numpy.array.
	None if x or theta are empty numpy.array.
	None if x or theta dimensions are not appropriate.
	Raises:
	This function should not raise any Exception.
	"""
	return (theta[0] + x * theta[1]).reshape(x.shape[0], -1)


def plot(x: np.ndarray, y: np.ndarray, theta: np.ndarray) -> None:
	"""Plot the data and prediction line from three non-empty numpy.arrays.
	Args:
	x: has to be a numpy.array, a vector of dimension m * 1.
	y: has to be a numpy.array, a vector of dimension m * 1.
	theta: has to be an numpy.array, a vector of dimension 2 * 1.
	Returns:
	Nothing.
	Raises:
	This function should not raise any Exceptions.
	"""
	if any(not isinstance(arg, np.ndarray) or arg.size == 0 for arg in (x, y, theta)):
		return None
	plt.plot(x, y, 'bo')
	plt.plot(x, predict_(x, theta), color='orange')
	plt.show()
