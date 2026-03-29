from datetime import datetime
import pytz
Beijing_tz=pytz.timezone("Asia/Shanghai")
now_beijing=datetime.now(Beijing_tz)
print(now_beijing.strftime("%H"))
if 6<int(now_beijing.strftime("%H"))<22:
    print("北京现在是白天")
else:
    print("北京现在是晚上")