#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# File  : mysqlite3.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2019/6/7

import sqlite3

class sql_con:
    def __init__(self, sqlpath):
        self.conn = sqlite3.connect(sqlpath)
        self.cur = self.conn.cursor()

    def dosql(self, sqlcode):
        """
        执行sql语句
        :param sqlcode: sql语句代码
        :return:
        """
        self.cur.execute(sqlcode)

    def close(self):
        """
        关闭数据库和游标
        :return:
        """
        self.cur.close()
        self.conn.close()

    def run(self):
        """
        执行sql语句并更新数据表
        :return:
        """
        self.results = self.cur.fetchall()  # 执行语句
        self.conn.commit()  # 更新数据库
        return self.results

    def newtb(self, tablename, *args):
        """

        :param tablename: 表名
        :param args: 表内不定长字段名
        :return:
        """
        vaules = ["%s varchar" % i for i in args]
        vaules = ",".join(vaules)
        sqlcode = "create table if not exists {}({})".format(tablename, vaules)
        self.dosql(sqlcode)

    def add(self, tablename, **kwargs):
        """

        :param tablename: 表名
        :param kwargs: 新增内容字典
        :return:
        """
        values1 = ["%s" % i for i in kwargs.keys()]
        values1 = ",".join(values1)
        values2 = ["%s" % i for i in kwargs.values()]
        values2 = ",".join(values2)
        values3 = ["%s='%s'" % (i, kwargs[i]) for i in kwargs.keys()]
        values3 = " and ".join(values3)
        sqlcode = "insert into {}({}) select {} where not exists(select * from {} where {})".format(
            tablename, values1, values2, tablename, values3)
        print(sqlcode)
        self.dosql(sqlcode)

    def update(self, tablename, origindict, **kwargs):
        """

        :param tablename: 表名
        :param origindict: 条件字典
        :param kwargs: 待更新内容
        :return:
        """
        values1 = ["%s=%s" % (i, origindict[i]) for i in origindict.keys()]
        values1 = " and ".join(values1)
        values2 = ["%s=%s" % (i, kwargs[i]) for i in kwargs.keys()]
        values2 = ",".join(values2)
        sqlcode = "update {} set {} where {}".format(
            tablename, values2, values1)
        print(sqlcode)
        self.dosql(sqlcode)

    def delete(self, tablename, **kwargs):
        """

        :param tablename: 表名
        :param kwargs: 不定长条件字典参数
        :return:
        """
        values1 = ["%s=%s" % (i, kwargs[i]) for i in kwargs.keys()]
        values1 = " and ".join(values1)
        sqlcode = "delete from {} where {}".format(tablename, values1)
        print(sqlcode)
        self.dosql(sqlcode)

    def seach(self, tablename, origindict, *args):
        """
        :param tablename: 表名
        :param origindict: 条件字典
        :param args: 待查询参数，可以是*
        :return:
        """
        values1 = ",".join(args)
        values2 = ["%s='%s'" % (i, origindict[i]) for i in origindict.keys()]
        values2 = " and ".join(values2)
        sqlcode = "select {} from {} where {}".format(
            values1, tablename, values2)
        print(sqlcode)
        self.dosql(sqlcode)


def demo():
    s = sql_con('student.db')  # 连接一个student.db数据库文件，没有则会自动创建
    s.newtb("settings", "ip", "port")  # 新建一个表，两个字段ip,port
    # 向settings表里添加，字段ip值为123,字段port值为5694
    s.add("settings", ip=123, port=5694)
    s.run()  # 执行上条语句并更新数据库
    # 向settings表里添加，字段ip值为123456,字段port值为3564
    s.add("settings", ip=123456, port=3564)
    s.run()  # 执行上条语句并更新数据库
    s.seach("settings", {"ip": 123}, "*")  # 查询settings表里，字段ip值为123的所有项
    res = s.run()  # 执行上条语句并更新数据库
    for i in res:
        print(i)  # 打印查询结果
    # 更新settings表，将原始字段ip值为123的所有项的字段ip设置为456,字段port设置为8956
    s.update("settings", {"ip": 123}, ip=456, port=8956)
    s.run()  # 执行上条语句并更新数据库
    # 删除settings里，字段ip=456,port=8956的所有项
    s.delete("settings", ip=456, port=8956)
    s.run()  # 执行上条语句并更新数据库
    s.close()  # 操作完毕后断开数据库连接


if __name__ == '__main__':
    demo()
