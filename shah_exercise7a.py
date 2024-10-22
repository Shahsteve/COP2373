import re

def main():
   text = input("Enter sentences here: ")

   pat = r'[A-Z].*?[.!?](?= [A-Z]|$)'
   m = re.findall(pat, text, flags=re.DOTALL | re.MULTILINE)

   pat = r'.*?[.?!]'
   lst = re.findall(pat, text, flags=re.DOTALL)

   for i in m:
       print('->', i)

   print('There are', len(lst), 'sentences in your text.')

if __name__ == "__main__":
    main()