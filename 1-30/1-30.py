a_list = [7, 5, -4, 6]
def check_negative(z):
  return [item * -1 for item in z if item < 0][:1]
print(check_negative(a_list))