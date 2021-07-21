current_users = ['admin','reflex','king','yingzi','losters']
current_users_lower = [current_user.lower() for current_user in current_users]
new_users = ['wAng','reFlexyz','aDmin','Flex','kiNg']

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"用户名 {new_user} 重复,请输入其他的用户名!")
    else:
        print(f"恭喜你, {new_user} 未被使用!")
