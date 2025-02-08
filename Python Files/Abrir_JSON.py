import json
import csv

headers = ["DatabaseName", "SourceAgentType",
           "AgentsProcessed", "ExecutionTime"]

with open('report.json', 'r') as new_report:
    dict_NewReport = json.load(new_report)
with open('report-baseline.json', 'r') as base_line:
    dict_BaseLine = json.load(base_line)

result = list(map(dict_NewReport.get, (tuple(headers))))
print(result)


for head_1 in headers:
    # Value = dict_NewReport[head_1]
    print(head_1)
    dict_NewReport_2 = dict.fromkeys(headers, headers)
print(dict_NewReport_2)

# print()
# headers_1 = dict_NewReport[head_1]
# headers_2 = dict_BaseLine[head_1]


# for headers,value in dict_NewReport.items():

# print(f"{headers}")


# print(dict_NewReport)
# print(headers_1)
# print(headers_2)
