# coding:utf-8
"""爬虫
    汽车之家的口碑数据

    _> scrapy runspider -s JOBDIR=jobs/autohome-01 spiders/autohome.py

    @author Liu Shengguo
    @date 2019-1-9
"""
import scrapy
import csv, json, sys, copy
from praise.items import PraiseItem

class AutohomeSpider(scrapy.Spider):
    name = "autohome"  # spider name
    page_dict = {}

    def start_requests(self):
        prd_dict = self.get_data_dict()
        for pdict in prd_dict:
            page_url = self.prd_kburl_gentator(pdict)
            # 爬取到的页面 提交给parse方法处理
            yield scrapy.Request(page_url, callback=self.parse, meta={'cur_dict': pdict})

    def parse(self, response):
        """start_requests已经爬取到页面
            eleStyle = response.css('style::text').extract_first()
        """
        cur_dict = copy.copy(response.meta['cur_dict'])
        jstr = bytes.decode(response.body)
        jsonobj = json.loads(jstr)
        if 0 != jsonobj.get('returncode'):
            self.logger.warning('request failed: autohome_pid=%d' %(cur_dict['autohome_pid']))
        ret = jsonobj.get('result')
        listdata = []
        if ret and ret.get('list'):
            listdata = ret.get('list')
        if 0 >= len(listdata):
            self.logger.warning('request data an empty: url %s' %(response.url))
        if None == self.page_dict.get(cur_dict['autohome_pid']):
            self.page_dict[cur_dict['autohome_pid']] = int(ret.get('pagecount'))

        # content
        ptyear = 2018
        for k_dict in listdata:
            posttime = k_dict.get('posttime')
            ptyear = int(posttime.split('-')[0])
            if not ptyear or ptyear < 2018:
                continue
            if k_dict.get('Koubeiid'):
                kou_url = self.kou_detail_url(k_dict.get('Koubeiid'))
                yield response.follow(kou_url, callback=self.content, meta={'cur_dict': cur_dict})
                # break  # TODO 去掉 break

        # next
        pages = self.page_dict[cur_dict['autohome_pid']]
        if 1 < pages:
            for page in range(2,pages+1):
                if ptyear < 2018:  # 口碑发布的时间不能小于 2018年
                    break
                next_url = self.get_next_url(cur_dict, page)
                yield scrapy.Request(next_url, callback=self.parse, meta={'cur_dict': cur_dict})

    def content(self, response):
        cdict = copy.copy(response.meta['cur_dict'])
        jstr = bytes.decode(response.body)
        jsonobj = json.loads(jstr)
        if 0 != jsonobj.get('returncode'):
            self.logger.warning('request content an empty: url %s' %(response.url))
        ret = jsonobj.get('result')
        columns = {}
        if ret:
            columns['line_id'] = cdict['xgo_lid']
            columns['product_id'] = cdict['xgo_pid']
            columns['autohome_id'] = cdict['autohome_pid']
            columns['username'] = ret.get('userName')
            columns['koubei_id'] = int(ret.get('eid'))
            columns['product_name'] = ret.get('brandname') +'|'+ ret.get('seriesname') +'|'+ ret.get('specname')
            columns['score_wg'] = int(ret.get('apperanceScene').get('score'))
            columns['score_ssd'] = int(ret.get('comfortablenessScene').get('score'))
            columns['score_xjb'] = int(ret.get('oilScene').get('score'))
            columns['buy_price'] = ret.get('boughtPrice')
            columns['buy_date'] = ret.get('boughtdate')
            columns['prov_name'] = ret.get('boughtprovincename')
            columns['city_name'] = ret.get('boughtcityname')
            columns['car_merit'] = ret.get('bestScene').get('feeling')  # 优点
            columns['car_defect'] = ret.get('worstScene').get('feeling')  # 缺点
            columns['car_oil'] = ret.get('actualOilConsumption')  # 油耗
            columns['pub_date'] = ret.get('lastEdit')  # 发表日期

        item = PraiseItem()
        item['columns'] = columns
        yield item

    def get_data_dict(self):
        # 多任务跑
        f_suffix = ''
        for arg in sys.argv:
            arg_li = 0 <= arg.find('=') and arg.split('=') or ''
            if type(arg_li) == list and arg_li[0] == 'JOBDIR':
                f_num = (arg_li[1].split('-'))
                if 1 < len(f_num):
                    f_suffix = '_%s' % f_num[1]
        settings = self.settings
        csvpath = settings['APP_PATH'] + ('/data/product%s.csv' % f_suffix)
        print(csvpath)
        prdli = []
        # inum = 0
        with open(csvpath, 'r', encoding='gbk') as csvfile:
            for row in csv.reader(csvfile):
                prdli.append({'xgo_pid': int(row[0]), 'xgo_lid': int(row[2]), 'autohome_pid': int(row[7])})
                # inum += 1
                # if inum > 1:  # TODO 去掉 break
                #     break

        return prdli

    def prd_kburl_gentator(self, cur_dict):
        return 'https://koubei.app.autohome.com.cn/autov9.8.5/alibi/specsalibiinfos-pm2-sp%d-st0-p1-s20-isstruct1-o0-a0.json' %(cur_dict['autohome_pid'])

    def get_next_url(self, cur_dict, page):
        return 'https://koubei.app.autohome.com.cn/autov9.8.5/alibi/specsalibiinfos-pm2-sp%d-st0-p%d-s20-sk0-isstruct0-o0-a0.json' %(cur_dict['autohome_pid'], page)

    def kou_detail_url(self, kbid):
        if kbid:
            return 'https://%s/autov9.8.5/alibi/NewEvaluationInfo.ashx?pm=1&eid=%d&useCache=1' %('123.138.60.191', int(kbid))
        else:
            return None
