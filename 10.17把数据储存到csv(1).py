import csv
csvFile = open('test.csv', 'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'numberS', 'numberS Plus'))
    for i in range(10):
        i = str(i)
        writer.writerow((i, i + 's', i + 's Plus'))
finally:
    csvFile.close()
