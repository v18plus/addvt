from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, PhoneNumberBannedError, ChatAdminRequiredError
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError, UserBannedInChannelError, UserAlreadyParticipantError, FloodWaitError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.channels import LeaveChannelRequest
import sys
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.messages import ImportChatInviteRequest, AddChatUserRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import UserStatusRecently
import time
import random
import os
import pickle
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
from colorama import init, Fore
from time import sleep
import csv
scam = '@notoscam'
init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    # fancy logo

   #kanger ki maki chut
   # bsdk remove mt krna nhi toh gey ki aulad
   # puch lena bsdkk                                                
    
    b= [

     '██████╗ ███████╗ █████╗ ███████╗████████╗',
     '██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝',
     '██████╔╝█████╗  ███████║███████╗   ██║',
     '██╔══██╗██╔══╝  ██╔══██║╚════██║   ██║',
     '██████╔╝███████╗██║  ██║███████║   ██║',
     '╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝',

      '█████╗ ██████╗ ██████╗ ███████╗██████╗',
     '██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗ ',
     '███████║██║  ██║██║  ██║█████╗  ██████╔╝',
     '██╔══██║██║  ██║██║  ██║██╔══╝  ██╔══██╗',
     '██║  ██║██████╔╝██████╔╝███████╗██║  ██║',
     '╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝'

    ]
    for char in b:
        print(f'{char}{w}')
    print(f'{r} Author: github.com/msy1717{r}')
    print(f'{r} Developer : @Godmrunal{r}')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(ye+'Choose a Option:'+n)
    print(cy+'            [1] Add new accounts'+n)
    print(cy+'            [2] Filter all banned accounts'+n)
    print(cy+'            [3] Remove specific accounts'+n)
    print(cy+'            [4] Member Adding'+n)
    print(ye+'Special Options:'+n)
    print(cy+'            [5] Scam Tag [Special]'+n)
    print(cy+'            [6] Bulk Message Sender[special]'+n)
    print(cy+'            [7] Set Profile Pic  '+n)
    print(cy+'            [8] Report Spam A User'+n)
    print(ye+'Additional Options:'+n)
    print(cy+'            [9]  Send DM [pm spam]'+n)
    print(cy+'            [11] join channel/group '+n)
    print(cy+'            [12] leave channel/group'+n)
    print(cy+'            [13] Update Script'+n)
    print(cy+'            [0]  Exit'+n)



    a = int(input('\nEnter your choice: '))
    if a == 1:
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{lg} [~] Enter number of accounts to add: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{lg} [~] Enter Phone Number: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{lg} [i] Saved all accounts in vars.txt')
            clr()
            print(f'\n{lg} [*] Logging in from new accounts\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 8027196 , '9b70b20efd67e9b99edc395d78407cfa')
                c.start(number)
                print(f'{lg}[+] Login successful')
                c.disconnect()
            input(f'\n Press enter to goto main menu...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] There are no accounts! Please add some and retry')
            sleep(3)
        else:
            for account in accounts:
                phone = a[0]
                client = TelegramClient(f'sessions/{phone}', 8027196 , '9b70b20efd67e9b99edc395d78407cfa')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Enter the code: '))
                        print(f'{lg}[+] {phone} is not banned{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' is banned!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Congrats! No banned accounts')
                input('\nPress enter to goto main menu...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] All banned accounts removed'+n)
                input('\nPress enter to goto main menu...')

    elif a == 3:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{lg}[i] Choose an account to delete\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] Enter a choice: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Account Deleted{n}')
        input(f'\nPress enter to goto main menu...')
        f.close()
    elif a == 4:
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        
        #print('\n' + info + lg + ' Checking for banned accounts...' + rs)
        print('\n' ' Checking for banned accounts...' )
        for a in accounts:
            phn = a[0]
            print(f'Checking {lg}{phn}')
            clnt = TelegramClient(f'sessions/{phn}', 8027196 , '9b70b20efd67e9b99edc395d78407cfa')
            clnt.connect()
            banned = []
            if not clnt.is_user_authorized():
                try:
                    clnt.send_code_request(phn)
                    print('kk')
                except PhoneNumberBannedError:
                    print(f'{error} {w}{phn} {r}is banned!{rs}')
                    banned.append(a)
            for z in banned:
                accounts.remove(z)
                print('{lg}Banned account removed[Remove permanently using manager.py]{rs}')
            time.sleep(0.5)
            clnt.disconnect()
        print(' Sessions created!')
        clr()
        banner()
# func to log scraping details(link of the grp to scrape
# and current index) in order to resume later
        def log_status(scraped, index):
            with open('status.dat', 'wb') as f:
                pickle.dump([scraped, int(index)], f)
                f.close()
            print(f'{lg} Session stored in {w}status.dat{lg}')
    

        def exit_window():
            input(f'\n{cy} Press enter to exit...')
            clr()
            banner()
            sys.exit()
        try:
            with open('status.dat', 'rb') as f:
                status = pickle.load(f)
                f.close()
                lol = input(f'{cy} Resume scraping members from {w}{status[0]}{lg}? [y/n]: {r}')
                if 'y' in lol:
                    scraped_grp = status[0] ; index = int(status[1])
                else:
                    if os.name == 'nt':
                        os.system('del status.dat')
                    else: 
                        os.system('rm status.dat')
                    scraped_grp = input(f'{cy} Public/Private group link to scrape members: {r}')
                    index = 0
        except:
            scraped_grp = input(f'{cy} Public/Private group link to scrape members: {r}')
            index = 0
# load all the accounts(phonenumbers)
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        print(f'{lg} Total accounts: {w}{len(accounts)}')
        number_of_accs = int(input(f'{cy} Enter number of accounts to use: {r}'))
        print(f'{cy} Choose an option{lg}')
        print(f'{cy}[0]{lg} Add to public group')
        print(f'{cy}[1]{lg} Add to private group')
        choice = int(input(f'{cy} Enter choice: {r}'))
        if choice == 0:
            target = str(input(f'{cy} Enter public group link: {r}'))
        else:
            target = str(input(f'{cy} Enter private group link: {r}'))

        print(f'_'*50)
        status_choice = str(input(f'{cy} Do you wanna add active members?[y/n]: {r}'))
        to_use = [x for x in accounts[:number_of_accs]]
        for l in to_use: accounts.remove(l)
        with open('vars.txt', 'wb') as f:
            for a in accounts:
                pickle.dump(a, f)
            for ab in to_use:
                pickle.dump(ab, f)
            f.close()
        sleep_time = int(input(f'{cy} Enter delay time per request{w}[{lg}0 for None{w}]: {r}'))
        print(f'{lg} Joining group from {w}{number_of_accs} accounts...')
        print(f'-'*50)
        print(f'{lg} -- Adding members from {w}{len(to_use)}{lg} account(s) --')
        adding_status = 0
        approx_members_count = 0
        for acc in to_use:
            stop = index + 60
            c = TelegramClient(f'sessions/{acc[0]}', 8027196 , '9b70b20efd67e9b99edc395d78407cfa')
            print(f' User: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
            c.start(acc[0])
            acc_name = c.get_me().first_name
            try:
                if '/joinchat/' in scraped_grp:
                    g_hash = scraped_grp.split('/joinchat/')[1]

                    try:
                        c(ImportChatInviteRequest(g_hash))
                        print(f'User: {cy}{acc_name}{lg} -- Joined group to scrape')
                    except UserAlreadyParticipantError:
                        pass 
                else:
                    c(JoinChannelRequest(scraped_grp))
                    print(f'User: {cy}{acc_name}{lg} -- Joined group to scrape')
                scraped_grp_entity = c.get_entity(scraped_grp)
                if choice == 0:
                    c(JoinChannelRequest(target))
                    print(f'User: {cy}{acc_name}{lg} -- Joined group to add')
                    target_entity = c.get_entity(target)
                    target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
                else:
                    try:
                        grp_hash = target.split('/joinchat/')[1]
                        c(ImportChatInviteRequest(grp_hash))
                        print(f'User: {cy}{acc_name}{lg} -- Joined group to add')
                    except UserAlreadyParticipantError:
                        pass
                    target_entity = c.get_entity(target)
                    target_details = target_entity
            except Exception as e:
                print(f'User: {cy}{acc_name}{lg} -- Failed to join group')
                print(f'{e}')
                continue
            print(f' User: {cy}{acc_name}{lg} -- {cy}Retrieving entities...')
    #c.get_dialogs()
            try:
                members = []
                members = c.get_participants(scraped_grp_entity, aggressive=True)
            except Exception as e:
                print(f' Couldn\'t scrape members')
                print(f'{e}')
                continue
            approx_members_count = len(members)
            assert approx_members_count != 0
            if index >= approx_members_count:
                print(f'{lg} No members to add!')
                continue
            print(f'{lg} Start: {w}{index}')
    #adding_status = 0
            peer_flood_status = 0
            for user in members[index:stop]:
                index += 1
                if peer_flood_status == 10:
                    print(f'Too many Peer Flood Errors! Closing session...')
                    break
                try:
                    if choice == 0:
                        c(InviteToChannelRequest(target_details, [user]))
                    else:
                        c(AddChatUserRequest(target_details.id, user, 42))
                    user_id = user.first_name
                    target_title = target_entity.title
                    print(f'User: {cy}{acc_name}{lg} ==> {cy}{user_id} {lg}==> {cy}{target_title}')
                    #print(f'User: {cy}{acc_name}{lg} -- Sleep 1 second')
                    adding_status += 1
                    print(f'User: {cy}{acc_name}{lg} -- Sleep {w}{sleep_time} {lg}second(s)')
                    time.sleep(sleep_time)
                except UserPrivacyRestrictedError:
                    print(f'User: {cy}{acc_name}{lg} -- {r}User Privacy Restricted Error')
                    continue
                except PeerFloodError:
                    print(f'User: {cy}{acc_name}{lg} -- {r}Peer Flood Error.')
                    peer_flood_status += 1
                    continue
                except ChatWriteForbiddenError:
                    print(f'Can\'t add to group. Contact group admin to enable members adding')
                    if index < approx_members_count:
                        log_status(scraped_grp, index)
                        exit_window()
                except UserBannedInChannelError:
                    print(f'User: {cy}{acc_name}{lg} -- {r}Banned from writing in groups')
                    break
                except ChatAdminRequiredError:
                    print(f'User: {cy}{acc_name}{lg} -- {r}Chat Admin rights needed to add')
                    break
                except UserAlreadyParticipantError:
                    print(f'User: {cy}{acc_name}{lg} -- {r}User is already a participant')
                    continue
                except FloodWaitError as e:
                    print(f'{e}')
                    break
                except ValueError:
                    print(f'Error in Entity')
                    continue
                except KeyboardInterrupt:
                    print(f'---- Adding Terminated ----')
                    if index < len(members):
                        log_status(scraped_grp, index)
                        exit_window()
                except Exception as e:
                    print(f'{e}')
                    continue
#global adding_status, approx_members_count
        if adding_status != 0:
            print(f"\n{lg} Adding session ended")
            try:
                if index < approx_members_count:
                    log_status(scraped_grp, index)
                    exit_window()
            except:
                exit_window()
    elif a == 5:
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        
        #print('\n' + info + lg + ' Checking for banned accounts...' + rs)
        print('\n' ' Checking for banned accounts...' )
        for a in accounts:
            phn = a[0]
            print(f'Checking {lg}{phn}')
            clnt = TelegramClient(f'sessions/{phn}', 8027196 , '9b70b20efd67e9b99edc395d78407cfa')
            clnt.connect()
            banned = []
            if not clnt.is_user_authorized():
                try:
                    clnt.send_code_request(phn)
                    print('kk')
                except PhoneNumberBannedError:
                    print(f'{error} {w}{phn} {r}is banned!{rs}')
                    banned.append(a)
            for z in banned:
                accounts.remove(z)
                print('{lg}Banned account removed[Remove permanently using manager.py]{rs}')
            time.sleep(0.5)
            clnt.disconnect()
        print(' Sessions created!')
        clr()
        banner()
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break
        print(f'{lg} Total accounts: {w}{len(accounts)}')
        number_of_accs = int(input(f'{cy} Enter number of accounts to Report: {r}'))
        choice = str(input(f'{cy} Send Message For Report {r}'))
        to_use = [x for x in accounts[:number_of_accs]]
        for l in to_use: accounts.remove(l)
        with open('vars.txt', 'wb') as f:
            for a in accounts:
                pickle.dump(a, f)
            for ab in to_use:
                pickle.dump(ab, f)
            f.close()
        sleep_time = 1
        print(f'{lg} -- Sending Reports from {w}{len(to_use)}{lg} account(s) --')   
        send_status = 0
        
        approx_members_count = 0
        index = 0
        for acc in to_use:
            stop = index + 60
            c = TelegramClient(f'sessions/{acc[0]}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
            print(f'User: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
            c.start(acc[0])
            acc_name = c.get_me().first_name
            try:
                c(JoinChannelRequest('@Beast_Selling')) 
                c.send_message(scam,choice)
                print(f'Report Done From: {cy}{acc_name}{lg}  To Notoscam-- ')
                send_status += 1
            except Exception as e:
                print(f'{e}')
                continue
        if send_status != 0:
            print(f"\n{lg}session ended")
            input(f'\n{cy} Press enter to exit...')
        else:
            print(f"\n{lg}All reports done sucesfully")
            input(f'\n{cy} Press enter to exit...')

    elif a == 6:
        accounts = []
        chats = []
        last_date = None
        chunk_size = 200
        groups = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break
        print('\n' ' Checking for banned accounts...' )
        for a in accounts:
            phn = a[0]
            print(f'Checking {lg}{phn}')
            clnt = TelegramClient(f'sessions/{phn}', 8027196 , '9b70b20efd67e9b99edc395d78407cfa')
            clnt.connect()
            banned = []
            if not clnt.is_user_authorized():
                try:
                    clnt.send_code_request(phn)
                    print('kk')
                except PhoneNumberBannedError:
                    print(f'{error} {w}{phn} {r}is banned!{rs}')
                    banned.append(a)
            for z in banned:
                accounts.remove(z)
                print('{lg}Banned account removed[Remove permanently using manager.py]{rs}')
            time.sleep(0.5)
           # clnt.disconnect()
        print(' Sessions created!')
        clr()
        banner()
        result = clnt(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
        ))
        chats.extend(result.chats)
        for chat in chats:
            try:
                if chat.megagroup == True:
                    groups.append(chat)
            except:
                continue
        acc_name = clnt.get_me().first_name 

        print(f'Message was sending throuh {acc_name} {ye}')
        print(f'Message was sending throuh {acc_name} {ye}')
        print(f'Choose a group to scrape members from:{lg}')
        i = 0
        for g in groups:
            print(str(i) + '- ' + g.title)
            i += 1
        g_index = input(f"Enter a Number:{lg}")
        target_group = groups[int(g_index)]
        print('Fetching Members...')
        all_participants = []
        all_participants = clnt.get_participants(target_group, aggressive=True)
        print('Saving In file...')
        with open("members.csv", "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
            for user in all_participants:
                if user.username:
                    username = user.username
                else:
                    username = ""
                if user.first_name:
                    first_name = user.first_name
                else:
                    first_name = ""
                if user.last_name:
                    last_name = user.last_name
                else:
                    last_name = ""
                name = (first_name + ' ' + last_name).strip()
                writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
        print(f'Members scraped successfully.{lg}')
        SLEEP_TIME_2 = 1800
        SLEEP_TIME_1 = 400
        SLEEP_TIME = int(input(f"Enter sleep time duration in messages :{lg}"))
        users = []
        with open(r"members.csv", encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['username'] = row[0]
                user['id'] = int(row[1])
                user['access_hash'] = int(row[2])
                user['name'] = row[3]
                users.append(user)
        mode = int(input(f"Enter 1 to send by user ID or 2 to send by username:{lg}"))
        message = str(input(f"send your messsage{lg}"))  
        for user in users:
            if mode == 2:
                if user['username'] == "":
                    continue
                receiver = clnt.get_input_entity(user['username'])
            elif mode == 1:
                receiver = InputPeerUser(user['id'],user['access_hash'])
            else:
                print(f"Invalid Mode. Exiting.{lg}")
                clnt.disconnect()
                sys.exit()
            try:
                print(f"Sending Message to:{lg}", user['name'])
                clnt.send_message(receiver, message.format(user['name']))
                print("Waiting {} seconds{lg}".format(SLEEP_TIME))
                time.sleep(SLEEP_TIME)
            except PeerFloodError:
                print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                print("Waiting {} seconds".format(SLEEP_TIME_2))
                time.sleep(SLEEP_TIME_2)
            except Exception as e:
                print("Error:", e)
                print("Trying to continue...")
                print("Waiting {} seconds".format(SLEEP_TIME_1))
                time.sleep(SLEEP_TIME_1)
        clnt.disconnect()
        print(f"Done. Message sent to all users.{lg}") 
        input(f'\n Press enter to goto main menu...')
      
    elif a == 7:
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        
        #print('\n' + info + lg + ' Checking for banned accounts...' + rs)
        print('\n' ' Checking for banned accounts...' )
        for a in accounts:
            phn = a[0]
            print(f'Checking {lg}{phn}')
            clnt = TelegramClient(f'sessions/{phn}', 8027196 , '9b70b20efd67e9b99edc395d78407cfa')
            clnt.connect()
            banned = []
            if not clnt.is_user_authorized():
                try:
                    clnt.send_code_request(phn)
                    print('kk')
                except PhoneNumberBannedError:
                    print(f'{error} {w}{phn} {r}is banned!{rs}')
                    banned.append(a)
            for z in banned:
                accounts.remove(z)
                print('{lg}Banned account removed[Remove permanently using manager.py]{rs}')
            time.sleep(0.5)
            clnt.disconnect()
        print(' Sessions created!')
        clr()
        banner()
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break
        print(f'{lg} Total accounts: {w}{len(accounts)}')
        number_of_accs = int(input(f'{cy} Enter number of accouns to change Pic {r}'))
        to_use = [x for x in accounts[:number_of_accs]]
        for l in to_use: accounts.remove(l)
        with open('vars.txt', 'wb') as f:
            for a in accounts:
                pickle.dump(a, f)
            for ab in to_use:
                pickle.dump(ab, f)
            f.close()
        sleep_time = 1
        print(f'{lg} --Profie Set Sucesfully{w}{len(to_use)}{lg} account --')   
        send_status = 0
        
        approx_members_count = 0
        index = 0
        for acc in to_use:
            stop = index + 60
            c = TelegramClient(f'sessions/{acc[0]}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
            print(f'User: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
            c.start(acc[0])
            acc_name = c.get_me().first_name
            try:
                c(UploadProfilePhotoRequest(c.upload_file('beast.jpg')))
                print(f'Profile Set Sucesfully To: {cy}{acc_name}{lg}  T-- ')
                send_status += 1
            except Exception as e:
                print(f'{e}')
                continue
        if send_status != 0:
            print(f"\n{lg}session ended")
            input(f'\n{cy} Press enter to exit...')
        else:
            print(f"\n{lg} all profile setupped succesfully")
            input(f'\n{cy} Press enter to exit...')
       
    elif a == 8:
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        
        #print('\n' + info + lg + ' Checking for banned accounts...' + rs)
        print('\n' ' Checking for banned accounts...' )
        for a in accounts:
            phn = a[0]
            print(f'Checking {lg}{phn}')
            clnt = TelegramClient(f'sessions/{phn}', 8027196 , '9b70b20efd67e9b99edc395d78407cfa')
            clnt.connect()
            banned = []
            if not clnt.is_user_authorized():
                try:
                    clnt.send_code_request(phn)
                    print('kk')
                except PhoneNumberBannedError:
                    print(f'{error} {w}{phn} {r}is banned!{rs}')
                    banned.append(a)
            for z in banned:
                accounts.remove(z)
                print('{lg}Banned account removed[Remove permanently using manager.py]{rs}')
            time.sleep(0.5)
            clnt.disconnect()
        print(' Sessions created!')
        clr()
        banner()
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break
        print(f'{lg} Total accounts: {w}{len(accounts)}')
        number_of_accs = int(input(f'{cy} Enter number of accounts to report spam  {r}'))
        user = str(input(f'{cy} Enter Group,Channel or user username{r}'))
        to_use = [x for x in accounts[:number_of_accs]]
        for l in to_use: accounts.remove(l)
        with open('vars.txt', 'wb') as f:
            for a in accounts:
                pickle.dump(a, f)
            for ab in to_use:
                pickle.dump(ab, f)
            f.close()
        sleep_time = 1
        print(f'{lg} --Report Spam Started Sucesfully{user}{lg} account --')   
        send_status = 0
        
        approx_members_count = 0
        index = 0
        for acc in to_use:
            stop = index + 60
            c = TelegramClient(f'sessions/{acc[0]}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
            print(f'User: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
            c.start(acc[0])
            acc_name = c.get_me().first_name
            try:
                c(ReportSpamRequest(user))
                
                print(f'=======Reported spam {user}:from {cy}{acc_name}{lg}======== ')
                send_status += 1
            except Exception as e:
                print(f'{e}')
                continue
        if send_status != 0:
            print(f"\n{lg}session ended")
            input(f'\n{cy} Press enter to exit...')
        else:
            print(f"\n{lg} all reports done sucessfylly")
            input(f'\n{cy} Press enter to exit...')
        
    elif a == 9:
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        
        #print('\n' + info + lg + ' Checking for banned accounts...' + rs)
        print('\n' ' Checking for banned accounts...' )
        for a in accounts:
            phn = a[0]
            print(f'Checking {lg}{phn}')
            clnt = TelegramClient(f'sessions/{phn}', 8027196 , '9b70b20efd67e9b99edc395d78407cfa')
            clnt.connect()
            banned = []
            if not clnt.is_user_authorized():
                try:
                    clnt.send_code_request(phn)
                    print('kk')
                except PhoneNumberBannedError:
                    print(f'{error} {w}{phn} {r}is banned!{rs}')
                    banned.append(a)
            for z in banned:
                accounts.remove(z)
                print('{lg}Banned account removed[Remove permanently using manager.py]{rs}')
            time.sleep(0.5)
            clnt.disconnect()
        print(' Sessions created!')
        clr()
        banner()
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break
        print(f'{lg} Total accounts: {w}{len(accounts)}')
        number_of_accs = int(input(f'{cy} Enter number of accounts To send Dm {r}'))
        use = str(input(f'{cy} Enter username of a user to send dm him/her{r}'))
        msg_topi = str(input(f'{cy} Now enter Message to send him{r}'))
        to_use = [x for x in accounts[:number_of_accs]]
        for l in to_use: accounts.remove(l)
        with open('vars.txt', 'wb') as f:
            for a in accounts:
                pickle.dump(a, f)
            for ab in to_use:
                pickle.dump(ab, f)
            f.close()
        sleep_time = 1
        print(f'{lg} --Sending Dm to {use}{lg}..... --')   
        send_status = 0
        
        approx_members_count = 0
        index = 0
        for acc in to_use:
            stop = index + 60
            c = TelegramClient(f'sessions/{acc[0]}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
            print(f'User: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
            c.start(acc[0])
            acc_name = c.get_me().first_name
            try:
                c.send_message(use,msg_topi)
                print(f'=======Dm sent {use}:from {cy}{acc_name}{lg}======== ')
                send_status += 1
            except Exception as e:
                print(f'{e}')
                continue
        if send_status != 0:
            print(f"\n{lg}session ended")
            input(f'\n{cy} Press enter to exit...')
        else:
            print(f"\n{lg} All Dm done sucessfylly")
            input(f'\n{cy} Press enter to exit...')

    elif a == 11:
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        
        #print('\n' + info + lg + ' Checking for banned accounts...' + rs)
        print('\n' ' Checking for banned accounts...' )
        for a in accounts:
            phn = a[0]
            print(f'Checking {lg}{phn}')
            clnt = TelegramClient(f'sessions/{phn}', 8027196 , '9b70b20efd67e9b99edc395d78407cfa')
            clnt.connect()
            banned = []
            if not clnt.is_user_authorized():
                try:
                    clnt.send_code_request(phn)
                    print('kk')
                except PhoneNumberBannedError:
                    print(f'{error} {w}{phn} {r}is banned!{rs}')
                    banned.append(a)
            for z in banned:
                accounts.remove(z)
                print('{lg}Banned account removed[Remove permanently using manager.py]{rs}')
            time.sleep(0.5)
            clnt.disconnect()
        print(' Sessions created!')
        clr()
        banner()
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break
        print(f'{lg} Total accounts: {w}{len(accounts)}')
        number_of_accs = int(input(f'{cy} Enterr number accout to join channel or group {r}'))
        join_op = str(input(f'{cy} send channel/group username {r}'))
        to_use = [x for x in accounts[:number_of_accs]]
        for l in to_use: accounts.remove(l)
        with open('vars.txt', 'wb') as f:
            for a in accounts:
                pickle.dump(a, f)
            for ab in to_use:
                pickle.dump(ab, f)
            f.close()
        sleep_time = 1
        print(f'{lg} --joining channels--')   
        send_status = 0
        
        approx_members_count = 0
        index = 0
        for acc in to_use:
            stop = index + 60
            c = TelegramClient(f'sessions/{acc[0]}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
            print(f'User: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
            c.start(acc[0])
            acc_name = c.get_me().first_name
            try:
                c(JoinChannelRequest(join_op))
                print(f'joined from: {cy}{acc_name}{lg}  Sucesfully-- ')
                send_status += 1
            except Exception as e:
                print(f'{e}')
                continue
        if send_status != 0:
            print(f"\n{lg}session ended")
            input(f'\n{cy} Press enter to exit...')
        else:
            print(f"\n{lg} Joined succesfully")
            input(f'\n{cy} Press enter to exit...')
        
    elif a == 12:
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        
        #print('\n' + info + lg + ' Checking for banned accounts...' + rs)
        print('\n' ' Checking for banned accounts...' )
        for a in accounts:
            phn = a[0]
            print(f'Checking {lg}{phn}')
            clnt = TelegramClient(f'sessions/{phn}', 8027196 , '9b70b20efd67e9b99edc395d78407cfa')
            clnt.connect()
            banned = []
            if not clnt.is_user_authorized():
                try:
                    clnt.send_code_request(phn)
                    print('kk')
                except PhoneNumberBannedError:
                    print(f'{error} {w}{phn} {r}is banned!{rs}')
                    banned.append(a)
            for z in banned:
                accounts.remove(z)
                print('{lg}Banned account removed[Remove permanently using manager.py]{rs}')
            time.sleep(0.5)
            clnt.disconnect()
        print(' Sessions created!')
        clr()
        banner()
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break
        print(f'{lg} Total accounts: {w}{len(accounts)}')
        number_of_accs = int(input(f'{cy} Enterr number accout to join channel or group {r}'))
        left_op = str(input(f'{cy} send channel/group username {r}'))
        to_use = [x for x in accounts[:number_of_accs]]
        for l in to_use: accounts.remove(l)
        with open('vars.txt', 'wb') as f:
            for a in accounts:
                pickle.dump(a, f)
            for ab in to_use:
                pickle.dump(ab, f)
            f.close()
        sleep_time = 1
        print(f'{lg} --Leaving channels--')   
        send_status = 0
        
        approx_members_count = 0
        index = 0
        for acc in to_use:
            stop = index + 60
            c = TelegramClient(f'sessions/{acc[0]}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
            print(f'User: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
            c.start(acc[0])
            acc_name = c.get_me().first_name
            try:
                c(LeaveChannelRequest(left_op))
                print(f'left from: {cy}{acc_name}{lg}  Sucesfully-- ')
                send_status += 1
            except Exception as e:
                print(f'{e}')
                continue
        if send_status != 0:
            print(f"\n{lg}session ended")
            input(f'\n{cy} Press enter to exit...')
        else:
            print(f"\n{lg} left succesfully")
            input(f'\n{cy} Press enter to exit...')



    elif a == 13:
        # thanks to github.com/th3unkn0n for the snippet below
        print(f'\n{lg}[i] Checking for updates...')
        try:
            version = requests.get('https://raw.githubusercontent.com/msy1717/MemberAdder/main/version.txt')
        except:
            print(f'{r} You are not connected to the internet')
            print(f'{r} Please connect to the internet and retry')
            exit()
        if float(version.text) > 1.1:
            prompt = str(input(f'{lg}[~] Update available[Version {version.text}]. Download?[y/n]: {r}'))
            if prompt == 'y' or prompt == 'yes' or prompt == 'Y':
                print(f'{lg}[i] Downloading updates...')
                if os.name == 'nt':
                    os.system('del main.py')
                    os.system('del setup.py')
                else:
                    os.system('rm main.py')
                    os.system('rm setup.py')
                os.system('curl -l -O https://raw.githubusercontent.com/msy1717/MemberAdder/main/main.py')
                os.system('curl -l -O https://raw.githubusercontent.com/msy1717/MemberAdder/main/setup.py')
                print(f'{lg}[*] Updated to version: {version.text}')
                input('Press enter to exit...')
                exit()
            else:
                print(f'{lg}[!] Update aborted.')
                input('Press enter to goto main menu...')
        else:
            print(f'{lg}[i] Your script is already up to date')
            input('Press enter to goto main menu...')

    elif a == 0:
        clr()
        banner()
        exit()

