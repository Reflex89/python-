#嘉宾名单
jiabin = ['reflex','king','lily','jason']

#打印邀请消息
message = f"{jiabin[0].title()},Can you have dinner with me today?"
print(message)
message = f"{jiabin[1].title()},Can you have dinner with me today?"
print(message)
message = f"{jiabin[2].title()},Can you have dinner with me today?"
print(message)
message = f"{jiabin[3].title()},Can you have dinner with me today?"
print(message)

#打印某位嘉宾无法赴约
message = f"{jiabin[2].title()} can't come to dinner because of something."
print(message)

#修改嘉宾名单
jiabin[2] = 'rox'

#打印新消息
message = f"{jiabin[0].title()},Can you have dinner with me today?"
print(message)
message = f"{jiabin[1].title()},Can you have dinner with me today?"
print(message)
message = f"{jiabin[2].title()},Can you have dinner with me today?"
print(message)
message = f"{jiabin[3].title()},Can you have dinner with me today?"
print(message)


#用len()指出邀请了多少嘉宾
message = f"I invited {len(jiabin)} guests to dinner tonight."
print(message)