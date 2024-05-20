def reverse_string(input: str) -> str:
    if len(input) >= 3:
        result = ""
        for i in range(len(input)-1, -1, -1):
            result += input[i]

        return result
        # return input[::-1]

    return input


if __name__ == '__main__':
    input = input("Masukan string: ")
    result = reverse_string(input)
    print(result)