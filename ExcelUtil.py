#coding=utf-8
import xlrd
import shutil
import os
import csv
from openpyxl import Workbook

class ExcelUtil:
    def read_excel(self, excel_file, out_path):
        out_file_path = ''
        count = 0
        if(os.path.exists(out_path)):
            shutil.rmtree(out_path)
        os.mkdir(out_path)

        data = xlrd.open_workbook(excel_file)
        print(data.sheet_names)
        table = data.sheets()[0]
        nrows = table.nrows  # 行数
        ncols = table.ncols  # 列数
        print(nrows)
        print(ncols)
        for i in range(0, nrows):
            try:
                row = table.row_values(i)  # 某一行数据
                province = row[4]
                city = row[5]
                if(out_path.endswith('/')):
                    out_file_path = out_path + province;
                else:
                    out_file_path = out_path + "/" + province;
                if(not os.path.exists(out_file_path)):
                    os.mkdir(out_file_path)
                out_file = out_file_path + "/" + city + ".csv";
                out_file_handle = open(out_file, 'a+', encoding='utf-8')
                csv_writer = csv.writer(out_file_handle)
                csv_writer.writerow(row)
                out_file_handle.close()
                count = count + 1
                print('Lines:' + str(count))
            except Exception as err:
                print(err)
                continue


    def split_excel(self, excel_file, out_path):
        if(os.path.exists(out_path)):
            shutil.rmtree(out_path)
        os.mkdir(out_path)

        data = xlrd.open_workbook(excel_file)
        print(data.sheet_names)
        length = len(data.sheets())

        for j in range(0, length) :
            try:
                print(j)
                table = data.sheets()[j]
                wb = Workbook()
                ws = wb.create_sheet("sheet1", index=0)
                for i in range(0, table.nrows):
                    try:
                        ws.append(table.row_values(i))
                    except Exception as ex:
                        print(ex)
                out_file = out_path + "/" + str(j) + ".xls";
                wb.save(out_file)
            except Exception as e:
                print(e)

