#coding=utf-8
import DBUtil
def main() :
    util = DBUtil.DBUtil()
    DBUtil.DBUtil.digit_fence(util)
    # print(FileUtil.count_lines('/Users/xiangyongqing/Documents/crawler-data-1797910-1522984840544.csv'))
    # print(CSVUtil.CSVUtil.get_length(CSVUtil, '/Users/xiangyongqing/Documents/crawler-data-1797910-1522984840544.csv'))
    # CSVUtil.CSVUtil.split_data_by_city(CSVUtil, '/Users/xiangyongqing/Documents/crawler-data-1797909-1523092432926.csv',
    # '/Users/xiangyongqing/Documents/output2')

    #CSVUtil.CSVUtil.extract_data_from_csv_all(Constant, Constant.LIFE_SERVICE, Constant.OUT_PATH)
    #CSVUtil.CSVUtil.extract_data_from_csv_all(Constant, Constant.RESTAURANT, Constant.OUT_PATH)
    #CSVUtil.CSVUtil.extract_data_from_csv_all(Constant, Constant.SHOPPING, Constant.OUT_PATH)


    # DBUtil.DBUtil.read_csv_to_db(DBUtil, Constant.LIFE_SERVICE_ONLINE)
    # DBUtil.DBUtil.read_csv_to_db(DBUtil, Constant.RESTAURANT_ONLINE)
    # DBUtil.DBUtil.read_csv_to_db(DBUtil, Constant.SHOPPING_ONLINE)

    #CSVUtil.CSVUtil.extract_data_from_takeout_csv(DBUtil, Constant.TAKEOUT_SHOP, Constant.TAKEOUT_OUT_PATH)
    #DBUtil.DBUtil.read_takeout_csv_to_db(DBUtil, Constant.TAKEOUT_SHOP)

    #DBUtil.DBUtil.read_xlsx_to_db(DBUtil, Constant.DIGIT_FENCE)


    #extract data for jiaming
    # file_path = "/Users/xiangyongqing/Desktop/meituan_data.xls"
    # out_path = "/Users/xiangyongqing/Desktop/out"
    # ExcelUtil.ExcelUtil.split_excel(ExcelUtil, file_path, out_path)

if(__name__== '__main__') :
    print(__name__)
    main()


