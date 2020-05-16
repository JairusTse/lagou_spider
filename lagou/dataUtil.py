# 对数据库进行重复数据删除
import pymongo
from pymongo import MongoClient


# 连接数据库
def connect():
    client = MongoClient()
    db = client['lagou']
    collection = db['lagou_jobs']


def main():
    pass


if __name__ == "__main__":
    main()
