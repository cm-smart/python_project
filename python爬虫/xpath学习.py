from lxml import etree

# 本地解析：etree.parse('')
# 服务器返回数据解析：etree.HTML()

tree = etree.parse('xpath的基本使用.html')

li_list = tree.xpath('//body/ul/li')

print(li_list)

# 查找所有有id属性的li标签
li_list = tree.xpath('//ul/li[@id]')
print(li_list)

# 查找所有有id属性的li标签的内容
li_list = tree.xpath('//ul/li[@id]/text()')
print(li_list)

# 查找所有有id属性的li标签,并且id=l1
li_list = tree.xpath('//ul/li[@id="l1"]')
print(li_list)

# 查找id=l1的li标签的class的属性值
cla = tree.xpath('//ul/li[@id="l1"]/@class')
print(cla)

# 查询id中包含1的li标签
li_list = tree.xpath('//ul/li[contains(@id,"1")]/text()')
print(li_list)

# 查询id的值以l开头的li标签
li_list = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')