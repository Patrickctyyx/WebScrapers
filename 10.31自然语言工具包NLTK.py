from nltk import word_tokenize
from nltk import Text


tokens = word_tokenize('My name is Patrick, and I love yyx.')
text = Text(tokens)

# 依赖安装太慢了...
# skip
