def convert_cel_to_far(deg_cel):
    f_cal = deg_cel * 1.8 + 32
    return f_cal

def convert_far_to_cel(far):
    deg_cal = (far - 32) * (5/9)
    return deg_cal

a = float(input("Enter a temperature in degrees F:"))
print(f'{a} degrees F = {convert_far_to_cel(a):.2f} degrees C')

b = float(input("Enter a temperature in degrees C:"))
print(f'{b} degrees C = {convert_cel_to_far(b):.2f} degrees F')