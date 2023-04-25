def main():
  book_path = './books/frankenstein.txt'
  book_cotent = get_book(book_path)
  words = get_words(book_cotent)
  words_count = count_words(words)
  char_dict = get_char_dict(words)
  sorted_char = sort_char_dict(char_dict)
  alpha_list = filter_alpha(sorted_char)
  print_report(book_path, words_count, alpha_list)
  # print(alpha_list)

  
  
  
def get_book(path):
  with open(path) as f:
    content = f.read()
  return content
    
def get_words(content):
  return content.split()

def count_words(words):
  return len(words)
  
def get_char_dict(words):
  result = {}
  for word in words:
    for char in word:
      lower_char = char.lower()
      
      if lower_char in result:
        result[lower_char] += 1
      else: 
        result[lower_char] = 1
        
  return result

def sort_char_dict(char_dict):
  list = []
  for char in char_dict:
    list.append({ "char": char, "times": char_dict[char] })
    
  list.sort(key=lambda x: x['times'], reverse=True)  
  return list

def filter_alpha(list):
  return [ i for i in list if i["char"].isalpha()]

def print_report(file_name, words_count, char_list):
  print(f"--- Begin report of {file_name} ---")
  print(f"{words_count} words found in the document")
  print()
  
  for i in char_list:
    print(f"The '{i['char']}' character was found {i['times']} times")
    
  print("--- End report ---")
  
main()