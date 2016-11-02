from urllib.request import urlopen
from random import randint


def wordListSum(wordlist):
    sums = 0
    for word, value in wordlist.items():
        sums += value
    return sums


def retrieveRandomWord(wordlist):
    randIndex = randint(1, wordListSum(wordlist))
    for word, value in wordlist.items():
        # 在所有结果中用比较高级的方法随便找一个词
        randIndex -= value
        if randIndex <= 0:
            return word


def bulidDict(text):
    text = text.replace('\n', ' ')
    text = text.replace('\"', '')

    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        # 用后面的代替前面的
        text = text.replace(symbol, ' ' + symbol + ' ')

    words = text.split(' ')
    words = [word for word in words if word != '']

    # 这是双侧dict
    # 第一层放的是词语
    # 对应的value又是一个dict
    # 这个dict里面就是后面跟的词语和出现的次数
    wordDict = {}
    for i in range(1, len(words)):
        if words[i - 1] not in wordDict:
            wordDict[words[i - 1]] = {}
        if words[i] not in wordDict[words[i - 1]]:
            wordDict[words[i - 1]][words[i]] = 0
        wordDict[words[i - 1]][words[i]] += 1

    return wordDict


def main():
    text = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(),
               'utf-8')
    wordDict = bulidDict(text)

    length = 100
    chain = ''
    currentWord = 'I'
    for i in range(0, length):
        chain += currentWord + ' '
        currentWord = retrieveRandomWord(wordDict[currentWord])
    print(chain)

if __name__ == '__main__':
    main()

# 这个简直amazing
# 乍一看句子还make sense
# 机器学习的一个开始，连着的两个词都有一定的关联性
