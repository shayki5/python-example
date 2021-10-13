def longest_word(file):
    with open(file, 'r') as infile:
                words = infile.read().split()
    max_len = len(max(words, key=len))
    longestWord = ([word for word in words if len(word) == max_len])
    print("Longest word is: {}. num of chars: {}".format(longestWord, len(longestWord[0])))
    return(len(longestWord[0]))

if __name__ == "__main__":
    longest_word("/home/test.txt")