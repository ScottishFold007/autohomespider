import csv
from datetime import datetime

class CsvPipline(object):
    def process_item(self, item, spider):
        columns = item['columns']
        if not columns:
            return item

        settings = spider.settings
        d = datetime.now().strftime("%Y%m%d%H")  #  %Y%m%d%H%M%S
        csvpath = settings['APP_PATH'] + '/data/ret'+ d +'.csv'
        data = [
            columns['username'],  # 用户名
            columns['autohome_id'],
            columns['koubei_id'],
            columns['product_name'],
            columns['score_wg'],  # 外观评分
            columns['score_ssd'],
            columns['score_xjb'],
            columns['prov_name'],
            columns['city_name'],
            columns['buy_date'],
            columns['buy_price'],
            columns['car_oil'],
            columns['car_merit'],
            columns['car_defect']
        ]
        with open(csvpath, 'a+', newline='') as csvfile:
            # pwriter.writerow(['那就这样吧', '哈哈'])
            pwriter = csv.writer(csvfile)
            pwriter.writerow(data)
        return item
