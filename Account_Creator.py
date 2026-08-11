from random import choice 
from threading import Thread , Lock
import requests , os

BIO = 'Mr Joker Here @221298'


FIRST_NAMES = [
    'محمد','أحمد','عبدالله','عبدالرحمن','عبدالعزيز','عبدالملك','عبدالله','خالد','سعود','فهد',
    'سلطان','ناصر','فيصل','تركي','مشعل','بندر','ماجد','وليد','ياسر','عمر',
    'علي','حسن','حسين','يوسف','إبراهيم','إسماعيل','عثمان','طارق','سامي','راشد',
    'حمد','جاسم','أنور','منصور','صالح','سليمان','زكي','نواف','مشاري','عادل',
    'كريم','باسم','رامي','هاني','فارس','زياد','مروان','أنس','بلال','أمين',
    'رائد','نبيل','جمال','شريف','هشام','ماهر','عصام','معتز','إياد','وسام',
    'لؤي','قصي','همام','غسان','فادي','سامر','نادر','طلال','علاء','رياض',
    'قاسم','سفيان','ياسين','أيوب','حمزة','زكريا','إلياس','نوح','آدم','مالك',
    'سيف','فراس','حسام','مؤيد','معاذ','أسامة','أيمن','بشار','ثامر','جهاد',
    'حيدر','داود','ذياب','رعد','زهير','سعد','شادي','صابر','ضياء','ظافر',
    'عباس','غازي','فواز','قتيبة','كامل','لطفي','محيي','نزار','هيثم','يزيد',
    'أكرم','بدر','تيم','جابر','حازم','خليل','رائد','زهدي','ساجد','شجاع',
    'صبري','طاهر','عامر','عبدالكريم','عبدالهادي','عبدالناصر','عبدالوهاب','عدنان','عز الدين','عماد',
    'غالب','فؤاد','قيس','لبيب','مجد','منير','نسيم','هلال','وائل','يحيى',
    'أوس','براء','تامر','جابر','حسان','خضر','راني','زاهر','سهيل','شكري',]
LAST_NAMES = [
    'العتيبي','القحطاني','الدوسري','الشمري','الحربي','المطيري','العنزي','الزهراني','الغامدي','الشهري',
    'السبيعي','البقمي','الجعيد','الجهني','الرشيدي','الصاعدي','العمري','الفايز','القرني','المالكي',
    'النعيمي','الهذلي','اليامي','الثقفي','الحارثي','الخالدي','الدغيم','الراشد','الزيد','السالم',
    'الشريف','الصالح','الطائي','العبدلي','الفهد','الكناني','اللهيبي','المحيميد','الناصري','الهاشمي',
    'الوهيبي','اليوسف','آل سعود','آل نهيان','آل مكتوم','الكواري','المهندي','الجابر','الخليفي','المري',
    'الأنصاري','البلوشي','الجسمي','الحمادي','الخوري','الدرعي','الراشدي','الزيودي','السويدي','الشامسي',
    'الظاهري','العبيدلي','الفلاسي','الكتبي','المنصوري','النقبي','الهنائي','اليماحي','البوسعيدي','الحارثي',
    'الخروصي','السيابي','الشقصي','العامري','الفارسي','الكندي','المقبالي','النبهاني','الهنائي','اليافعي',
    'الحسيني','العلوي','الزيني','الخليل','الرفاعي','الصباغ','الطرابلسي','العلي','الفاعور','القدسي',
    'الكسواني','اللحام','المحمد','النجار','الهندي','الياسين','الأسعد','البقاعي','الجمل','الحمصي',
    'الديري','الرياشي','الزعبي','السقا','الشامي','الصيداوي','الطويل','العبسي','الفارس','القطان',
    'اللبابيدي','المصري','النابلسي','الهواري','اليوسف','أبو زيد','أبو سعد','أبو علي','ابن علي','آل علي',
    'بركات','جبران','حمادة','خوري','درويش','رزق','سلمان','شاهين','طربي','عبدالله',
    'عواد','فضل','قاسم','كنيش','لحود','مراد','ناصر','هلال','ياسين','زيدان',
    'حنا','سعود','عمر','فارس','كريم','ماجد','نادر','وسام','ياسر','حسن',]
def logo():
    return r"""
   _____ _                                            
  / ____| |          Account Creator                                 
 | (___ | |__   _____      ____ _ _ __ __ _ _ __ ___  
  \___ \| '_ \ / _ \ \ /\ / / _` | '__/ _` | '_ ` _ \ 
  ____) | | | | (_) \ V  V / (_| | | | (_| | | | | | |
 |_____/|_| |_|\___/ \_/\_/ \__, |_|  \__,_|_| |_| |_|
                             __/ |                    
                            |___/   By: MR Joker                
"""

class Add_Likes_Comments:
    def __init__(self,token , post_id):
        self.token = token
        self.post_id = post_id
        self.likes = False
        try:
            joker = requests.get(f'https://api.demoda.app/api/reels/{self.post_id}' ,headers = { 'Host': 'api.demoda.app', 'Accept': 'application/json, text/plain, */*', 'Authorization': f'Bearer {self.token}', 'Accept-Encoding': 'gzip, deflate','User-Agent': 'Showgram/10 CFNetwork/3860.600.12 Darwin/25.5.0','Priority': 'u=3, i','Accept-Language': 'ar',}).json().get('reel', {})
            self.viewToken = joker.get('viewToken', '')
            data = {"token":self.viewToken,"watchedMs":3000}
            JQ = requests.post(f'https://api.demoda.app/api/reels/{self.post_id}/view' ,headers = { 'Host': 'api.demoda.app', 'Accept': 'application/json, text/plain, */*', 'Authorization': f'Bearer {self.token}', 'Accept-Encoding': 'gzip, deflate','User-Agent': 'Showgram/10 CFNetwork/3860.600.12 Darwin/25.5.0','Priority': 'u=3, i','Accept-Language': 'ar',}, json=data)
        except Exception as e:pass
        self.Add_Likes()
    def Add_Comments(self):
        headers = {
            'Host': 'api.demoda.app',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Showgram/10 CFNetwork/3860.600.12 Darwin/25.5.0',
            'Priority': 'u=3, i',
            'Accept-Language': 'ar'}
        Comments = choice(["❤️","🔥🔥","❤️🔥","💙🦋","❤️❤️❤️","👀🔥","😍😍","🃏🫣","👀💙","🔥🔥🔥🔥"])
        data = {"text": Comments}
        JQ = requests.post(f'https://api.demoda.app/api/reels/{self.post_id}/comments' , headers=headers , json=data)
        if '"text":"'+Comments+'"' in JQ.text:
            return True
        else:
            return False
    def Add_Likes(self):
        headers = {
            'Host': 'api.demoda.app',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': f'Bearer {self.token}',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Showgram/10 CFNetwork/3860.600.12 Darwin/25.5.0',
            'Priority': 'u=3, i',
            'Accept-Language': 'ar',}
        data = {}
        JQ = requests.post(f'https://api.demoda.app/api/reels/{self.post_id}/like' , headers=headers , json=data)
        if '"liked":true' in JQ.text:
            self.likes = self.Add_Comments()
        else:
            self.likes = False
class Account_Followers:
    def __init__(self,token , TARGET):
        self.token = token
        self.TARGET = TARGET
        self.Followers = []
        self.followed = False
        self.search_account()
    def Add_Followers(self , target_id , headers):
        data = {}
        JQ = requests.post(f'https://api.demoda.app/api/follows/{target_id}' , headers=headers , json=data)
        if '"following":true' in JQ.text:
            return True
        else:
            return False
    def search_account(self):
        headers = {
            'Host': 'api.demoda.app',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': f'Bearer {self.token}',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Showgram/10 CFNetwork/3860.600.12 Darwin/25.5.0',
            'Priority': 'u=3, i',
            'Accept-Language': 'ar',}
        JQ = requests.get(f'https://api.demoda.app/api/users/search?q={self.TARGET}' , headers=headers)
        items = JQ.json().get('items', [])
        if items:
            self.target_id = items[0]['id']
            self.followed = self.Add_Followers(self.target_id , headers)
        else:
            self.followed = False
class Account_Creator:
    def __init__(self):
        self.FileUsers = set()
        self.TARGET = input('[+] Enter Your Username to Follow: ')
        self.FileUsers_mode = input('[+] Do you want to use a username file? (y/n) :  ').lower()
        if self.FileUsers_mode == 'y':
            self.FileUsers_mode = True
            while True: 
                try:
                    self.FileUsers = set(open(input('[+] Enter the path of the username file: '), 'r').read().splitlines())
                    break
                except Exception as e:
                    print('[-] Invalid username file , try again')
        else:
            self.FileUsers_mode = False
        self.ADD_LIKES_mode = input('[+] Add Likes and Comments ? (y/n) :  ').lower()
        if self.ADD_LIKES_mode == 'y':
            self.ADD_LIKES_mode = True
            while True:
                self.POST_ID = input('[+] Enter URL Reels :  ').split('/r/')[-1]
                if self.POST_ID:
                    break
                else:
                    print('[+] Invalid URL Reels')
        else:
            self.ADD_LIKES_mode = False
            self.POST_ID = None
        self.Threads = 50
        self.username_length = 5
        self.proxy = []
        self.secuess , self.followers ,self.likes ,self.prx_errors ,self.errors = 0, 0, 0, 0,0
        self.lock = Lock()
        self.used_names = set()
        while True:
            try:
                with open(input('Enter the path of the proxy file: '), 'r') as proxy_file:
                    self.proxy = proxy_file.read().splitlines()
                break
            except Exception as e:
                print('Proxy file not found , try again')
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo())
        self.run()
    def run(self):
        threads = []
        for i in range(self.Threads):
            t = Thread(target=self.Signup)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
    def SAVE(self , files , RESULT):
        try:
            with open(f'{files}.txt', 'a' , encoding='utf-8' , errors='ignore') as wr:
                wr.write(f"{RESULT}\n")
        except Exception as e:pass
    def Generator_Password(self):
        return ''.join(choice('0123456789@@ABCDEFGHIJK$LMNOPQRSTUVW@XYZabcdefghijklmnopq!rstuvwxyz') for i in range(8))
    def Generator_Phone(self):
        return ''.join(choice('0123456789') for i in range(9))
    def Generator_DeviceId(self):
        return f"{''.join(choice('0123456789ABCDEF') for i in range(8))}-{''.join(choice('0123456789ABCDEF') for i in range(4))}-{''.join(choice('0123456789ABCDEF') for i in range(4))}-{''.join(choice('0123456789ABCDEF') for i in range(4))}-{''.join(choice('0123456789ABCDEF') for i in range(12))}"
    def Generator_DeviceName(self):
        div = ['iPhone' , 'iPad' , 'huawei' , 'samsung' , 'oppo' , 'vivo']
        phone = choice(div)
        if 'iPhone' in phone or 'iPad' in phone:
            platform = 'IOS'
        else:
            platform = 'Android'
        return phone , platform
    def Generator_usernames(self):
        if self.FileUsers_mode:
            if not self.FileUsers:
                raise Exception('Username file is empty')
            self.username = self.FileUsers.pop()
        else:
            self.username= str(''.join((choice('qwe1rty2uiop3asd4fg_hjkl5zxcv6bnmza7qwsxedcr9fvbhy_ojmly') for i in range(self.username_length))))
    def Generator_names(self):
        for _ in range(500):
            name = f"{choice(FIRST_NAMES)} {choice(LAST_NAMES)}"
            if name not in self.used_names:
                self.used_names.add(name)
                return name
        name = f"{choice(FIRST_NAMES)} {choice(LAST_NAMES)}"
        self.used_names.add(name)
        return name
    def update_proxy(self):
        PRX = str(choice(self.proxy))
        return {
            'http': f'http://{PRX}',
            'https': f'http://{PRX}'}
    def setup_profile(self,token , PWD):
        while True:
            self.Generator_usernames()
            username = self.username
            headers = {
                'Host': 'api.demoda.app',
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {token}',
                'Accept-Encoding': 'gzip, deflate',
                'User-Agent': 'Showgram/10 CFNetwork/3860.600.12 Darwin/25.5.0',
                'Priority': 'u=3, i',
                'Accept-Language': 'ar',}
            full_name = self.Generator_names()
            data = {"name": full_name, "username": f"{username}"}
            JQ = requests.post('https://api.demoda.app/api/users/setup-profile' , headers=headers , json=data)
            if JQ.text.__contains__('username'):
                self.secuess += 1
                try:requests.post('https://api.demoda.app/api/users/me/profile', headers = {'Host': 'api.demoda.app','Accept': 'application/json, text/plain, */*','Content-Type': 'application/json','Authorization': f'Bearer {token}', 'Accept-Encoding': 'gzip, deflate', 'User-Agent': 'Showgram/10 CFNetwork/3860.600.12 Darwin/25.5.0','Priority': 'u=3, i','Accept-Language': 'ar',}, json = {'name': full_name,'bio': BIO,'link': 'https://github.com/vv1ck',})
                except Exception as e:pass
                self.SAVE('Done_Creating' , f"{username}:{PWD} | {token}")
                break
            elif JQ.text.__contains__('"message":"اسم المستخدم محجوز، جرّب غيره"'):
                continue
            else:
                self.SAVE('bad_accounts2' , f"{JQ.text} , {JQ.status_code}")
                continue
        follower = Account_Followers(token, self.TARGET)
        if follower.followed:
            self.followers += 1
        if self.ADD_LIKES_mode:
            likes = Add_Likes_Comments(token, self.POST_ID)
            if likes.likes:
                self.likes += 1
    def Signup(self):
        while True:
            try:
                headers = {
                    'Host': 'api.demoda.app',
                    'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json',
                    'Accept-Language': 'ar',
                    'Accept-Encoding': 'gzip, deflate',
                    'User-Agent': 'Showgram/10 CFNetwork/3860.600.12 Darwin/25.5.0',
                    'Priority': 'u=3, i',}
                deviceName , platform = self.Generator_DeviceName()
                PWD = self.Generator_Password()
                phone = self.Generator_Phone()
                data = {"phone":f"+{phone}","password":f"{PWD}","deviceName":deviceName,"platform":platform,"deviceId":f"{self.Generator_DeviceId()}"}
                JQ = requests.post('https://api.demoda.app/api/auth/signup/phone' , headers=headers , json=data , proxies=self.update_proxy() , timeout=10)
                if JQ.text.__contains__('token'):
                    with self.lock:
                        token = JQ.json()['token']
                        self.setup_profile(token ,PWD)
                elif JQ.text.__contains__('طلبات كثيرة'):
                    self.prx_errors += 1
                elif JQ.text.__contains__("كلمة المرور لازم تحتوي أحرفاً وأرقاماً"):
                    continue
                else:
                    self.SAVE('bad_accounts1' , f"{JQ.text} , {JQ.status_code}")
            except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout, requests.exceptions.ChunkedEncodingError, requests.exceptions.InvalidURL, requests.exceptions.ProxyError, requests.exceptions.Timeout, requests.exceptions.HTTPError) as e:
                self.prx_errors += 1
            except Exception as e:
                self.lock.acquire()
                self.errors += 1
                self.SAVE('ERRORS' , e)
                self.lock.release()
            
            print(f'Creating: {self.secuess} | Followers Added: {self.followers} | Likes Added: {self.likes} | Proxy Errors: {self.prx_errors} | Errors: {self.errors} ', f'\r', end='', flush=True)

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('title Account Creator ~ By JoKer')
    print(logo())
    Account_Creator()
