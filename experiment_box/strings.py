def unpack_words(string: str):
  lexicon: list[str] = []
  container: str = ""

  i = 0
  
  while i < len(string):
    if string[i] == " " or not ((string[i] >= 'A' and string[i] <= "Z") or (string[i] >= 'a' and string[i] <= "z")):
      i += 1
      if len(container) > 0:
        lexicon.append(container)
      container = ""
      continue
    container += string[i]
    i += 1
  
  if container:
    lexicon.append(container)
  
  return lexicon
    
quote = "Remember Red, HOPE is a Good thing and no good thing ever dies."
# print(unpack_words(quote))


def find_duplicates(lexicon: list) -> set:
    # for index in range(len(lexicon)):
    #   lexicon[index] = lexicon[index].lower()

    duplicates: set = set()
    
    if len(lexicon) >= 2:
      for n in range(len(lexicon)):
        for index in range(len(lexicon)):  # n+1
          if n != index and lexicon[n].lower() == lexicon[index].lower():
            duplicates.add(lexicon[n].lower())
  
    return duplicates


# print(find_duplicates(unpack_words(quote)))


def count_vowels(string: str) -> int:
  vowels = "aeiouAEIOU"
  count = 0

  for index in range(len(string)):
    for n in range(len(vowels)):
      if string[index] == vowels[n]:
        count += 1
    
  return count


# print(count_vowels("applEe"))

def reverse_string(string: str) -> str:
  reversed_string = ""
  
  for i in range(len(string)):
    reversed_string = string[i] + reversed_string
  
  return reversed_string


# print(reverse_string("apple"))


def find_first_non_repeated_word(string: str) -> str|bool:
  if len(string) < 1:
    return ""
  
  sentence = unpack_words(string)
  
  for index in range(len(sentence)):
    unique = True
    for n in range(index + 1, len(sentence)):
      if sentence[index].lower() == sentence[n].lower():
        unique = False
    if unique:
      return sentence[index]
        
  return False

  
# print(find_first_non_repeated_word("Sometimes, a man in love is a man in trouble."))
def remove_duplicate_characters(string: str) -> str:
    if len(string) == 0:
        return ""
        
    n = 0
    length = len(string)
       
    while n < length:
        i = n + 1 
        while i < length:
            if string[n] == string[i]:
              if i == length-1:
                string = string[:i]
                # Slice out the duplicate character at index i
              else:
                string = string[:i] + string[i+1:]
                # Reduce the tracking length since the string shrank
                # Do NOT increment i; the next character shifted into index i
              length -= 1
            else:
                # Move to the next character only if no deletion happened
                i += 1
        n += 1
         
    # Corrected indentation: Return after BOTH loops finish
    return string


        
#  N starts with the same index as the first char in the string, for every resizing, the length of the string would decrease by 1,
# and a new char takes up that index. 
# print(remove_duplicate_characters("aaaaabuus"))


def is_palindrome(string: str) -> bool:
  length = len(string)
  n = 0
  mid = length//2
  print(mid)

  while n < mid:
    if string[n] != string[length-(n+1)]:
      return False
    n += 1

  return True


# print(is_palindrome("eve"))


def array_reversal_in_place(arr: list) -> list:
  mid = len(arr)//2
  n = 0

  while n < mid:
    arr[n], arr[len(arr)-(n+1)] = arr[len(arr)-(n+1)], arr[n]
    n+=1

  return arr


# print(array_reversal_in_place([1, 3, 7, 2]))

# The Substring Finder (indexOf)The Goal: Write a function that searches for a smaller string inside a larger string (e.g., finding "cat" inside "the scary cat").
# Return the starting index where it begins (9), or -1 if it is not found.The Hard Way Rule: You cannot use in, .find(), or .index(). 
# You have to use nested loops to manually match sequences of characters.

def substring_finder(string: str, substring: str):
  if len(string) == 0:
    return ""
  
  for index in range(len(string) - len(substring)+1):
    if string[index:index+len(substring)] == substring:
      return index
  
  return -1


# print(substring_finder("Remember Red, Hope is a good thing, and no good thing ever dies", ""))

def find_the_longest_word(string: str):

  if string == "":
    return ""

  word = ""
  longest_word = ""
  
  for index in range(len(string)):
    if string[index] == " ":
      if len(word) > len(longest_word):
        longest_word = word
      word = ""
      continue
    word += string[index]
    
  if len(word) > len(longest_word):
    longest_word = word

  return longest_word


# print(find_the_longest_word(quote))


def compress_chars(string: str):
  container = ""
  for index in range(len(string)):
    count = 0
    for i in range(len(string)):
      if string[index] == string[i]:
        count += 1
    if len(container) == 0:
      container += string[index]+str(count)
      # print(container)
    else:
      seen = False
      for n in range(len(container)):
        if container[n] == string[index]:
          seen = True
      if not seen:
        container += string[index]+str(count)
      
  return container


# print(compress_chars("aaabbcc"))


def compress_chars_2(string: str) -> str:
  result = ""
  
  for i in range(len(string)):
    
    seen = False
    for j in range(i):
      if string[i] == string[j]:
        seen = True
        break
    
    if seen:
      continue
    
    count = 0
    for n in range(len(string)):
      if string[n] == string[i]:
        count += 1
    
    result += string[i] + str(count)
  
  return result


# print(compress_chars_2("aaabbcc"))


# # * Compress `"aaabbcc"` → `"a3b2c2"`.

# aaabbccccdd

# ↓

# a3b2c4d2


# def run_length_encoding(string: str) -> str:
#   result = ""
  
#   for n in range(len(string)):
#     count = 0
#     for i in range(len(string)):
#       if string[i] != string[n]:
#         if count > 0:
#           result += string[n]+str(count)
#         break
#       count += 1
    
#   return result


def run_encoding_length(string: str):
    length = len(string)
    n = 0
    result = ""

    while n < length:
        count = 0
        i = n

        while i < length and string[i] == string[n]:
            count += 1
            i += 1

        result += string[n] + str(count)

        n += count

    return result


# print(run_encoding_length("aabbccddd"))


def max_of_vowels_in_substring_of_length_k(string: str, k: int):
  num = 0
  
  for n in range(len(string) - k + 1):
    count = 0
    
    for j in range(len(string[n:n+k])):
      if string[j+n] in "aeiou":
        count += 1
      else:
        break
  
    if count == k:
      return count

    if count > num:  # noqa: PLR1730
      num = count
      
  return num


print(max_of_vowels_in_substring_of_length_k("abaaacaa", 3))


# A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

# For example, take 153 (3 digits), which is narcissistic:

#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

# and 1652 (4 digits), which isn't:

#     1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938

# The Challenge:

# Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.

# This may be True and False in your language, e.g. PHP.

# Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.