import time
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))

with open('daily_events.csv') as in_file, open('daily_events_dist.txt', 'w') as out_file:
    for line in in_file:
        parsed_line = pars_line(line)
        out_file.write(parsed_line)
