import requests as req

# 取得資料
def getdata(url):
    pc = req.get(url)
    # pc.text   檢視網頁內容
    import json
    datas = json.loads(pc.text)
    datas = datas['prods']   # (字典型態)網頁資料裡的prods字典
    # print(datas)
    return datas

# (1)取得商品資訊-名稱/圖片/價格
def information(datas):
    lists = []
    for data in datas:
        name = data['name']
        img = 'https://b.ecimg.tw'+ data['picB']
        price = data['price']
        urlid = 'https://24h.pchome.com.tw/prod/' + data['Id']
        lists.append([name, img, urlid, price])
    return lists

# 轉換格式
def content(datas, keyword):
    for line in datas:
        name = line[0]
        if keyword == 'a':
            print('名稱：', line[0], '\n圖片：', line[1], '\n網址：', line[2], '\n價格：', line[3], '\n')
        elif  keyword in name:
            print('名稱：', line[0], '\n圖片：', line[1], '\n網址：', line[2], '\n價格：', line[3], '\n')

# ========================================= #

# 主要函式
def main():
    count = int(1)
    keyword = input('輸入關鍵字：')
    page = input('輸入搜尋次數：')
    page = int(page) + 1
    while count<page:
        url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/category/DGBJ/results?q=SWitch&page=' + str(count) + '&sort=prc/dc'
        print('【第', count , '筆資料】')
        count += 1
        datas = getdata(url)
        datas = information(datas)
        print(content(datas, keyword))
        print('=====================================================')


# 呼叫使用
main()