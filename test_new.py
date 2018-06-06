import codecs
import jieba
#import sys
import timeit
s1=timeit.default_timer()
#timeit.timeit("sum(range(100))")

#读取文本文件数据
def getData(filename):
    fp = codecs.open(filename,'r','gbk')
    arr = []
    for lines in fp.readlines():
        lines = lines.replace("\r\n","").split('/')
        arr.append(lines)
    ar = [a for a in arr if len(a) != 0]
    ar = dict(ar)
    return ar

#识别输入字符串中的查询目的是查询产品还是机构
def orgnize_org_prd(input_string):
    word_dic_file = 'word_dict.txt'
    prd_file = 'prd_name_dict0428.txt'
    org_file = 'org_name_dict0428.txt'

    prd_dic = getData(prd_file)
    org_dic = getData(org_file)

    # 结巴分词
    jieba.load_userdict(word_dic_file)  # 添加自定义词库

    #input_string = '我家乡的余额宝'

    wordlist = jieba.cut(input_string, cut_all=False)
    vocabStr = "/".join(wordlist)
    vocabList = vocabStr.split('/')
    print(vocabList)
    result = []
    for word in vocabList:
        if word in org_dic:
            result.append(org_dic[word])
        elif word in prd_dic:
            result.append(prd_dic[word])

    tar = ''
    if len(result) != 0:
        # org_count = result.count('org')
        # prd_count = result.count('prd')
        if 'prd' in result:
            tar = tar + 'prd'
        elif 'prd' not in result and 'org' in result:
            tar = tar + 'org'
    else:
        print('no find')
    return tar

#orgnize_org_prd(sys.argv[1])
input_list = ["找廊坊银行","找北京的银行","找薪金宝","找微众银行的理财产品","找廊有财","找五大行的理财","找河北省的银行"]

for str in input_list:
    print(orgnize_org_prd(str))
'''
input_list = "找廊坊银行"
print(orgnize_org_prd(input_list))
'''
d1=timeit.default_timer()
print(d1-s1)