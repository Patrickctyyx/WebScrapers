import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='passwd',
                       db='mysql',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
cur.execute('USE patscraper')


# 有两个作用第一个用来捕捉错误
# 集成了RuntimeError类来捕捉超时情况
# 另外就是用来发送message
class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message


def getLinks(fromPageId):
    cur.execute('SELECT to_page_id FROM links WHERE from_page_id = %s', fromPageId)
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]


def constructDict(currentPageId):
    links = getLinks(currentPageId)
    if links:
        # 得到类似这样的结果{1: {}, 2: {}, 3: {}, 4: {}, 5: {}}
        return dict(zip(links, [{}] * len(links)))
    return {}


# 几层递归来建立一个当前id到目标id的一个连接树
# 这个linkTree也是一个多层的dict
def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree:
            return {}  # 这个就相当于not linkTree
    # 先找到与目标链接的联系,主要是为了提个醒
    if targetPageId in linkTree.keys():
        print('TARGET ' + str(targetPageId) + ' FOUND!')
        raise SolutionFound('PAGE: ' + str(currentPageId))
    # 然后就一直往里面找了直到达到递归的极限
    for branchKey, branchValue in linkTree.items():
        try:
            linkTree[branchKey] = searchDepth(targetPageId, branchKey,
                                              branchValue, depth - 1)
        except SolutionFound as e:
            print(e.message)
            raise SolutionFound('PAGE: ' + str(currentPageId))
    return linkTree

try:
    linkTree = searchDepth(18653, 1, {}, 4)
    if not linkTree:
        print('No solution found')
except SolutionFound as e:
    print(e.message)
