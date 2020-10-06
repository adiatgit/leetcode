def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    digit_dict = {
                0:[" "],
                1:[" "], 2: ["a","b","c"], 3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],
                6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]
                 }
    # digit_dict = [[]i for i in digit_dict]
    list_of_letters = []
    letters = ""
    # for i in digit_dict[int(digits[0])]:
    #     list_of_letters.append(i)
    print list_of_letters
    for i in range(1,len(digits)):
        print digit_dict[int(digits[i])]
        for j in digit_dict[int(digits[i])]:
            list_of_letters[] = list_of_letters[]+j
            # for k in range(len(list_of_letters)):
            print list_of_letters
    return list_of_letters
print letterCombinations("23")
