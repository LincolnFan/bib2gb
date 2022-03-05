# coding = utf-8
import bibtexparser
from bibtexparser.customization import convert_to_unicode
# 解析bib
with open('article.bib') as f:
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    parser.customization = convert_to_unicode
    bib_data = bibtexparser.load(f, parser=parser).entries[0]
print('*'*50)
for key, value in bib_data.items():
    print('{key}:{value}'.format(key=key, value=value))

# 生成国标

'''
文献中的作者数量低于三位时全部列出；
超过三位时只列前三位，其后加“等”字即可；
作者姓名之间用逗号分开；
中外人名一律采用姓在前，名在后的著录法

（2）论文集、会议录
【论文集格式】	[序号]作者. 论文集名称[C]. 出版地: 出版者, 出版年份: {起始页码}.
【会议论文格式】	[序号]作者. 篇名[A]. // 论文集名称[C], 出版地: 出版者, 出版年份: 起始页码.
【示例】
[1]	辛希孟. 信息技术与信息服务国际研讨会论文集: A集[C]. 北京: 中国社会科学出版社, 1994: 12-17.
[2]	伍蠡甫. 西方文论选[C]. 上海: 上海译文出版社, 1979.

 （7）期刊中析出的文献
【格式】[序号]作者. 篇名[J]. 刊名, 出版年份, 卷号(期号): 起止页码.
【示例】
[1]	陆庆, 周世杰, 秦志光, 等. 对等网络流量检测技术 [J]. 电子科技大学学报:自然科学版, 2007, 36(7): 1333-1337.
[2]	Bernaille, L., Teixeira, R., Akodkenou, I., et al. Traffic classification on the fly [J]. ACM SIGCOMM Computer Communication Review, 2006, 36(2): 23-26.

'''


def author2gb(author):
    authors = []
    author_gb = ''
    authors = author.split(' and')
    if len(authors) > 3:
        author_gb = '{a0}, {a1}, {a2}, eta al '.format(a0=authors[0], a1=authors[1], a2=authors[2])
    elif len(authors) > 0:
        for item in authors:
            author_gb = author_gb + item + ', '
        author_gb = author_gb[0:-2]
    author_gb = author_gb.replace('\n', '')
    return author_gb


# print(author2gb(bib_data['author']))

cite_gb = ''
if bib_data['ENTRYTYPE'] == 'inproceedings' or bib_data['ENTRYTYPE'] == 'conference':  # 会议集
    cite_gb = '[序号]{作者}. {论文集名称}[C]. {出版地}: {出版者}, {出版年份}: {起止页码}'.format(
        作者=author2gb(bib_data['author']), 论文集名称=bib_data['booktitle'], 出版地=bib_data['address'],
        出版者=bib_data['publisher'], 出版年份=bib_data['year'], 起止页码=bib_data['pages']
    )
if bib_data['ENTRYTYPE'] == 'article':  # 期刊杂志
    cite_gb = '[序号]{作者}. {篇名}[J]. {刊名}, {出版年份}, {卷号}: {起止页码}.'.format(
        作者=author2gb(bib_data['author']), 篇名=bib_data['title'], 刊名=bib_data['journal'],
        出版年份=bib_data['year'], 卷号=bib_data['volume'], 起止页码=bib_data['pages']
    )
# 因为

print(cite_gb)

'''
@article          An article from a journal or magazine 

@book             A book with an explicit publisher

@booklet          A work that is printed and bound, but without a named publisher or sponsoring institution 

@conference       The same as inproceedings
@inbook           A part of a book, which may be a chapter (or section or whatever) and/or a range of pages

@incollection     A part of a book having its own title

@inproceedings    An article in a conference proceedings
@manual  Technical documentation

@mastersthesis    A Master's thesis

@misc             Use this type when nothing else fits

@phdthesis        A PhD thesis

@proceedings      The proceedings of a conference

@techreport       A report published by a school or other institution, usually numbered within a series

@unpublished      A document having an author and title, but not formally published

@collection       Not a standard entry type. Use proceedings instead.

@patent           Not a standard entry type.
'''