from datetime import datetime
import pytz
beijing_tz=pytz.timezone('Asia/Shanghai')
chicago_tz=pytz.timezone('America/Chicago')
now_beijing=datetime.now(beijing_tz)
now_chicago=datetime.now(chicago_tz)
diff = (now_beijing.utcoffset().total_seconds() - now_chicago.utcoffset().total_seconds()) / 3600
print(f"北京时间：{now_beijing.strftime("%Y-%m-%d %H:%M")}")
print(f"美国中部时间：{now_chicago.strftime("%Y-%m-%d %H:%M")}")
print(f"你比北京时间要晚{int(diff)}小时")