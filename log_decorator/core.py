def log(descriptor: list):
    def log_decorator(inner_func):
        def wrapper(*args):
            func_name = inner_func.__name__
            command = f'{func_name}{args}'
            result = inner_func(*args)
            descriptor.append(command)
            return result

        return wrapper

    return log_decorator


descriptor_list = list()


@log(descriptor_list)
def my_max(a, b, c):
    return max(a, b, c)


@log(descriptor_list)
def my_min(x, y, z):
    return min(x, y, z)


@log(descriptor_list)
def sum(a, b):
    return a + b


if __name__ == "__main__":
    _ = my_max(1, 2, 4)
    _ = sum(10, 99)
    _ = my_min(100, 9, -1)
    print(f'{descriptor_list}')
