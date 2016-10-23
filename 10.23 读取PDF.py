from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO


# 这个例子只是对pdfminer的一个比较初级的用法
# 之所以步骤这么多
# 是因为pdf相对于csv复杂性高了很多
# 所以处理的情况也复杂多了
# 但由于这里没涉及到图片之类的
# 于是看起来就像有很多多余的步骤一样
# 最后吐槽一下这个模块的文档不好啊... Not friendly...
def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()  # 创建pdf资源管理器
    retstr = StringIO()  # 具有文件属性的字符串
    laparams = LAParams()  # 创建参数分析器
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)  # 转移的准备

    process_pdf(rsrcmgr, device, pdfFile)  # pdf文件内容转移到retstr中
    device.close()

    content = retstr.getvalue()  # 读取这个对象的内容
    retstr.close()
    return content

pdfFile = urlopen('http://pythonscraping.com/pages/warandpeace/chapter1.pdf')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()
