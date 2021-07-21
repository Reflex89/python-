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

#打印我找到了一个更大的餐桌
print('I found a bigger table')

#在之前的列表添加三位嘉宾并检查
print(jiabin) 
jiabin.insert(0,'flex')
print(jiabin) 
jiabin.insert(3,'fox')
print(jiabin) 
jiabin.append('tina')
print(jiabin) 

#打印新的邀请信息
message = f"{jiabin[0].title()},Can you have dinner with me today?"
print(message)
message = f"{jiabin[1].title()},Can you have dinner with me today?"
print(message)
message = f"{jiabin[2].title()},Can you have dinner with me today?"
print(message)
message = f"{jiabin[3].title()},Can you have dinner with me today?"
print(message)
message = f"{jiabin[4].title()},Can you have dinner with me today?"
print(message)
message = f"{jiabin[5].title()},Can you have dinner with me today?"
print(message)
message = f"{jiabin[6].title()},Can you have dinner with me today?"
print(message)