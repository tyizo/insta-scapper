def tool():

    import uuid
    import requests
    from colored import fg

    green = fg(83)
    red = fg(124)
    logo = (green+"""
  _____              _              _____                                       
 |_   _|            | |            / ____|                                      
   | |   _ __   ___ | |_  __ _    | (___    ___  __ _  _ __   _ __    ___  _ __ 
   | |  | '_ \ / __|| __|/ _` |    \___ \  / __|/ _` || '_ \ | '_ \  / _ \| '__|
  _| |_ | | | |\__ \| |_| (_| |    ____) || (__| (_| || |_) || |_) ||  __/| |   
 |_____||_| |_||___/ \__|\__,_|   |_____/  \___|\__,_|| .__/ | .__/  \___||_|   
                                                      | |    | |                
                                                      |_|    |_|               - By Tyizo\r\n""")
    print(logo)
    s = requests.session()
    print(red+'                         Please Login with a fake account!                           ' + '\n')
    uuid = str(uuid.uuid4())
    user = input(green+'[-] Enter username: ')
    password = input(green+'[-] Enter password: ')
    url = "https://i.instagram.com/api/v1/accounts/login/"
    header = {
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTBw==',
        'User-Agent': 'Instagram 35.0.0.20.96 Android (26/8.0.0; 320dpi; 768x1184; unknown/Android; Li0N; vbox86p; vbox86; en_US; 95414347)',
        'Accept-Language': 'en-US',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'i.instagram.com',
        'Connection': 'keep-alive',
        'Accept': '*/*'
    }
    data = {
        'uuid': uuid,
        'username': user,
        'password': password,
        'device_id': uuid,
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_count': '0'
    }
    login = s.post(url, headers=header, data=data)
    res = login.text
    if ('"logged_in_user"') in res: print(green+'[-] Done login', user)
    else:
        print(red+'[-] Error', res)
        exit()

    username = input(green+'[+] Enter username you want: ')
    url2 = (f'https://www.instagram.com/{username}/?__a=1')
    r = s.get(url2)
    the_user = '[+] Username: ' + str(r.json()['graphql']['user']['username'])
    followers = '[+] Followers: ' + str(r.json()['graphql']['user']['edge_followed_by']['count'])
    following = '[+] Following: ' + str(r.json()['graphql']['user']['edge_follow']['count'])
    bio = '[+] Bio: ' + str(r.json()['graphql']['user']['biography'])
    is_private = '[+] Private: ' + str(r.json()['graphql']['user']['is_private'])
    name = '[+] Name: ' + str(r.json()['graphql']['user']['full_name'])
    bio_url = '[+] Bio Url: ' + str(r.json()['graphql']['user']['external_url'])
    id = '[+] Id: ' + str(r.json()['graphql']['user']['id'])
    profile_pic = '[+] Profile Picture: ' + str(r.json()['graphql']['user']['profile_pic_url_hd'])
    highlight_num = '[+] HighLights Number: ' + str(r.json()['graphql']['user']['highlight_reel_count'])
    bus_account = '[+] Business Account: ' + str(r.json()['graphql']['user']['is_business_account'])
    category = '[+] Category: ' + str(r.json()['graphql']['user']['category_name'])
    print(the_user)
    print(followers)
    print(following)
    print(bio)
    print(is_private)
    print(name)
    print(bio_url)
    print(id)
    print(profile_pic)
    print(highlight_num)
    print(bus_account)
    print(category)
    input()
tool()
while True:
    print('\r\n')
    ask = input('Do you wanna reapet y/n: ')
    if ask == 'y' or 'Y' or 'yes' or 'Yes': tool()
    elif ask == 'n' or 'N' or 'No' or 'no': exit()
    else: exit()
    break