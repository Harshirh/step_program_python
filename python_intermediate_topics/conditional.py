# person_name = str(input("Enter the person's name: "))
# age = int(input("Enter the person's age: "))

# if age < 18:
#     print(f'{person_name} is a minor.')
# elif age >= 18 and age < 65:
#     print(f'{person_name} is an adult.')
# else:
#     print(f'{person_name} is a senior citizen.')


def sliding_window(nums, k):
    if len(nums) < k:
        print("The values are not valid")
    else:
        sum_window = sum(nums[:k])
        print(sum_window)

        for i in range(k, len(nums)):
            sum_window += nums[i] - nums[i - k]
            print(sum_window)
            