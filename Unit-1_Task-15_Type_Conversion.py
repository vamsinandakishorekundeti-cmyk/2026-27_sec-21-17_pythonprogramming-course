# Example solution: type conversion (int, float, string)
str_num = input("Enter a numeric value as text: ")
int_num = int(str_num)
float_num = float(str_num)
str_num = str(int_num)

print(f"Integer value: {int_num}, type: {type(int_num)}")
print(f"Float value: {float_num}, type: {type(float_num)}")
print(f"String value: {str_num}, type: {type(str_num)}")