# coding: utf-8
import xlrd
import xlwt


def check(begin, end):
    begin_hour = int(begin[:begin.find(':')])
    begin_min = int(begin[begin.find(':') + 1:begin.find(':') + 3])
    if (begin_hour >= 9 or begin_hour >= 1) and begin_min > 5:
        return False
    end_hour = int(end[:1])
    if end_hour < 6:
        return False
    return True


myWorkbook = xlrd.open_workbook('kaoqin.xls')
sheets = myWorkbook.sheets()
sheet = sheets[0]
rows = sheet.nrows
cols = sheet.ncols
temp_name = sheet.row_values(1)[1]
temp_time_min = sheet.row_values(1)[3]
temp_time_max = None

myWorkbook = xlwt.Workbook()
mySheet = myWorkbook.add_sheet('result')
myStyle = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
mySheet.write(0, 0, '姓名', myStyle)
mySheet.write(0, 1, '第一次打卡时间', myStyle)
mySheet.write(0, 2, '最后一次打卡时间', myStyle)
mySheet.write(0, 3, '上班时间', myStyle)
mySheet.write(0, 4, '下班时间', myStyle)
mySheet.write(0, 5, '统计结果', myStyle)
j = 1
for i in range(2, rows):
    row = sheet.row_values(i)
    if row[1] == temp_name and \
            str(row[3])[:str(row[3]).find('星')] == str(temp_time_min)[:str(temp_time_min).find('星')]:
        temp_time_max = sheet.row_values(i)[3]
    else:
        begin = temp_time_min[temp_time_min.find('午') + 1:].strip()
        end = temp_time_max[temp_time_max.find('午') + 1:].strip()
        result = check(begin, end)
        print('%s | %s | %s (%s -- %s) | %s ' % (temp_name, temp_time_min, temp_time_max, begin, end, result))
        mySheet.write(j, 0, temp_name)
        mySheet.write(j, 1, temp_time_min)
        mySheet.write(j, 2, temp_time_max)
        mySheet.write(j, 3, begin)
        mySheet.write(j, 4, end)
        if result:
            mySheet.write(j, 5, result)
        else:
            mySheet.write(j, 5, result, myStyle)
        j += 1
        temp_name = sheet.row_values(i)[1]
        temp_time_min = sheet.row_values(i)[3]

result = check(begin, end)
print('%s | %s | %s (%s -- %s) | %s ' % (temp_name, temp_time_min, temp_time_max, begin, end, result))
mySheet.write(j, 0, temp_name)
mySheet.write(j, 1, temp_time_min)
mySheet.write(j, 2, temp_time_max)
mySheet.write(j, 3, begin)
mySheet.write(j, 4, end)
mySheet.write(j, 5, result)
mySheet.col(1).width = 256 * 30
mySheet.col(2).width = 256 * 30
myWorkbook.save('excelFile.xls')
