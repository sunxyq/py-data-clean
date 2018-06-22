#coding=utf-8
import csv
import pymysql
import DataUtil
import xlrd


class DBUtil:

    def __init__(self):
        print('init DBUtil')

    def query_mysql(self):
        # 打开数据库连接
        db = pymysql.connect("10.188.40.12", "udata", "123456", "udata_privilege", charset="utf8")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句
        sql = "SELECT * FROM account"
        try:
            print('hello')
            # 执行SQL语句
            cursor.execute(sql)

            # 获取所有记录列表
            results = cursor.fetchall()
            print(results.count)
            for row in results:
                fname = row[0]
                lname = row[1]
                age = row[2]
                sex = row[3]
                income = row[4]
                # 打印结果
                print("id=%s,uid=%s,uname=%s,status=%s,operator=%s" % \
                      (fname, lname, age, sex, income))
        except Exception as err:
            print(err)
        finally:
            db.close()

    def read_csv_to_db(self, csv_file_path):
        csv_reader = csv.reader(open(csv_file_path, encoding='utf-8'))
        # 打开数据库连接
        db = pymysql.connect("10.188.40.12", "udata", "123456", "udata_business", charset="utf8")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句
        sql = " insert into life_service_0502(shop_id, shop_name, province, city, district, address, lat, lon," \
              "classification, phone, business_hours, type, branch_code) " \
              "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        try:
            list = []
            i = 0
            for row in csv_reader:
                shop_type = DataUtil.get_shop_type(row[8])

                data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], shop_type, 0 )
                list.append(data)
                if len(list) > 5000:
                    cursor.executemany(sql, list)
                    db.commit()
                    list.clear()
                    i = i + 1
                    print(i * 5000)
            cursor.executemany(sql, list)
            db.commit()
        except Exception as err:
            print(err)
            db.rollback()
        finally:
            # 关闭数据库连接
            cursor.close()
            db.close()

    def read_xlsx_to_db(self, xlsx_file_path):
        # 打开数据库连接
        db = pymysql.connect("10.188.40.12", "udata", "123456", "udata_business", charset="utf8")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句
        sql_fence = " insert into digit_fence(branch_code, branch_type, lon, lat)" \
              " VALUES (%s,%s,%s,%s) "
        sql_branch = " insert into branch(branch_code, branch_name, branch_type, branch_superior, superior_name, superior_type, area_code, area_name," \
              "region_code, region_name, effect_time, account_no, city_code,province,city,city_level) " \
              "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "

        try:
            data = xlrd.open_workbook(xlsx_file_path)
            sheets = len(data.sheets())
            print(sheets)
            for sheet in range(0, sheets) :
                sql = sql_fence
                if (sheet % 2 == 0) :
                    print(sheet)
                    sql = sql_branch
                table = data.sheets()[sheet]
                nrows = table.nrows  # 行数
                print(nrows)
                for i in range(0, nrows):
                    row = table.row_values(i)  # 某一行数据
                    print(row)
                    cursor.execute(sql, row)
                    print(i)
                db.commit()
                print('Done ' + str(sheet))
        except Exception as err:
            print(err)
            db.rollback()
        finally:
            cursor.close()
            db.close()

    def read_takeout_csv_to_db(self, csv_file_path):
        csv_reader = csv.reader(open(csv_file_path, encoding='utf-8'))
        # 打开数据库连接
        db = pymysql.connect("10.188.40.12", "udata", "123456", "udata_business", charset="utf8")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句
        sql = " insert into takeout_shop_0510(shop_id, shop_name, classification,province, city, address, lon_lat, business_hours,sales, is_brand," \
              "avg_deliver_time, begin_price, deliver_fee, deliver_service, company,remark) " \
              " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        try:
            list = []
            i = 0
            j = 0
            for row in csv_reader:
                list.append(row)

                if len(list) > 5000:
                    cursor.executemany(sql, list)
                    db.commit()
                    list.clear()
                    i = i + 1
                    print(i * 5000)
            cursor.executemany(sql, list)
            db.commit()
        except Exception as err:
            print(err)
            db.rollback()
        finally:
            # 关闭数据库连接
            cursor.close()
            db.close()

    def digit_fence(self):

        db = pymysql.connect("10.188.40.12", "udata", "123456", "udata_business", charset="utf8")
         # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        sql = "select * from digit_fence"
        dict = {}

        try:
            # 执行SQL语句
            cursor.execute(sql)

            # 获取所有记录列表
            results = cursor.fetchall()
            print("the length of records in digit_fence:" + str(len(results)))
            for row in results:
                if row[0] in dict:
                    dict[row[0]].append(row)
                else:
                    dict[row[0]] = [row]

            print("the length of dict is:" + str(len(dict)))
            sql = "SELECT * FROM life_service_0502_bsgsh_3type"

            # 执行SQL语句
            cursor.execute(sql)

            # 获取所有记录列表
            results = cursor.fetchall()
            print("the length of records in life_service_0502_bsgsh_3type:" + str(len(results)))
            for row in results:
                lat = row[7]
                lon = row[8]
                for key in dict:
                    try:
                        if DataUtil.is_in_fence(lon, lat, dict[key]) :
                            code = dict[key][0][0];
                            name = dict[key][0][1];
                            if( code is None):
                                continue
                            if (name is None):
                                continue
                            sql = "update life_service_0502_bsgsh_3type set branch_code='" + code + "', branch_name='" + name + "' where id=" + str(row[0]);
                            print(sql)
                            cursor.execute(sql)
                            db.commit()
                            break
                    except Exception as err:
                        print("Error in circle:" + str(err))
        except Exception as err:
            print(err)
        finally:
            db.close()
