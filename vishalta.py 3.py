# Outer loop for rows
for i in range(1, 6):  # Change 6 to desired number of rows (5 for a complete pyramid)
  # Inner loop for spaces before numbers (adjust spacing for different pyramid shapes)
  for j in range(6 - i):
    print(" ", end="")
  # Inner loop for printing numbers in increasing order
  for j in range(1, i + 1):
    print(j, end=" ")
  # Move to next line
  print()

def remove_vowels(text):
  """Removes all vowels from a string.

  Args:
      text: The string to remove vowels from.

  Returns:
      A new string with all vowels removed.
  """
  vowels = 'aeiouAEIOU'
  return ''.join([char for char in text if char not in vowels])

# Example usage
text = "This is a string with vowels."
text_without_vowel = remove_vowels(text)
print(text_without_vowel)  # Output: Ths s  strng wth vwls.

def count_unique_characters(text):
  """Counts the number of unique characters in a string.

  Args:
      text: The string to count unique characters in.

  Returns:
      The number of unique characters in the string.
  """
  return len(set(text))

# Example usage
text = "Hello, world!"
unique_chars = count_unique_characters(text)
print(unique_chars)  # Output: 12

def is_palindrome(text):
  """Checks if a string is a palindrome (reads the same backward as forward).

  Args:
      text: The string to check.

  Returns:
      True if the string is a palindrome, False otherwise.
  """
  # Convert to lowercase and remove non-alphanumeric characters
  text = ''.join(char.lower() for char in text if char.isalnum())
  # Check if the reversed string is equal to the original
  return text == text[::-1]

# Example usage
text1 = "Race car"
text2 = "Hello, world!"

print(is_palindrome(text1))  # Output: True
print(is_palindrome(text2))  # Output: False

def count_words(text):
  """Counts the number of words in a string.

  Args:
      text: The string to count words in.

  Returns:
      The number of words in the string.
  """
  word_count = 0
  in_word = False
  for char in text:
    if char.isspace():
      if in_word:
        word_count += 1
      in_word = False
    else:
      in_word = True
  if in_word:  # Handle the last word if it doesn't end with space
    word_count += 1
  return word_count

# Example usage
text = "This is a string with multiple words."
word_count = count_words(text)
print(word_count)  # Output: 5

def is_anagram(str1, str2):
  """Checks if two strings are anagrams (have the same characters with different arrangement).

  Args:
      str1: The first string.
      str2: The second string.

  Returns:
      True if the strings are anagrams, False otherwise.
  """
  # Convert strings to lowercase and remove non-alphanumeric characters
  str1 = ''.join(char.lower() for char in str1 if char.isalnum())
  str2 = ''.join(char.lower() for char in str2 if char.isalnum())

  # Check if string lengths are equal (anagrams must have the same length)
  if len(str1) != len(str2):
    return False

  # Create a character count dictionary for str1
  char_counts = {}
  for char in str1:
    char_counts[char] = char_counts.get(char, 0) + 1

  # Check if characters in str2 can be formed from str1's character counts
  for char in str2:
    if char not in char_counts or char_counts[char] == 0:
      return False
    char_counts[char] -= 1

  # All characters in str2 were found in str1 with matching counts (anagram)
  return True

# Example usage
str1 = "listen"
str2 = "silent"
print(is_anagram(str1, str2))  # Output: True

str1 = "apple"
str2 = "papel"
print(is_anagram(str1, str2))  # Output: True

str1 = "cinema"
str2 = "iceman"
print(is_anagram(str1, str2))  # Output: False (different character sets)
