import math

def get_circle(radius=1):
    return radius * radius * math.pi

if __name__ == "__main__":
    print(get_circle(10), 'cm^2')
    print(get_circle(7), 'cm^2')
