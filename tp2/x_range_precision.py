def amplify(a_list, between_points):
    result = []
    for i in range(0, len(a_list) - 1):
        result.append(a_list[i])
        min = a_list[i]
        max = a_list[i + 1]
        delta = (max - min) / (between_points + 1)
        for j in range(1, between_points + 1):
            result.append(min + (delta * j))
    result.append(a_list[len(a_list) - 1])
    return result

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    print(a)
    a = amplify(a, 2)
    print(a)