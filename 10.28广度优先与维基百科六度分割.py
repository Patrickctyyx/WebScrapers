import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='ctyyx',
                       db='mysql',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
cur.execute('USE patscraper')


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


def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree:
            return {}
    if targetPageId in linkTree.keys():
        print('TARGET ' + str(targetPageId) + ' FOUND!')
        raise SolutionFound('PAGE: ' + str(currentPageId))

    for branchKey, branchValue in linkTree.items():
        try:
            linkTree[branchKey] = searchDepth(targetPageId, branchKey,
                                              branchValue, depth - 1)
        except SolutionFound as e:
            print(e.message)
            raise SolutionFound('PAGE: ' + str(currentPageId))
    return linkTree

try:
    linkTree = searchDepth(18, 1, {}, 4)
    print('No solution found')
except SolutionFound as e:
    print(e.message)
