import time

current_time = time.time()

print(current_time)


def decorator_function(func):
	def wrapper(*args, **kwargs):

		start_time = time.time()

		result = func(*args, **kwargs)

		stop_time = time.time()

		name = func.__name__

		speed = stop_time - start_time

		print(f"{name} run speed : {speed}s")

		return result

	return wrapper 


def fast_function():
	for i in range(1,10, 2):
		i * i

def slow_function():
	for i in range(0,10):
		i * i

fast_calc = decorator_function(fast_function)
fast_calc()
slow_calc = decorator_function(slow_function)
slow_calc()
