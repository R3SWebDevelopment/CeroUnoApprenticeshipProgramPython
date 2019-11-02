def make_bricks(small, big, goal):
    small_size, big_size = (1, 5)

    big_bricks_needed = int(goal / big_size)
    small_bricks_needed = goal % big_size

    if small >= small_bricks_needed and big >= big_bricks_needed:
        return True

    if big < big_bricks_needed:
        big_bricks_needed -= big
        small_bricks_needed += big_bricks_needed * big_size

        if small >= small_bricks_needed and big >= big_bricks_needed:
            return True

    return small >= small_bricks_needed
