import requests as req

# 取得資料
def getdata(url):
    pc = req.get(url)
    # pc.text   檢視網頁內容
    import json
    datas = json.loads(pc.text)
    datas = datas['prods']   # (字典型態)網頁資料裡的prods字典
    return datas

# 取得商品名稱
def name(datas):
    for data in datas:
        name = data['name']
        print(name)
    return name

# 主要函式
def main():
    url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/category/DGBJ/results?q=switch&page=1&sort=sale/dc'
    datas = getdata(url)
    print(name(datas))

# 呼叫使用
main()

