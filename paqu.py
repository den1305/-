import requests
import time
import hashlib
import re,json
import csv
import random
import pandas as pd

class TbSpider:

    def __init__(self):
        self.headers = {
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'tracknick=%5Cu6881%5Cu5FD7%5Cu65876661; enc=tcyfd2%2Bne4olUeN932mDiScGUckG5S5dGSh31d4BZga9o7yz93woIWZl7wb7vWPF8VQnX6ITJqErOQ83a4B0rA%3D%3D; _hvn_lgc_=0; havana_lgc2_0=eyJoaWQiOjI3MDc2NjQ3MTksInNnIjoiZDRiZWYxODJhMTAwYmRhOTljYjBmODEyOWVkOWI3OWMiLCJzaXRlIjowLCJ0b2tlbiI6IjFrX0ZYZV9QajZ3UjhuWE5PSDdkMTZRIn0; wk_cookie2=1753457d464623e0aa8b3d683cdceeee; wk_unb=UU8IO9LY1zIlag%3D%3D; sn=; lgc=%5Cu6881%5Cu5FD7%5Cu65876661; t=9912e2ad1a7ce9523c98cc120e014c28; cancelledSubSites=empty; dnk=%5Cu6881%5Cu5FD7%5Cu65876661; cna=Jjk/GT3LK0ICAXjGRqhyZ8cj; thw=cn; ariaDefaultTheme=undefined; cookie2=1d37ff1fa3b7f7aaa431dbd73135e7fc; _tb_token_=751b5a68f3fe8; mtop_partitioned_detect=1; _m_h5_tk=4ef7e7704795c21e3b6bb5bb98a1e1ed_1734924498428; _m_h5_tk_enc=a6b350170c85f1b2ec1a0e84b8ce1a31; _samesite_flag_=true; sgcookie=E100o3dbOrxEc%2F8S%2BRQan1m3i6hEmVIB%2BrlbsP4QTD%2BW2hP4pYU3KswSaOxW%2FfV%2BISijWziPVeVkM%2FeoM9zzYF80ginHTTpBZexer3%2BUewfaY04%3D; havana_lgc_exp=1766018420442; unb=2707664719; uc1=cookie14=UoYdWTAkzytizQ%3D%3D&cookie21=U%2BGCWk%2F7pY%2FF&pas=0&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D; uc3=nk2=okgNtK34wmjJ3A%3D%3D&id2=UU8IO9LY1zIlag%3D%3D&vt3=F8dD379%2B4vpNzZDwTXI%3D&lg2=UIHiLt3xD8xYTw%3D%3D; csg=d11abd01; cookie17=UU8IO9LY1zIlag%3D%3D; skt=6fea1784e951cf5d; existShop=MTczNDkxNDQyMA%3D%3D; uc4=nk4=0%40oErtPTCxZBgZNfH7nex1n8WIbpky&id4=0%40U22PHudVkL5pL2iP09b9NE63FqIj; _cc_=UIHiLt3xSw%3D%3D; _l_g_=Ug%3D%3D; sg=19f; _nk_=%5Cu6881%5Cu5FD7%5Cu65876661; cookie1=BvXn96sts19hw0PVOrW4%2Bx52puQsNNunBpPSHElF2Xg%3D; sdkSilent=1735000820445; havana_sdkSilent=1735000820445; xlly_s=1; tfstk=geFSaFVhJ3xW_BK0rgQqcfJJkTlQFk1wVegLSydyJbh-v-agA07hEbyjAoEj2Q7lEvnQqbH3UDorAXa3fZSN_1zurXDdbG5NV3Sksf8-J4KekIhER_sV3nzurXYDuHBaHzxQqw_t92ndlj3EyphKe2pxMm0e94EK2xKx5VcKvkEKDn3KRUp-JDpvkm0K9DEK9ZGxMOCjuai0PZup1PspHFUxcBdLGqsnXztMOqPxP4nTySRp9N3SFcU-DGapHoMY-vNH-BMzyRqnWuKRVXUj5lg_V98nV-UaaJU5GGhzZzetp5IHplG7AAF-hedQrbomGqFO8dm4G0rLNxQw1vlY_Ah83tjrLbg_v7qWRBETuPPonWs6DD2rSj37v1If4xAZfSyWdyveOqiNlZ9HKQez0D_jAF4teq02bZ_XQyD-oqiNlZ9HKY3muN7fldzh.; isg=BEBAPoT3M2vHWcs9kJ6L88XrEc4SySSTFsgrkLrRDtvuNeBfYttrI7gDTJ31g9xr',#设置成自己的cookies
            'pragma': 'no-cache',
            'referer': 'https://s.taobao.com/search?commend=all&finalPage=4&ie=utf8&initiative_id=tbindexz_20170306&page=2&q=%E6%96%B0%E4%BC%9A%E9%99%88%E7%9A%AE&search_type=item&sourceId=tb.index&spm=a21bo.jianhua%2Fa.201856.d13&ssid=s5-e&tab=all',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'script',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        }
        self.eS = '12574478'  # 固定
        self.eC = str(int(time.time() * 1000))  # 时间戳
        self.create_csv()

    def create_csv(self):
        f = open('商品信息.csv', 'w', encoding='utf-8', newline='')
        self.csv_writer = csv.DictWriter(f, fieldnames=[
            '标题',
            '原价(￥)',
            '售价(￥)',
            '净含量(g)',
            '省份',
            '城市',
            '销量',
            '店铺',
            '详情页'
        ])
        self.csv_writer.writeheader()

    def md5_encrypt(self,input_string): #md5
        md5_hash = hashlib.md5()
        md5_hash.update(input_string.encode('utf-8'))
        md5_hex = md5_hash.hexdigest()
        return md5_hex

    # 获取签名
    def get_sign(self,page,totalResults,sourceS,bcoffset,ntoffset):
        param = {'areaCode': 'CN',
     'bcoffset': bcoffset,
     'brand': 'HUAWEI',
     'categoryp': '',
     'client_os': 'Android',
     'countryNum': '156',
     'debug_rerankNewOpenCard': 'false',
     'device': 'HMA-AL00',
     'elderHome': 'false',
     'endPrice': None,
     'end_price': None,
     'filterTag': '500016663:524468638,500016663:526190408,500016663:524398021,500016663:524421050,500016663:524568459,500016663:524461093,500016663:524500689,500016663:524314493,500016663:524392878,500016663:524454621,500016663:524226743,500016663:524380289,500016663:524268360',
     'from': 'nt_history',
     'gpsEnabled': 'false',
     'grayHair': 'false',
     'hasPreposeFilter': 'false',
     'homePageVersion': 'v7',
     'index': '4',
     'info': 'wifi',
     'isBeta': 'false',
     'isEnterSrpSearch': 'true',
     'itemIds': None,
     'loc': '',
     'm': 'pc',
     'myCNA': '+zW9H3gLal4CAXAglROQv4vH',
     'n': 48,
     'needTabs': 'true',
     'network': 'wifi',
     'newSearch': 'false',
     'ntoffset': ntoffset,
     'p4pIds': None,
     'p4pS': None,
     'page': page,
     'pageSize': 48,
     'pageSource': 'a21bo.jianhua/a.201867-main.d10_first.5af92a89O8hh23',
     'prepositionVersion': 'v2',
     'prop': '500016663:524468638,500016663:526190408,500016663:524398021,500016663:524421050,500016663:524568459,500016663:524461093,500016663:524500689,500016663:524314493,500016663:524392878,500016663:524454621,500016663:524226743,500016663:524380289,500016663:524268360',
     'q': '%E6%96%B0%E4%BC%9A%E9%99%88%E7%9A%AE',
     'qSource': 'url',
     'rainbow': '',
     'schemaType': 'auction',
     'searchDoorFrom': 'srp',
     'searchElderHomeOpen': 'false',
     'search_action': 'initiative',
     'service': '524468638,526190408,524398021,524421050,524568459,524461093,524500689,524314493,524392878,524454621,524226743,524380289,524268360',
     'sort': '_coefp',
     'sourceS': sourceS,
     'startPrice': None,
     'start_price': None,
     'style': 'list',
     'subtype': '',
     'sugg': '_4_1',
     'sversion': '13.6',
     'tab': 'all',
     'totalPage': 100,
     'totalResults': totalResults,
     'ttid': '600000@taobao_pc_10.7.0',
     'vm': 'nw'}

        info_data = {
            'appId':'34385',
            'params':json.dumps(param)
        }
        data = json.dumps(info_data).replace(' ','')
        m_h5 = re.findall('_m_h5_tk=(.*?);',self.headers.get('cookie'))[0]
        tc = m_h5.split('_')
        # s = token + "&" + eC + "&" + eS + "&" +data
        s = tc[0]+ "&" + self.eC + "&" +self. eS + "&" +data
        # print(int(tc[1])-int(self.eC))
        # print(md5_encrypt(s))
        return self.md5_encrypt(s),data

    # 获得解析数据
    def get_data(self,page,totalResults,sourceS,bcoffset,ntoffset):
        sign,data = self.get_sign(page,totalResults,sourceS,bcoffset,ntoffset)
        params = {
            'jsv': '2.7.4',
            'appKey': self.eS,
            't': self.eC,
            'sign': sign,
            'api': 'mtop.relationrecommend.wirelessrecommend.recommend',
            'v': '2.0',
            'timeout': '10000',
            'type': 'jsonp',
            'dataType': 'jsonp',
            'callback': 'mtopjsonp8',
            'data': data
        }

        response = requests.get(  'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/',
            params=params,
            headers=self.headers,
        )
        # print(response.text)
        json_str = re.findall('mtopjsonp\d+\((.*)\)',response.text)[0]
        json_data = json.loads(json_str)
        # print(json_data)
        itemsArray = json_data['data']['itemsArray']
        for i in itemsArray:
            title = i['title'].replace('<span class=H>','').replace('</span>','')
            city_info = i['procity'].split(' ')
            if (len(city_info) == 2):
                pro = city_info[0]
                city = city_info[1]
            else:
                pro = city_info[0]
                city = ''
            weight = ''
            category = ''
            if i.get('structuredUSPInfo'):
                for j in i.get('structuredUSPInfo'):
                    if j['propertyName'] == '净含量':
                        weight = j['propertyValueName'].replace('g','')
                    # if j['propertyName'] == '特产品类':
                    #     category = j['propertyValueName']
            dit = {
                '标题':title,
                '原价(￥)':i['price'],
                '售价(￥)':i['priceShow']['price'],
                '净含量(g)':weight,
                '省份':pro,
                '城市':city,
                '销量':i['realSales'].replace('人付款','').replace('+','').replace('万','0000'),
                '店铺':i['nick'],
                '详情页': 'https:' + i['auctionURL']
            }
            self.csv_writer.writerow(dit)
            print(dit)
        # print(dit)
        totalResults = json_data['data']['mainInfo']['totalResults']
        sourceS = json_data['data']['mainInfo']['sourceS']
        bcoffset = json_data['data']['mainInfo']['bcoffset']
        ntoffset = json_data['data']['mainInfo']['ntoffset']
        return totalResults,sourceS,bcoffset,ntoffset


    def main(self):
        totalResults = 4800
        sourceS = ''
        bcoffset = ''
        ntoffset = ''

        for i in range(1,10):#页数
            time.sleep(random.randint(2, 4))
            totalResults,sourceS,bcoffset,ntoffset = self.get_data(i,totalResults,sourceS,bcoffset,ntoffset)



if __name__ == '__main__':
    t = TbSpider()
    t.main()

    #数据预处理
    data = pd.read_csv('商品信息.csv')
    data = data.drop_duplicates()  # 去除重复行
    data = data.dropna(subset=['售价(￥)','销量'], inplace=False)  # 去除缺失的行
    data = data[~data['销量'].str.contains('人看过')]
    data.to_csv('商品信息.csv', index=False)
    print(data)








