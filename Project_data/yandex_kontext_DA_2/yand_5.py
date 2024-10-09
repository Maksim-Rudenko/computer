import pandas as pd
import json

sum_value = 0
workers_value = dict()

df = pd.read_json(path_or_buf='logs.jsonl', lines=True)
test = df.values.tolist()

for i in range(len(test)):
    test[i]['diff_hours'] = (test[i]['end_ts'] - test[i]['start_ts']) // 3600
    test[i]['skill_value_new'] = (test[i]['skill_value'] - 50) * 0.4 + 40
    if test[i]['status'] == 'APPROVED':
        sum_value += test[i]['skill_value_new'] * test[i]['diff_hours']    
        workers_value[test[i]['worker_id']] = test[i]['skill_value_new'] * test[i]['diff_hours']
    else:
        workers_value[test[i]['worker_id']] = 0


'''for i in range(len(test)):
    print(test[i]['diff_hours'], test[i]['skill_value_new'], test[i]['status'])'''

max_val = max(workers_value.values())
final_dict = {worker:value for worker, value in workers_value.items() if value == max_val}
print(sum_value)
for key, value in final_dict.items():
    print(key, value)