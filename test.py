def add(nums: list, *args):

    """
    This is a simple function that adds numbers together.

    """

    total = 0.

    if nums:
        total += sum(nums)

    for arg in args:

        total += arg

    return total


if __name__ == "__main__":

    nums = input("Enter numbers to add: ").split(",")
    nums = [float(x) for x in nums]

    a = float(input("Enter another number: "))
    b = float(input("Enter another number again: "))

    total = add(nums, a, b)

    print(f"Final sum: {total}")
