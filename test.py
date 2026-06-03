from backend.utils.decorators import execution_time


@execution_time
def sample_function():
    total = 0

    for i in range(1000000):
        total += i

    return total


print(sample_function())