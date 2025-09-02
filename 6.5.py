#Write triangle_area(b, h=1) with default height 1.
def triangle_area(b, h=1):
    """
    Calculate the area of a triangle.
    Formula: (base * height) / 2
    Default height is 1 if not provided.
    """
    return (b * h) / 2

# Example usage:
print(triangle_area(10, 5))  # 25.0
print(triangle_area(10))     # 5.0 (since h defaults to 1)
