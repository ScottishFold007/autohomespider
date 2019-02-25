# -*- coding: utf-8 -*-

# Scrapy settings for praise project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'praise'

SPIDER_MODULES = ['praise.spiders']
NEWSPIDER_MODULE = 'praise.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'praise (+http://www.yourdomain.com)'
USER_AGENT = 'iPhone	12.1.2	autohome	9.8.5	iPhone'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
   'Host': 'koubei.app.autohome.com.cn',
   'apisign': '1|63c4fc1d743f22ff44f53389e59db4b49e107082|autohomebrush|1547461957|795B800B7A6E2FF3840BAEE07BA65FE4',
   'Cookie': 'area=110101; app_cityid=110100; app_provinceid=110000; app_devicename=iPhone; app_key=auto_iphone; app_platform=iPhone; app_sign=0053A6CC63C90E69C09EBBAB195A00CB; app_sysver=12.1.2; app_userid=0; app_ver=9.8.5; device_standard=iPhone11,6; pcpopclub=;',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'praise.middlewares.PraiseSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'praise.middlewares.PraiseDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
   'scrapy.extensions.telnet.TelnetConsole': 300,
   'scrapy.extensions.memusage.MemoryUsage': 300,
}
TELNETCONSOLE_ENABLED = True
# Memory  MB
MEMUSAGE_ENABLED = True
MEMUSAGE_WARNING_MB = 800
MEMUSAGE_LIMIT_MB = 2048
MEMUSAGE_NOTIFY_MAIL = 'lsg9012@qq.com'

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#   'praise.pipelines.PraisePipeline': 300,
   'praise.csvpipline.CsvPipline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 90
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 数据路径
APP_PATH = '/Volumes/Bdisk/www/pyproject/praise' # 'D:/htdocs/pyproject/praise'
LOG_FILE = APP_PATH + '/log/logs.log'
# default set  DEBUG
LOG_LEVEL = 'INFO'