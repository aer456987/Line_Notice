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
        urlid = 'https://24h.pchome.com.tw/prod/' + data['Id']
        price = data['price']
        lists.append([name, img, urlid, price])
    return lists

# 搜尋關鍵字
def content(datas, keyword):
    switch = ['Switch', 'SWITCH', 'switch', 'Nintendo Switch', '任天堂']
    lite = ['Switch lite', 'switch lite', 'switchlite', 'Switchlite', 'lite', 'Lite', 'Nintendo Switch Lite']
    token = '**token**'
    
    for line in datas:
        title = line[0]
        name = '名稱：' + line[0] + '\n'
        img = '圖片：' + line[1] + '\n'
        urlid = '網址：' + line[2] + '\n'
        price = '價格：' + str(line[3]) + '\n'
        content = name, img, urlid, price
        
        if keyword == 'a':
            lineNotifyMessage(token, content)
        if keyword in switch:
            keyword = 'Switch'
        elif keyword in lite:
            keyword = 'Switch Lite'
        if keyword in title:
            lineNotifyMessage(token, content)

# Line通知
def lineNotifyMessage(token, *msg):
    headers = {
        'Authorization' : 'Bearer ' + token,
        'Content-Type' : 'application/x-www-form-urlencoded'
    }
    payload = {'message': msg}
    r = req.post('**URL**', headers = headers, params = payload) #補網址
    return r.status_code

# ========================================= #

# 主要函式
def main():
    count = int(1)
    keyword = input('輸入關鍵字：')
    page = input('輸入搜尋次數：')
    page = int(page) + 1
    while count<page:
        url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/category/DGBJ/results?q=SWitch&page=' + str(count) + '&sort=prc/dc'
        # print('【第', count , '次搜尋】')
        count += 1
        datas = getdata(url)
        datas = information(datas)
        print(content(datas, keyword))
        # print('=====================================================')

# 呼叫使用
main()





