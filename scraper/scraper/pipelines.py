# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
from datetime import datetime


class ScraperPipeline(object):
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.conn = psycopg2.connect(
            database="PC_PARTS", user="pcadmin", password="adminpass", host="127.0.0.1", port="5432")  # TODO check for error
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute('INSERT INTO products(product_id,name,category,price,shop,date) VALUES (%s, %s, %s, %s, %s, %s)',
                          (item['id'], item['name'], item['category'], item['price'], item['shop'], datetime.now()))
        self.conn.commit()
        # print("test")
