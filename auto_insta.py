from instabot import Bot


bt=Bot()
bt.login(username="your username",password="your passworld")


bt.follow('enter a username you want to follow')

bt.upload_photo('enter a path of photo you want to upload',caption="add caption")
bt.unfollow("usrname")

bt.send_message('i llove python',["list of accounts"])
followers=bt.get_user_followers('username')

for i in followers:
    print(bt.get_user_info(followers))

following=bt.get_user_following("username")
for i in following:
    priint(bt.get_user_info(following))
