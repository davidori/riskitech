
import time<br>
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))<br>
<br>

with open('daily_events.csv') as in_file, open('daily_events_dist.txt', 'w') as out_file:<br>
&nbsp;&nbsp;&nbsp;&nbsp;for line in in_file:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parsed_line = pars_line(line)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out_file.write(parsed_line)<br>
