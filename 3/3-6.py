#嘉宾名单
guests = ['reflex','king','lily','jason']

#打印邀请消息
message = f"{guests[0].title()},Can you have dinner with me today?"
print(message)
message = f"{guests[1].title()},Can you have dinner with me today?"
print(message)
message = f"{guests[2].title()},Can you have dinner with me today?"
print(message)
message = f"{guests[3].title()},Can you have dinner with me today?"
print(message)

#打印某位嘉宾无法赴约
message = f"{guests[2].title()} can't come to dinner because of something."
print(message)

#修改嘉宾名单
guests[2] = 'rox'

#打印新消息
message = f"{guests[0].title()},Can you have dinner with me today?"
print(message)
message = f"{guests[1].title()},Can you have dinner with me today?"
print(message)
message = f"{guests[2].title()},Can you have dinner with me today?"
print(message)
message = f"{guests[3].title()},Can you have dinner with me today?"
print(message)

#打印我找到了一个更大的餐桌
print('I found a bigger table')

#在之前的列表添加三位嘉宾并检查
print(guests) 
guests.insert(0,'flex')
print(guests) 
guests.insert(3,'fox')
print(guests) 
guests.append('tina')
print(guests) 

#打印新的邀请信息
message = f"{guests[0].title()},Can you have dinner with me today?"
print(message)
message = f"{guests[1].title()},Can you have dinner with me today?"
print(message)
message = f"{guests[2].title()},Can you have dinner with me today?"
print(message)
message = f"{guests[3].title()},Can you have dinner with me today?"
print(message)
message = f"{guests[4].title()},Can you have dinner with me today?"
print(message)
message = f"{guests[5].title()},Can you have dinner with me today?"
print(message)
message = f"{guests[6].title()},Can you have dinner with me today?"
print(message)

#打印新买的餐桌无法及时送达
print("Sorry, the new table can't be delivered, so we can only invite two guests.")

#缩减名单并逐个致歉
popped_1 = guests.pop(6)
message = f"I'm sorry {popped_1.title()}, I can't invite you to dinner."
print(message)
popped_2 = guests.pop(5)
message = f"I'm sorry {popped_2.title()}, I can't invite you to dinner."
print(message)
popped_3 = guests.pop(4)
message = f"I'm sorry {popped_3.title()}, I can't invite you to dinner."
print(message)
popped_4 = guests.pop(3)
message = f"I'm sorry {popped_4.title()}, I can't invite you to dinner."
print(message)
popped_5 = guests.pop(2)
message = f"I'm sorry {popped_5.title()}, I can't invite you to dinner."
print(message)

#再次邀请剩余再邀请名单的嘉宾
message = f"Hello,{guests[0].title()}! You are still on the list of invitees. Welcome to dinner tonight."
print(message)
message = f"Hello,{guests[1].title()}! You are still on the list of invitees. Welcome to dinner tonight."
print(message)

#用del删除剩余嘉宾并检查名单是否为空
del guests[0]
del guests[0]
print(guests)