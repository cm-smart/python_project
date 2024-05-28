import jieba
def context_jieba(data):
    result = list()

    words = jieba.cut_for_search(data)
    for word in words:
        result.append(word)

    return result

def filter_words(data):
    """过滤不要的词，谷，帮，客"""
    return data not in ['谷','帮','客']

def replace_words(data):
    if data == '传智播':
        data = '传智播客'
    if data == '院校':
        data = '院校帮'
    if data == '博学':
        data = '博学谷'
    return data
def create_words(data):
    return (replace_words(data),1)

def user_words_map(data):
    userId = data[0]
    content = data[1]
    result = list()

    # 拆分词组
    words = context_jieba(content)
    # 过滤不需要的词
    for word in words:
        if filter_words(word):
            r_word = replace_words(word)
            result.append((userId + '_' + r_word,1))
    return result