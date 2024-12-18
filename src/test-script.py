import numpy as np


def main():
    """
    Random example: matrix-multiply two random 3x3 NumPy arrays
    """
    ex_arr1 = np.random.randint(100, size=(3,3))
    ex_arr2 = np.random.randint(100, size=(3,3))
    print("Array 1:")
    print(ex_arr1)
    print("Array 2:")
    print(ex_arr2)
    result_arr = np.matmul(ex_arr1, ex_arr2)
    print("Result:")
    print(result_arr)
    return result_arr


if __name__=="__main__":
    _ = main()
