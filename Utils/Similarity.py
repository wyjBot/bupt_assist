import jieba,re
import gensim
#获取指定路径的文件内容
def get_file_contents(path):
    str = ''
    f = open(path, 'r', encoding='UTF-8')
    line = f.readline()
    while line:
        str = str + line
        line = f.readline()
    f.close()
    return str
#将读取到的文件内容先进行jieba分词，然后再把标点符号、转义符号等特殊符号过滤掉
def filter(str):
    str = jieba.lcut(str)
    result = []
    for tags in str:
        if (re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", tags)):
            result.append(tags)
        else:
            pass
    return result
#传入过滤之后的数据，通过调用gensim.similarities.Similarity计算余弦相似度
def calc_similarity(text1,text2):
    texts=[text1,text2]
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim

if __name__ == '__main__':

    str1="""
通过写存储器操作将手工汇编的程序写入存储器。 
通过读寄存器，检查写入寄存器的数据是否正确。
"""
    str2="""
通过读存储器操作，将指令逐条读出，检查写入是否正确。 
通过写寄存器操作，将数12H写入寄存器R2，0FH写入寄存器R3。 
    """
    text1 = filter(str1)
    text2 = filter(str2)
    print(text1,text2)
    similarity = calc_similarity(text1, text2)
    print("Test1:文章相似度： %.4f"%similarity)
    str1="中国面积最大的省级行政区是新疆"
    str2="新疆乃中国面积最大的省级行政区"
    text1 = filter(str1)
    text2 = filter(str2)
    print(text1,text2)
    similarity = calc_similarity(text1, text2)
    print("Test2:文章相似度： %.4f"%similarity)