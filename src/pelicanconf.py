#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import markdown
AUTHOR = u'Rocky Lai'
ABOUT_PAGE_NAME = AUTHOR.replace(" ", "-").lower()
SITENAME = u"心亡则忙，亡心则忘"

#
# 开启测试环境
#

#IN_TEST_Environment = True
IN_TEST_Environment = False

#
# 通用
#
DISQUS_SITENAME = "wudixiaopgithubio"
SITEURL = 'http://blog.shuiguzi.com'
THEME = "Theme/CLEANBLOG"
WEB_SITE_DOMAIN = "http://blog.shuigui.com"
DEFAULT_PAGINATION = 8

if IN_TEST_Environment:
    SITEURL = "http://localhost:8000"
    WEB_SITE_DOMAIN = "http://localhost:8000"

PATH = 'content'
TIMEZONE = 'Asia/Chongqing'
DEFAULT_LANG = u'zhcn'

# 根据上面的DEFALUT_LANG来匹配日期格式
DATE_FORMATS = {
    'en-us': '%Y-%m-%d %H:%M',
    'zhcn': '%Y-%m-%d %H:%M',
}

#
# 个人信息等等
#
about_me_markdown = open('aboutme.md', 'r').read().decode('utf-8')

ABOUT_ME = markdown.markdown(about_me_markdown, extension=["markdown.extensions.extra"])

COPYRIGHTMARK = "Rocky Lai @ 2014 - 2015"

#
# CLEAN-BLOG THEME SETTINGS
#
COLOR_SCHEME_CSS = "github.css"
GITHUB_LINK_DISPLAY_NAME = "Rocky Lai @ Github"
GITHUB_URL = 'https://github.com/wudixiaop'
DISPLAY_CATEGORIES_ON_MENU = True
SUMMARY_MAX_LENGTH = 4

# FEED_DOMAIN = WEB_SITE_DOMAIN
# FEED_RSS = "feed/rocky-lai.rss.xml"
