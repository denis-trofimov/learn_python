def triple_step(n):
    """ Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
    steps at a time. Implement a method to count how many possible ways the child can run up the
    stairs.
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 1 + 2 * 2 + 1
    else:
        ways = triple_step(n - 1) * n + triple_step(n - 2) * (n - 1) 

if __name__ == '__main__':
    stair = int(input("Staircase steps: "))
    triple_step(stair)