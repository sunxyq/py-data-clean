#coding=utf-8
import csv
import os
import shutil
import DataUtil


class CSVUtil:
    def get_length(self,file):
        csv_reader = csv.reader(open(file, encoding='utf-8'))
        for row in csv_reader:
            return len(row)

    def split_data_by_city(self, file, out_path):
        csv_reader = csv.reader(open(file, encoding='utf-8'))
        out_file_path = ''
        count = 0
        exception = 0
        if(os.path.exists(out_path)):
            shutil.rmtree(out_path)
        os.mkdir(out_path)
        for row in csv_reader:
            try:
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
                exception = exception + 1
                print("Exception " + str(exception) + ":" + str(err))
                continue

    #extract data from csv file and store into database, life service
    def extract_data_from_csv(self, raw_file, out_path):
        csv_reader = csv.reader(open(raw_file, encoding='utf-8'))
        out_file_path = ''
        count = 0
        exception = 0
        if(not os.path.exists(out_path)):
            os.mkdir(out_path)
        for row in csv_reader:
            try:
                if(DataUtil.is_target_shop(row[8])):
                    province = row[2]
                    city = row[3]
                    if(out_path.endswith('/')):
                        out_file_path = out_path + province;
                    else:
                        out_file_path = out_path + "/" + province;
                    if(not os.path.exists(out_file_path)):
                        os.mkdir(out_file_path)
                    out_file = out_file_path + "/" + city + ".csv";
                    out_file_handle = open(out_file, 'a+', encoding='gbk')
                    csv_writer = csv.writer(out_file_handle)

                    row.append(DataUtil.get_shop_type(row[8]))

                    csv_writer.writerow(row)
                    out_file_handle.close()
                    count = count + 1
                    print('Lines:' + str(count))
            except Exception as err:
                exception = exception + 1
                print("Exception " + str(exception) + ":" + str(err))
                continue
        print('Finished')

    def extract_data_from_csv_all(self, raw_file, out_path):
        csv_reader = csv.reader(open(raw_file, encoding='utf-8'))
        out_file_path = ''
        count = 0
        exception = 0
        if(not os.path.exists(out_path)):
            os.mkdir(out_path)
        #os.mkdir(out_path)
        for row in csv_reader:
            try:
                province = row[2]
                city = row[3]
                if(out_path.endswith('/')):
                    out_file_path = out_path + province;
                else:
                    out_file_path = out_path + "/" + province;
                if(not os.path.exists(out_file_path)):
                    os.mkdir(out_file_path)
                out_file = out_file_path + "/" + city + ".csv";
                out_file_handle = open(out_file, 'a+', encoding='gbk')
                csv_writer = csv.writer(out_file_handle)

                row.append(DataUtil.get_shop_type(row[8]))

                csv_writer.writerow(row)
                out_file_handle.close()
                count = count + 1
                print('Lines:' + str(count))
            except Exception as err:
                exception = exception + 1
                print("Exception " + str(exception) + ":" + str(err))
                continue
        print('Finished')

    def extract_data_from_takeout_csv(self, raw_file, out_path):
        csv_reader = csv.reader(open(raw_file, encoding='utf-8'))
        out_file_path = ''
        count = 0
        exception = 0
        if(not os.path.exists(out_path)):
            os.mkdir(out_path)
        for row in csv_reader:
            try:
                province = row[3]
                city = row[4]
                if(out_path.endswith('/')):
                    out_file_path = out_path + province;
                else:
                    out_file_path = out_path + "/" + province;
                if(not os.path.exists(out_file_path)):
                    os.mkdir(out_file_path)
                out_file = out_file_path + "/" + city + ".csv";
                out_file_handle = open(out_file, 'a+', encoding='gbk')
                csv_writer = csv.writer(out_file_handle)

                csv_writer.writerow(row)
                out_file_handle.close()
                count = count + 1
                print('Lines:' + str(count))

            except Exception as err:
                exception = exception + 1
                print("Exception " + str(exception) + ":" + str(err))
                continue
        print('Finished')