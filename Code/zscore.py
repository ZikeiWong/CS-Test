import xlrd as xl
import csv
from collections import Counter
wb = xl.open_workbook('pnas.xlsx')
ws = wb.sheet_by_index(0)
scores = ws.col_values(5)
scores.pop(0)

score_counter = Counter()
for score in scores:
    score_counter.update(score)
print(score_counter)

# temp = list(set(scores))
# temp.sort(key=scores.index)
# scores = temp
# scores.pop(-1)


# SDs = []
# temp = scores[0]
# for score in scores[1:]:
#     SDs.append(temp-score)
#     print(temp-score)
#     temp = score

# print(SDs)
# f = open('SDs.csv', 'w')
# writer = csv.writer(f)
# for i in range(len(SDs)):
#     writer.writerow(SDs[i])



