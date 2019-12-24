import time
# stage 1
def csv_to_dict(path_to_file):
    dicts_list = list()
    with open(path_to_file) as in_file:
        headers = in_file.readline().replace('\n','').split(',')
        while True:
            line = in_file.readline()
            if not line:
                print("here")
                break;
            line = line.replace('\n','').split(',')
            print(line)
            line_dict = dict()
            for i in range(len(headers)):
                line_dict[headers[i]] = line[i]
            dicts_list.append(line_dict)
            print(dicts_list)
        return dicts_list

# print(csv_to_dict('session2/working_with_files/ex2_simple_csv_parser/daily_events.csv'))

# stage 2 + 3

def csv_to_dict2(path_to_file):
    dicts_list = list()
    with open(path_to_file) as in_file:
        headers = in_file.readline().replace('\n','').split(',')
        while True:
            line = in_file.readline()
            if not line:
                break;
            line = line.replace('\n','').split(',')
            line_dict = dict()
            for i in range(len(headers)):
                if headers[i] == 'timestamp':
                    line_dict[headers[i]] = convert_timestamp(int(line[i]))
                else:    
                    line_dict[headers[i]] = line[i]
            dicts_list.append(line_dict)
        return dicts_list

def convert_timestamp(timestamp_str):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp_str))

# print(csv_to_dict2('session2/working_with_files/ex2_simple_csv_parser/daily_events.csv'))

# stage 4

def csv_to_dict_file(path_to_csv,path_to_outfile):
    dicts_list = csv_to_dict2(path_to_csv)
    with open(path_to_outfile, 'w') as out_file:
        for item in dicts_list:
            out_file.write(f'{item}\n')

csv_to_dict_file('session2/working_with_files/ex2_simple_csv_parser/daily_events.csv','session2/working_with_files/ex2_simple_csv_parser/daily_events_dict.txt')