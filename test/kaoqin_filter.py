# coding: utf-8
import datetime

import xlrd
import xlwt


def check(begin, end):
    if begin.hour >= 10:
        return False
    if begin.hour >= 9 and begin.minute > 5:
        return False
    if end.hour < 18:
        return False
    return True


myWorkbook = xlrd.open_workbook('kaoqin.xls')
sheets = myWorkbook.sheets()
sheet = sheets[0]
rows = sheet.nrows
cols = sheet.ncols
temp_name = sheet.row_values(1)[1]
temp_time_min = datetime.datetime.strptime(str(sheet.row_values(1)[3]).replace('/', '-'), "%Y-%m-%d %H:%M:%S")
temp_time_max = None

myWorkbook = xlwt.Workbook()
mySheet = myWorkbook.add_sheet('result')
myStyle = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
mySheet.write(0, 0, '姓名', myStyle)
mySheet.write(0, 1, '当天第一次打卡时间', myStyle)
mySheet.write(0, 2, '当天最后一次打卡时间', myStyle)
mySheet.write(0, 3, '上班时间', myStyle)
mySheet.write(0, 4, '下班时间', myStyle)
mySheet.write(0, 5, '统计结果', myStyle)
mySheet.write(0, 6, '星期', myStyle)
week = ['一', '二', '三', '四', '五', '六', '日']
j = 1
for i in range(2, rows):
    row = sheet.row_values(i)
    clock_time = datetime.datetime.strptime(row[3].replace('/', '-'), "%Y-%m-%d %H:%M:%S")
    if row[1] == temp_name and clock_time.day == temp_time_min.day:
        temp_time_max = clock_time
    else:
        begin, end = temp_time_min, temp_time_max
        result = check(begin, end)
        print('%s | %s | %s (%s -- %s)  ' % (temp_name, temp_time_min, temp_time_max, begin, end))
        mySheet.write(j, 0, temp_name)
        mySheet.write(j, 1, temp_time_min.strftime("%Y-%m-%d %H:%M:%S"))
        mySheet.write(j, 2, temp_time_max.strftime("%Y-%m-%d %H:%M:%S"))
        mySheet.write(j, 3, begin.strftime("%Y-%m-%d %H:%M:%S"))
        mySheet.write(j, 4, end.strftime("%Y-%m-%d %H:%M:%S"))
        mySheet.write(j, 6, "星期" + week[int(end.strftime("%w")) - 1])
        if result:
            mySheet.write(j, 5, result)
        else:
            mySheet.write(j, 5, result, myStyle)
        j += 1
        temp_name = sheet.row_values(i)[1]
        temp_time_min = datetime.datetime.strptime(sheet.row_values(i)[3].replace('/', '-'), "%Y-%m-%d %H:%M:%S")

result = check(begin, end)
print('%s | %s | %s (%s -- %s) | %s ' % (temp_name, temp_time_min, temp_time_max, begin, end, result))
mySheet.write(j, 0, temp_name)
mySheet.write(j, 1, temp_time_min)
mySheet.write(j, 2, temp_time_max)
mySheet.write(j, 3, begin)
mySheet.write(j, 4, end)
mySheet.write(j, 6, "星期" + week[int(end.strftime("%w")) - 1])
# mySheet.write(j, 5, result)
mySheet.col(0).width = 256 * 15
mySheet.col(1).width = 256 * 35
mySheet.col(2).width = 256 * 35
mySheet.col(3).width = 256 * 15
mySheet.col(4).width = 256 * 15
mySheet.col(5).width = 256 * 10
myWorkbook.save('excelFile.xls')
