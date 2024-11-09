def next_not_3(x: int, y: int) -> int:
    a = x * y
    if a % 3 != 0:
        return a
    else:
        a % 3 == 0
        a += 1
        return a

# print(next_not_3(9, 2))



def correct_jumbled_text(text, words):
    """Corrects jumbled words in a text given a list of correct words.

    Args:
        text: A string containing jumbled words.
        words: A list of correct words in any order.

    Returns:
        A string with corrected words.
    """

    words_set = set(words)  # Create a set for faster lookup
    words_dict = {}  # Create a dictionary to store words with first and last letters

    for word in words:
        words_dict[word[0] + word[-1]] = word
    corrected_text = []
    for word in text.split():
        if word[0] + word[-1] in words_dict:
            corrected_text.append(words_dict[word[0] + word[-1]])
        else:
            corrected_text.append(word)  # If word not found, keep original

    return " ".join(corrected_text)


# hi =correct_jumbled_text("Somoene watns to colelct corcert wodrs", ["correct", "someone", "words", "to", "collect", "wants"])
# print(hi)


def correct_jumbled_text_alphabets(text, words):
    """Corrects jumbled words in a text given a list of correct words.

    Args:
        text: A string containing jumbled words.
        words: A list of correct words in any order.

    Returns:
        A string with corrected words.
    """

    words_set = set(words)
    corrected_text = []

    for word in text.split():
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                candidate_word = word[:i] + word[j:]
                if candidate_word in words_set:
                    corrected_text.append(candidate_word)
                    break
            else:
                corrected_text.append(word)  # If no match, keep original

    return " ".join(corrected_text)

# hi =correct_jumbled_text("Somoene watns to colelct wrogn wodrs", ["wrong", "someone", "words", "to", "collect", "wants"])
# print(hi)



def latest_time(time_str):
    """
    Finds the latest possible time from a given 24-hour format time string with '?' characters.

    Args:
        time_str: A string representing a 24-hour format time with '?' characters.

    Returns:
        A string representing the latest possible time.
    """

    hours, minutes = time_str.split(":")

    def replace_question_marks(time_part):
        if time_part[0] == "?":
            if time_part == "??":
                return "23"

            elif int(time_part[1]) <= 3:
                return f"2{time_part[1]}"

            elif 3 < int(time_part[1]):
                return f"1{time_part[1]}"

        else:
            return time_part

    hours = replace_question_marks(hours)

    def replace(minute_part):
        if minute_part[0] == "?":
            if minute_part == "??":
                return "59"
            else:
                return f"5{minute_part[1]}"
        
        else:
            return minute_part
    minutes = replace(minutes)
    
    return f"{hours}:{minutes}"


time_str = "23:??"
# print(latest_time(time_str))  
time_str = "?6:??"
# print(latest_time(time_str)) 






def compress(word: str) -> str:
    if not word:
        return ""

    compressed_string = ""
    count = 1

    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            count += 1
        else:
            if count > 1:
                compressed_string += str(count) + word[i - 1]
            count = 1


    compressed_string += str(count) + word[-1]
    return compressed_string


compres = "abbcccdddd"
# print(compress(compres))
compres = "ddffffee"
# print(compress(compres))





def get_longest_word( s: str) -> str:
    splitted = s.split(" ")
    longest_word = ""
    for i in splitted:
        if len(i) > len(longest_word):
            longest_word = i

    return longest_word


longest = get_longest_word('Python is simple and effective!')
# print(longest)




def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if left < right and s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# print(is_palindrome('racecar'))  
# print(is_palindrome('nottona'))  
# print(is_palindrome("A man, a plan, a canal: Panama"))  






def swap_quotes(string):

    new_string = ""
    for char in string:
        if char == "'":
            new_string += '"'
        elif char == '"':
            new_string += "'"
        else:
            new_string += char
    return new_string


input_string = "This is a 'string' with \"double\" quotes."
output_string = swap_quotes(input_string)
print(output_string)  































