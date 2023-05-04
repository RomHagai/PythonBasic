# import this
import datetime
import calendar
import string


# ex 2.3.3
def three_pigs():
    number_stones = int(input("Please Enter three digits (each digit for one pig):"))
    first_pig = number_stones % 10
    second_pig = number_stones % 100 // 10
    third_pig = number_stones // 100
    sum_stones = first_pig + second_pig + third_pig
    print(sum_stones)
    print(sum_stones // 3)
    print(sum_stones - (sum_stones // 3) * 3)
    print(sum_stones % 3 == 0)


# ex 3.2.1
def taki():
    print('"Shuffle, Shuffle, Shuffle", say it together! \n Change colors and directions, Don\'t back down and stop '
          'the player! \n \tDo you want to play Taki? \n \tPress y\\n')


# ex 3.3.3
def secret():
    encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
    print(encrypted_message[::-2])


# ex 3.4.2
def change():
    my_str = input("Please enter a string: ")
    letter_to_change = 'e'
    print(my_str[0] + my_str[1::].replace(my_str[0], letter_to_change))


# ex 3.4.3
def half_half():
    my_str = input("Please enter a string: ")
    first_part = my_str[:len(my_str) // 2]
    second_part = my_str[len(my_str) // 2:]
    print(first_part.lower() + second_part.upper())


# ex 4.2.2
def palindrome():
    input_str = input("Enter a word: ")
    input_str = input_str.replace(" ", "").lower()
    if input_str == input_str[::-1]:
        print("OK")
    else:
        print("NOT")


# ex 4.2.3
def convert():
    temp = input("Insert the temperature you would like to convert: ")
    if temp[-1].lower() == 'c':
        temp_c = float(temp[:-1])
        temp_f = (temp_c * 9 / 5) + 32
        print(str(temp_f) + "F")
    elif temp[-1].lower() == 'f':
        temp_f = float(temp[:-1])
        temp_c = (temp_f - 32) * 5 / 9
        print(str(temp_c) + "C")
    else:
        print("Invalid input")


# ex 4.2.4
def day_of_week():
    date_str = input("Enter a date (dd/mm/yyyy): ")
    date_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y')
    day = calendar.day_name[date_obj.weekday()]
    print(day)


# ex 5.3.4
def last_early(my_str):
    my_str = my_str.lower()
    last_char = my_str[-1]
    if last_char in my_str[:-1]:
        return True
    else:
        return False


# ex 5.3.5
def distance(num1, num2, num3):
    if abs(num2 - num1) <= 1 and abs(num3 - num1) >= 2 and abs(num2 - num3) >= 2:
        return True
    elif abs(num2 - num3) <= 1 and abs(num1 - num2) >= 2 and abs(num1 - num3) >= 2:
        return True
    elif abs(num3 - num1) <= 1 and abs(num2 - num1) >= 2 and abs(num2 - num3) >= 2:
        return True
    else:
        return False


# ex 5.3.6
def fix_age(age):
    if 13 <= age <= 19 and age != 15 and age != 16:
        return 0
    else:
        return age


def filter_teens(a=13, b=13, c=13):
    return fix_age(a) + fix_age(b) + fix_age(c)


# ex 5.3.7
def chocolate_maker(small, big, x):
    max_big_cubes = x // 5
    big_cubes_needed = min(max_big_cubes, big)
    small_cubes_needed = x - big_cubes_needed * 5
    return small_cubes_needed <= small


# ex 5.4.1
def fun(num1, num2):
    """
        This function takes two numbers, num1 and num2, and returns their sum.
        Parameters:
        num1 (int or float): the first number
        num2 (int or float): the second number
        Returns:
        int or float: the sum of num1 and num2
        """
    return num1 + num2


# ex 6.1.2
def shift_left(my_list):
    """
    :param my_list:
    :return: shift left list
    """
    return my_list[1:] + [my_list[0]]


# ex 6.2.3
def format_list(my_list):
    """
    :param my_list:
    :return: with ,
    """
    return ", ".join(my_list[::2][:-1]) + ", and " + my_list[-1]


# ex 6.2.4
def extend_list_x(list_x, list_y):
    """
    Concatenate two lists where list_y is added to the beginning of list_x
    :param list_x:
    :param list_y: list to be added to the beginning of list_x
    :return: the extended list_x
    """
    for item in list_x:
        list_y.append(item)
    return list_y


# ex 6.3.1
def are_lists_equal(list1, list2):
    """
    :param list1:
    :param list2:
    :return: if the list has same elements
    """
    return set(list1) == set(list2) and len(list1) == len(list2)


# ex 6.3.2
def longest(my_list):
    """
    :param my_list:
    :return: the longest word
    """
    return max(my_list, key=len)


# ex 7.1.4
def squared_numbers(start, stop):
    """
    :param start:
    :param stop:
    :return: squared
    """
    new_list = []
    i = start
    j = stop
    while i <= j:
        new_list.append(i * i)
        i = i + 1
    return new_list


# ex 7.2.1
def is_greater(my_list, n):
    """
    :param my_list:
    :param n:
    :return: only the long
    """
    new_list = []
    for item in my_list:
        if int(item) > n:
            new_list.append(item)
    return new_list


# ex 7.2.2
def numbers_letters_count(my_str):
    """
   :param my_str:
   :return: list
   """
    num_digits = sum(1 for c in my_str if c.isdigit())
    num_letters = sum(1 for c in my_str if c.isalpha() or c.isspace() or c in string.punctuation)
    return [num_digits, num_letters]


# ex 7.2.4
def seven_boom(end_number):
    """
    :param end_number:
    :return: seven BOOM list
    """
    new_list = []
    for i in range(0, end_number + 1):
        if i % 7 == 0 or '7' in str(i):
            new_list.append("BOOM")
        else:
            new_list.append(i)
    return new_list


# ex 7.2.5
def sequence_del(my_str):
    """
    :param my_str:
    :return: DISTINCT
    """
    new_str = ""
    for char in my_str:
        if not char in new_str:
            new_str = new_str + char
    return new_str


# ex 7.2.6
def print_products(products):
    print("Product list:")
    print(", ".join(products))


def print_num_products(products):
    print("Number of products:", len(products))


def is_product_in_list(products, product_name):
    if product_name in products:
        print("Yes, {} is on the list".format(product_name))
    else:
        print("No, {} is not on the list".format(product_name))


def print_product_count(products, product_name):
    count = products.count(product_name)
    print("The product {} appears {} times in the list".format(product_name, count))


def remove_product(products, product_name):
    if product_name in products:
        products.remove(product_name)
        print("{} was removed from the list".format(product_name))
    else:
        print("Product not found in list")


def add_product(products, product_name):
    products.append(product_name)
    print("{} was added to the list".format(product_name))


def print_invalid_products(products):
    invalid_products = [p for p in products if len(p) < 3 or not p.isalpha()]
    if invalid_products:
        print("Invalid products:", ", ".join(invalid_products))
    else:
        print("No invalid products found")


def remove_duplicates(products):
    unique_products = list(set(products))
    print("List with duplicates removed:")
    print_products(unique_products)


def menu():
    products_str = input("Enter list of products, separated by commas: ")
    products = products_str.split(",")

    while True:
        print("\nMenu:")
        print("1. Print product list")
        print("2. Print number of products")
        print("3. Is product on list?")
        print("4. How many times does a product appear?")
        print("5. Remove product from list")
        print("6. Add product to list")
        print("7. Print invalid products")
        print("8. Remove duplicates from list")
        print("9. Exit program")

        choice = input("Enter choice (1-9): ")

        if choice == "1":
            print_products(products)
        elif choice == "2":
            print_num_products(products)
        elif choice == "3":
            product_name = input("Enter product name: ")
            is_product_in_list(products, product_name)
        elif choice == "4":
            product_name = input("Enter product name: ")
            print_product_count(products, product_name)
        elif choice == "5":
            product_name = input("Enter product name to remove: ")
            remove_product(products, product_name)
        elif choice == "6":
            product_name = input("Enter product name to add: ")
            add_product(products, product_name)
        elif choice == "7":
            print_invalid_products(products)
        elif choice == "8":
            remove_duplicates(products)
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


# ex 7.2.7
def arrow(my_char, max_length):
    """
    :param my_char:
    :param max_length:
    :return: shape
    """
    new_str = ""
    for i in range(max_length):
        new_str = new_str + (i + 1) * my_char + "\n"
    for j in range(max_length - 1, 0, -1):
        new_str = new_str + j * my_char + "\n"
    return new_str


# ex 8.2.1
def format_change():
    data = ("self", "py", 1.543)
    format_string = "Hello {}.{} learner, you have only {:.1f} units left before you master the course!"
    print(format_string.format(data[0], data[1], data[2]))


# ex 8.2.2
def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: float(x[1]), reverse=True)


# ex 8.2.3
def mult_tuple(tuple1, tuple2):
    result = ()
    for i in tuple1:
        for j in tuple2:
            result += ((i, j), (j, i))
    return result


# ex 8.2.4
def sort_anagrams(list_of_strings):
    anagrams = {}
    for word in list_of_strings:
        key = ''.join(sorted(word))
        print(key)
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    return list(anagrams.values())


# ex 8.3.2
def menu2():
    mariah = {"first_name": "Mariah",
              "last_name": "Carey",
              "birth_date": "27.03.1970",
              "hobbies": ["Sing", "Compose", "Act"]}

    choice = int(input("Enter a number between 1 and 7: "))

    if choice == 1:
        print(mariah["last_name"])

    elif choice == 2:
        birth_date = mariah["birth_date"]
        month = birth_date[3:5]
        print(month)

    elif choice == 3:
        num_hobbies = len(mariah["hobbies"])
        print(num_hobbies)

    elif choice == 4:
        last_hobby = mariah["hobbies"][-1]
        print(last_hobby)

    elif choice == 5:
        mariah["hobbies"].append("Cooking")
        print(mariah["hobbies"])

    elif choice == 6:
        birth_date = mariah["birth_date"]
        day = int(birth_date[:2])
        month = int(birth_date[3:5])
        year = int(birth_date[6:])
        birth_tuple = (day, month, year)
        print(birth_tuple)

    elif choice == 7:
        birth_date = mariah["birth_date"]
        birth_year = int(birth_date[6:])
        current_year = 2023
        age = current_year - birth_year
        mariah["age"] = age
        print(mariah["age"])


# ex 8.3.3
def count_chars(my_str):
    my_dict = {}
    for char in my_str:
        if char != ' ':
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
    return my_dict


# ex 8.3.4
def inverse_dict(my_dict):
    new_dict = {}
    for key, value in my_dict.items():
        if value not in new_dict:
            new_dict[value] = [key]
        else:
            new_dict[value].append(key)
    for key in new_dict:
        new_dict[key] = sorted(new_dict[key])
    return new_dict


# ex 9.1.1
def are_files_equal(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read() == f2.read()


# ex 9.1.2
def sort_words(file_path):
    with open(file_path) as f:
        words = set()
        for line in f:
            words.update(line.strip().split())
        return sorted(words)


def reverse_lines(file_path):
    with open(file_path) as f:
        for line in f:
            print(line.strip()[::-1])


def last_lines(file_path, n):
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines[-n:]:
            print(line.strip())


def main_program():
    file_path = input("Enter a file path: ")
    task = input("Enter a task (sort, rev, last): ")

    if task == "sort":
        sorted_words = sort_words(file_path)
        print(sorted_words)

    elif task == "rev":
        reverse_lines(file_path)

    elif task == "last":
        n = int(input("Enter number of last lines: "))
        last_lines(file_path, n)

    else:
        print("Invalid task entered.")

# ex 9.2.2
def copy_file_content(source, destination):
    with open(source, 'r') as file1:
        with open(destination, 'w') as file2:
            file2.write(file1.read())

# ex 9.2.3
def who_is_missing(file_name):
    with open(file_name, 'r') as file:
        numbers = file.read().split(',')
        numbers = [int(num) for num in numbers]
        missing = None
        for i in range(1, len(numbers)+1):
            if i not in numbers:
                missing = i
                break
        with open('found.txt', 'w') as found_file:
            found_file.write(str(missing))
        return missing

# ex 9.3.1
def my_mp3_playlist(file_path):
    longest_song_length = -1
    longest_song_name = ""
    songs_count = 0
    operations = {}

    with open(file_path, "r") as file:
        for line in file:
            song_info = line.strip().split("; ")
            if len(song_info) != 3:
                continue

            song_name, performer_name, song_length = song_info
            songs_count += 1

            if longest_song_length < 0 or song_length > longest_song_length:
                longest_song_length = song_length
                longest_song_name = song_name

            operation_name = performer_name if performer_name != "Unknown" else song_name
            if operation_name in operations:
                operations[operation_name] += 1
            else:
                operations[operation_name] = 1

    most_common_operation = max(operations, key=operations.get)

    return longest_song_name, songs_count, most_common_operation

# ex 9.3.2
def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    while len(lines) < 3:
        lines.append('\n')
    lines[2] = f"{new_song};Unknown;\n"
    with open(file_path, 'w') as f:
        f.writelines(lines)
    with open(file_path, 'r') as f:
        print(f.read())

def main():

    # ex 2.3.3
    three_pigs()

if __name__ == '__main__':
    main()