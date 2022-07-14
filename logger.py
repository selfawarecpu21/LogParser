import json


log_file_path = 'mongod.log'

error_dict = {}


with open(log_file_path, 'r') as file:

    for line in file:
        json2_dict = json.load(line)
        log_id = json2_dict['id']
        log_ctx = json2_dict['ctx']
        if log_id not in error_dict:
            error_dict[log_id] = log_ctx
print(error_dict)

with open('error.log', 'w') as write_file:
    write_file.write(json.dumps(error_dict)) 

