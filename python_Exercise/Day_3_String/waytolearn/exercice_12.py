def copy_end(string):
    """Create a string with the 2 last elements repeated 4 times  """
    return string[-2:]*4 if len(string) >= 2 else ""


print(copy_end("hello"))
print(copy_end("h"))