# 导入模块
import requests
import csv

# 指定url
url = 'https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job'

# 设置请求头参数
head = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '406',
    'Content-Type': 'application/json;charset=UTF-8;',
    'Cookie': 'XSRF-TOKEN=Bh2gi6GcTtqIvM4lrU3m4g; __gc_id=f204bf9d8cc34c659470e09660711986; _ga=GA1.1.1267984231.1683208911; __uuid=1683208911082.70; __tlog=1683208911084.44%7C00000000%7C00000000%7C00000000%7C00000000; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1683208911; __session_seq=13; __uv_seq=13; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1683210035; _ga_54YTJKWN86=GS1.1.1683208911.1.1.1683211483.0.0.0',
    'Host': 'api-c.liepin.com',
    'Origin': 'https://www.liepin.com',
    'Referer': 'https://www.liepin.com/',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'X-Client-Type': 'web',
    'X-Fscp-Bi-Stat': '{"location": "https://www.liepin.com/zhaopin/?inputFrom=www_index&workYearCode=0&key=python&scene=input&ckId=wodpawgkbhefdidqtq1hso4xqml8alw9&dq="}',
    'X-Fscp-Fe-Version': '',
    'X-Fscp-Std-Info': '{"client_id": "40108"}',
    'X-Fscp-Trace-Id': '046a4cc3-72bc-4b95-8f7a-c39df3ee11d8',
    'X-Fscp-Version': '1.1',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'Bh2gi6GcTtqIvM4lrU3m4g',
}

# 表格数据
csvList = []

# 获取前两页数据
for i in range(0, 2):

    # post请求参数
    data = {"data":{"mainSearchPcConditionForm":{"city":"410","dq":"410","pubTime":"","currentPage":i,"pageSize":40,"key":"python","suggestTag":"","workYearCode":"0","compId":"","compName":"","compTag":"","industry":"","salary":"","jobKind":"","compScale":"","compKind":"","compStage":"","eduLevel":""},"passThroughForm":{"scene":"input","skId":"","fkId":"","ckId":"vmglvn6pyc3nv5scebhp02euhaexpkd8"}}}

    # 发送请求
    res = requests.post(url, headers=head, json=data)

    # 获取响应内容
    json_data = res.json() # 获取json格式的数据
    result = json_data['data']['data']['jobCardList']
    # print(result)

    # 循环获取所需数据
    for j in result:
        # 职位名称
        title = j['job']['title']
        # 薪资
        salary = j['job']['salary']
        # 公司地点
        compName = j['comp']['compName']
        # 打印所需数据
        print(title, salary, compName)

        # 追加表格数据
        csvList.append((title, salary, compName))
# print(csvList)

# 规定表头
tableHead = ('职位名称','薪资','公司地点')

# 创建文件对象
with open('liepin.csv', 'w', encoding='utf-8-sig', newline='') as f:
    # 创建csv写入对象
    writer = csv.writer(f)
    # 写入表头
    writer.writerow(tableHead)
    # 写入数据
    writer.writerows(csvList)