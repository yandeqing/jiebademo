#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
import re
from collections import Counter

import wordcloud, jieba
import jieba.analyse


class WordCounter(object):

    def get_content_from_file(self, file):
        with codecs.open(file, 'r', 'utf-8') as f:
            content = f.read()
            content = re.sub(r'\s+', r' ', content)
            content = re.sub(r'\.+', r' ', content)
            content = re.sub("[A-Za-z0-9!%\[\],。]", "", content)
            return content

    def count_from_str(self, content, top_limit=0):
        if top_limit <= 0:
            top_limit = 100
        jieba.load_userdict("userdict.txt")
        tags = jieba.analyse.extract_tags(content, topK=100)
        words = jieba.cut(content)
        counter = Counter()
        for word in words:
            if word in tags:
                counter[word] += 1

        return counter.most_common(top_limit)


if __name__ == '__main__':
    counter = WordCounter()
    content = counter.get_content_from_file(r'data.txt')
    result = counter.count_from_str(content, top_limit=10)
    for k, v in result:
        print(k, v)

    txt = " ".join(jieba.lcut(content))
    w = wordcloud.WordCloud(width=1280, font_path="msyh.ttc",font_step=2,height=720)
    w.generate(txt)
    w.to_file("wordcloud.png")
    os.system('wordcloud.png')