num1 = input().strip()
num2 = input().strip()
len_max = max(len(num1), len(num2))
num1 = num1.zfill(len_max)
num2 = num2.zfill(len_max)
carry_count = 0
carry = 0
for i in range(len_max - 1, -1, -1):
    digit_sum = int(num1[i]) + int(num2[i]) + carry
    carry = digit_sum // 10
    if carry > 0:
        carry_count += 1
print(carry_count)
