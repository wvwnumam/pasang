# Open data.txt file
file = open("data.txt", 'a')

# Main class
class pasang():

    # Adding same word
    def pair(self, word):
        for i in range(len(word)):
            file.write('\n' + word[i])


pasang = pasang()
wordlist = list()
confirm = 'y'

# Input
while confirm == 'y' or confirm == 'Y':
    word = input('\ninput word: ')
    wordlist.append(word)
    confirm = input('do you wanna add more word? (y/n): ')

# Process
pasang.pair(wordlist)

# Output
file = open('data.txt', 'r')
print(file.read())

file.close()