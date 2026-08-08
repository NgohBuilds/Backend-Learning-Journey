
def is_num_option_valid(input):

    try:
        input = int(input)
    except ValueError as e:
        print(f"\n {e}")

    if input  not in range(0, 7, 1):
        return None
    return input
