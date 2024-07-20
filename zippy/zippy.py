import os
import yt_dlp
import random
import requests
import json

api_key = 'f174e728b77748e08cdfffd339894c41'
base_url = 'https://newsapi.org/v2/top-headlines'

if not os.path.exists('videos'):
    os.makedirs('videos')

GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"
YELLOW = "\033[33m"

def zippy():
    os.system('cls')
    print(' ________  ___  ________  ________  ___    ___ ')
    print('|\_____  \|\  \|\   __  \|\   __  \|\  \  /  /|')
    print(' \|___/  /\ \  \ \  \|\  \ \  \|\  \ \  \/  / /')
    print('     /  / /\ \  \ \   ____\ \   ____\ \    / / ')
    print('    /  /_/__\ \  \ \  \___|\ \  \___|\/  /  /  ')
    print('   |\________\ \__\ \__\    \ \__\ __/  / /    ')
    print('    \|_______|\|__|\|__|     \|__||\___/ /     ')
    print('                                  \|___|/      ')
    print('')
    print(f"{GREEN}[>] {RESET}{BLUE}Created By{RESET}   : ebola-cmd")
    print(f"{GREEN}[>] {RESET}{BLUE}Version{RESET}      : 1.4")
    print('')
    print(f"{YELLOW}[!] Select a Option :{RESET}")
    print('')
    print(f"{GREEN}[0] {RESET}{BLUE}Youtube Downloader")
    print(f"{GREEN}[1] {RESET}{BLUE}To-do List")
    print(f"{GREEN}[2] {RESET}{BLUE}Games")
    print(f"{GREEN}[3] {RESET}{BLUE}News")
    print('')
    
    choice = input(f"{GREEN}[>]{RESET}")
    if choice == "0":
        yt()
        
    if choice == "1":
        todo()
        
    if choice == "2":
        games()
        
    if choice == "3":
        run_news_aggregator()
        
    if choice == "4":
        main()
        
    else:
        input('invalid key')
        zippy()
        
def yt():
    print(f"{YELLOW}[!] Note: Your videos will be downloaded in the 'videos' folder located in the 'zippy' folder :{RESET}")
    print(f"{YELLOW}[!] Note: You might get some error after downloading the video you can ignore it :{RESET}")
    os.chdir('videos')

    video_query = str(input('Search: '))

    # Use yt-dlp to search for videos
    search_result = yt_dlp.YoutubeDL().extract_info(f"ytsearch10:{video_query}", download=False)

    if 'entries' in search_result and search_result['entries']:
        video_titles = [(entry['title'], entry['webpage_url']) for entry in search_result['entries']]

        for j, (title, link) in enumerate(video_titles):
            print(f'{j+1}: {title}')

        n = int(input('Choose the video: '))
        chosen_title, chosen_link = video_titles[n - 1]

        print(f'LINK: {chosen_link}')
        print(f'Downloading {chosen_title}')

        download_choice = input("Do you want to download the video as MP4 or MP3? Enter 'mp4' or 'mp3': ").strip().lower()

        ydl_opts = {}
        if download_choice == 'mp3':
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': '%(title)s.%(ext)s'
            }
        elif download_choice == 'mp4':
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s'
            }
        else:
            input("Invalid choice. Please enter 'mp4' or 'mp3'.")
            zippy()

        # Download the chosen video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([chosen_link])

        input(f'{chosen_title} has been downloaded successfully!')
        zippy()
        
    else:
        input("No videos found.")
        zippy()

def todo():
    tasks = []

    def save_tasks():
        with open('tasks.txt', 'w') as file:
            for task in tasks:
                file.write(f"{task['task']}|{task['done']}\n")

    def load_tasks():
        if os.path.exists('tasks.txt'):
            with open('tasks.txt', 'r') as file:
                for line in file:
                    task_str, done_str = line.strip().split('|')
                    tasks.append({"task": task_str, "done": done_str == 'True'})

    def delete_task(index):
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print(f"{GREEN}Task deleted!{RESET}")
        else:
            print(f"{GREEN}Invalid task number.{RESET}")

    load_tasks()

    while True:
        print("\n===== To-Do List =====")
        print(f"{GREEN}[1]{RESET} Add Task")
        print(f"{GREEN}[2]{RESET} Show Tasks")
        print(f"{GREEN}[3]{RESET} Mark Task as Done")
        print(f"{GREEN}[4]{RESET} Delete Task")
        print(f"{GREEN}[5]{RESET} Exit")

        choice = input(f"{GREEN}[>]{RESET} ")

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add: "))
            
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print(f"{GREEN}Task added!{RESET}")

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{GREEN}{index + 1}. {task['task']} - {status}{RESET}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print(f"{GREEN}Task marked as done!{RESET}")
            else:
                print(f"{GREEN}Invalid task number.{RESET}")

        elif choice == '4':
            task_index = int(input("Enter the task number to delete: ")) - 1
            delete_task(task_index)

        elif choice == '5':
            save_tasks()
            print(f"{GREEN}Tasks saved. Exiting the To-Do List.{RESET}")
            zippy()
            break

        else:
            print(f"{GREEN}Invalid choice. Please try again.{RESET}")

def games():
    os.system('cls')
    print(f"{YELLOW}[!] Please choose which game you want to play :{RESET}")
    print('')
    print(f"{GREEN}[0] {RESET}{BLUE}Football")
    print(f"{GREEN}[1] {RESET}{BLUE}Wordle")
    print('')
    game = input(f"{GREEN}[>]{RESET}")
    if game == "0":
        football()
    
    if game == "1":
        wordlefr()
        
def football():
    coins = 0
    wherebruv_one = 0
    saved_players = []

    def play_game_gamer():
            global coins
            random_number_one = random.randint(1, 3)
            os.system('cls')
            print("                .---------------- _----------------.")
            print("              ,::::::::::::::::::|.|::::::::::::::::::, ")
            print("            .::::::::::::::::::::]^[::::::::::::::::::::. ")
            print("           |.================= ,-|||~\==================.|   ")
            print("           ||:::|:::::::::::::{<|||||>}:::::::::::::|:::|| ")
            print("           ||:::|::::::::::::::\|||||/::::::::::::::|:::||")
            print("           ||:::|::::::::::::::{/   \}::::::::::::::|:::||")
            print("           ||:::|::::::::::::::/__9__\::::::::::::::|:::||")
            print("           ||:::|::::::::::::::| / \ |::::::::::::::|:::||")
            print("           ||:::'              (<   >)              ':::||")
            print("           ||:                _|)   (|_                :||")
            print("___________!!________________(  |   |  )________________!!_____________")
            print("      /                                                       \ ")
            print("     /                                                         \  ")
            print("    /                                                           \ ")
            print("   /_____________________________________________________________\ ")
            print('+-----------------------------------------------------------------------------------------+')
            print('this is the goalie')
            print('he will try to save your shot')
            print('rememeber if u want to shoot left then enter 1, if u want to shoot in the midle enter 2, and if u want to shoot right enter 3')
            print('+-----------------------------------------------------------------------------------------+')
            print('where would u like to shoot [1/2/3]')
            wherebruv_one = input('>')
            wherebruv_one = int(wherebruv_one)
            if random_number_one == wherebruv_one and wherebruv_one == 1:
                print("                .-----------------------------------.")
                print("              ,:::::::::::::::::::::::::::::::::::::::, ")
                print("            .:::::::::::::::::::::::::::::::::::::::::::. ")
                print("           |.========_==================================.|   ")
                print("           ||:::|:::|.|:::::::::::::::::::::::::::::|:::|| ")
                print("           ||:::|::_]^[_::::::::::::::::::::::::::::|:::||")
                print("           ||:::|:/;;;;;\:::::::::::::::::::::::::::|:::||")
                print("           ||:::_<;\;;;/;>_:::::::::::::::::::::::::|:::||")
                print("           ||::(  \;>;<;/  )::::::::::::::::::::::::|:::||")
                print("           ||:::\ \ ___ / /                         ':::||")
                print("           ||:   >|     |<                             :||")
                print("___________!!___(_;     ;_)_____________________________!!_____________")
                print("      /                                                       \ ")
                print("     /                                                         \  ")
                print("    /                                                           \ ")
                print("   /_____________________________________________________________\ ")
                print('+-----------------------------------------------------------------------------------------+')
                print('Oh no the goalie saved your shot')
                print('Do you want to play again? [y/n]')
                play_again = input('>')
                if play_again == 'y':
                    play_game_gamer()
                else:
                    menu()
                
            if random_number_one == wherebruv_one and wherebruv_one == 2:
                print("                .-----------------------------------.")
                print("              ,:::::::::::::::::::::::::::::::::::::::, ")
                print("            .:::::::::::::::::::::::::::::::::::::::::::. ")
                print("           |.=====================_=====================.|   ")
                print("           ||:::|::::::::::::::::|.|::::::::::::::::|:::|| ")
                print("           ||:::|:::::::::::::::_]^[_:::::::::::::::|:::||")
                print("           ||:::|::::::::::::::/;;;;;\::::::::::::::|:::||")
                print("           ||:::|::::::::::::_<;\;;;/;>_::::::::::::|:::||")
                print("           ||:::|:::::::::::(  \;>;<;/  ):::::::::::|:::||")
                print("           ||:::             \ \ ___ / /            ':::||")
                print("           ||:                >|     |<                :||")
                print("___________!!________________(_;     ;_)________________!!_____________")
                print("      /                                                       \ ")
                print("     /                                                         \  ")
                print("    /                                                           \ ")
                print("   /_____________________________________________________________\ ")
                print('+-----------------------------------------------------------------------------------------+')
                print('Oh no the goalie saved your shot')
                input('>')
                print('Do you want to play again? [y/n]')
                play_again = input('>')
                if play_again == 'y':
                    play_game_gamer()
                else:
                    menu()
                
            if random_number_one == wherebruv_one and wherebruv_one == 3:
                print("                .-----------------------------------.")
                print("              ,:::::::::::::::::::::::::::::::::::::::, ")
                print("            .:::::::::::::::::::::::::::::::::::::::::::. ")
                print("           |.==================================_========.|   ")
                print("           ||:::|:::::::::::::::::::::::::::::|.|:::|:::|| ")
                print("           ||:::|::::::::::::::::::::::::::::_]^[_::|:::||")
                print("           ||:::|:::::::::::::::::::::::::::/;;;;;\:|:::||")
                print("           ||:::|:::::::::::::::::::::::::_<;\;;;/;>_:::||")
                print("           ||:::|::::::::::::::::::::::::(  \;>;<;/  )::||")
                print("           ||:::                          \ \ ___ / /:::||")
                print("           ||:                             >|     |<   :||")
                print("___________!!_____________________________(_;     ;_)___!!_____________")
                print("      /                                                       \ ")
                print("     /                                                         \  ")
                print("    /                                                           \ ")
                print("   /_____________________________________________________________\ ")
                print('+-----------------------------------------------------------------------------------------+')
                print('Oh no the goalie saved your shot')
                print('Do you want to play again? [y/n]')
                play_again = input('>')
                if play_again == 'y':
                    play_game_gamer()
                else:
                    menu()
                
            if random_number_one != wherebruv_one and wherebruv_one == 1:
                print("                .-----------------------------------.")
                print("              ,:::::::::::::::::::::::::::::::::::::::, ")
                print("            .:::::::::::::::::::::::::::::::::::::::::::. ")
                print("           |.==================================_========.|   ")
                print("           ||:::|::::___::::::::::::::::::::::|.|:::|:::|| ")
                print("           ||:::|:::/|||\::::::::::::::::::::_]^[_::|:::||")
                print("           ||:::|:::\|||/:::::::::::::::::::/;;;;;\:|:::||")
                print("           ||:::|:::::::::::::::::::::::::_<;\;;;/;>_:::||")
                print("           ||:::|::::::::::::::::::::::::(  \;>;<;/  )::||")
                print("           ||:::                          \ \ ___ / /:::||")
                print("           ||:                             >|     |<   :||")
                print("___________!!_____________________________(_;     ;_)___!!_____________")
                print("      /                                                       \ ")
                print("     /                                                         \  ")
                print("    /                                                           \ ")
                print("   /_____________________________________________________________\ ")
                print('+-----------------------------------------------------------------------------------------+')
                print('Wonderfull u scored')
                print('You earned 5 coins (u can spend them in the pack opener)')
                coins += 5
                print('Do you want to play again? [y/n]') 
                play_again = input('>')
                if play_again == 'y':
                    play_game_gamer()
                else:
                    menu()
                
            if random_number_one != wherebruv_one and wherebruv_one == 3:
                print("                .-----------------------------------.")
                print("              ,:::::::::::::::::::::::::::::::::::::::, ")
                print("            .:::::::::::::::::::::::::::::::::::::::::::. ")
                print("           |.========_==================================.|   ")
                print("           ||:::|:::|.|::::::::::::::::::::::___::::|:::|| ")
                print("           ||:::|::_]^[_::::::::::::::::::::/|||\:::|:::||")
                print("           ||:::|:/;;;;;\:::::::::::::::::::\|||/:::|:::||")
                print("           ||:::_<;\;;;/;>_:::::::::::::::::::::::::|:::||")
                print("           ||::(  \;>;<;/  )::::::::::::::::::::::::|:::||")
                print("           ||:::\ \ ___ / /                         ':::||")
                print("           ||:   >|     |<                             :||")
                print("___________!!___(_;     ;_)_____________________________!!_____________")
                print("      /                                                       \ ")
                print("     /                                                         \  ")
                print("    /                                                           \ ")
                print("   /_____________________________________________________________\ ")
                print('+-----------------------------------------------------------------------------------------+')
                print('Wonderfull u scored')
                print('You earned 5 coins (u can spend them in the pack opener)')
                coins += 5
                print('Do you want to play again? [y/n]')
                play_again = input('>')
                if play_again == 'y':
                    play_game_gamer()
                else:
                    menu()
                        
            if random_number_one != wherebruv_one and wherebruv_one == 2:
                print("                .-----------------------------------.")
                print("              ,:::::::::::::::::::::::::::::::::::::::, ")
                print("            .:::::::::::::::::::::::::::::::::::::::::::. ")
                print("           |.========_==================================.|   ")
                print("           ||:::|:::|.|::::::::::___::::::::::::::::|:::|| ")
                print("           ||:::|::_]^[_::::::::/|||\:::::::::::::::|:::||")
                print("           ||:::|:/;;;;;\:::::::\|||/:::::::::::::::|:::||")
                print("           ||:::_<;\;;;/;>_:::::::::::::::::::::::::|:::||")
                print("           ||::(  \;>;<;/  )::::::::::::::::::::::::|:::||")
                print("           ||:::\ \ ___ / /                         ':::||")
                print("           ||:   >|     |<                             :||")
                print("___________!!___(_;     ;_)_____________________________!!_____________")
                print("      /                                                       \ ")
                print("     /                                                         \  ")
                print("    /                                                           \ ")
                print("   /_____________________________________________________________\ ")
                print('+-----------------------------------------------------------------------------------------+')
                print('Wonderfull u scored')
                print('You earned 5 coins (u can spend them in the pack opener)')
                coins += 5
                print('Do you want to play again? [y/n]') 
                play_again = input('>')
                if play_again == 'y':
                    play_game_gamer()
                else:
                    menu()

    def play_game():
        print("                .-----------------------------------.")
        print("              ,:::::::::::::::::::::::::::::::::::::::, ")
        print("            .:::::::::::::::::::::::::::::::::::::::::::. ")
        print("           |.===========================================.|   ")
        print("           ||:::|:::__::::::::::_____::::::: _____::|:::|| ")
        print("           ||:::|::/  |::::::::/ __  \::::::|____ |:|:::||")
        print("           ||:::|::'| |::::::::`' / /'::::::::::/ /:|:::||")
        print("           ||:::|:::| |::::::::::/ / :::::::::::\ \:|:::||")
        print("           ||:::|::_| |_:::::::./ /__:::::::.___/ /:|:::||")
        print("           ||:::'  \___/       \_____/      \____/  ':::||")
        print("           ||:                                         :||")
        print("___________!!___________________________________________!!_____________")
        print("      /                                                       \ ")
        print("     /                                                         \  ")
        print("    /                                                           \ ")
        print("   /_____________________________________________________________\ ")
        print('+-----------------------------------------------------------------------------------------+')
        print('Welcome to the game!')
        print('this game is extremly easy to play')
        print('all you have to do is shoot the ball into the goal')
        print('u can choose where to shoot the ball by entering the number 1, 2 or 3')
        print('and a goalkeeper will try to save it')
        print('are you ready? [y/n]')
        print('+-----------------------------------------------------------------------------------------+')
        play_game_gamer()
        

    def intro():
        global wherebruv_one
        global coins
        coins = 0
        os.system('cls')
        print('  __            _   _           _ _ ')
        print(' / _|          | | | |         | | |')
        print('| |_ ___   ___ | |_| |__   __ _| | |')
        print("|  _/ _ \ / _ \| __| '_ \ / _` | | |")
        print('| || (_) | (_) | |_| |_) | (_| | | |')
        print('|_| \___/ \___/ \__|_.__/ \__,_|_|_|')
        print('+-----------------------------------------------------------------------------------------+')
        input('>')
        menu()

    def menu():
        os.system('cls')
        print('  __            _   _           _ _ ')
        print(' / _|          | | | |         | | |')
        print('| |_ ___   ___ | |_| |__   __ _| | |')
        print("|  _/ _ \ / _ \| __| '_ \ / _` | | |")
        print('| || (_) | (_) | |_| |_) | (_| | | |')
        print('|_| \___/ \___/ \__|_.__/ \__,_|_|_|')
        print('+-----------------------------------------------------------------------------------------+')
        print('1. Penalty kicks (main gamemode)')
        print('2. Pack opener (open packs with the money you earn by playing penalty kicks)')
        print('3. Your cards (your players which u packed)')
        print('4. Balance (ur current balance)')
        print('5. Exit')
        print('+-----------------------------------------------------------------------------------------+')
        menu_choice = input('>')
        if menu_choice == "1":
            play_game()
            
        if menu_choice == "2":
            pack_opener()
            
        if menu_choice == "3":
            show_saved_players(saved_players)
            
        if menu_choice == "4":
            balance()
            
        if menu_choice == "5":
            zippy()
            
    def save_player(rating, player, saved_players):
        print('Would you like to save this player? (y/n)')
        save_choice = input('>')
        if save_choice.lower() == 'y':
            saved_players.append({'rating': rating, 'player': player})
            print('Player saved!')
            menu()
        else:
            print('Player not saved.')
            menu()

    def pack_opener():
        global coins
        players = ['Lionel Messi', 'Kylian Mbappé', 'Karim Benzema', 'Erling Haaland', 'Luka Modric', 'Kevin De Bruyne', 'Robert Lewandowski', 'Vinícius Júnior', 'Thibaut Courtois', 'Mohamed Salah', 'Sadio Mané', 'Neymar', 'Harry Kane', 'Jude Bellingham', 'Casemiro', 'Achraf Hakimi', 'Antoine Griezmann', 'Federico Valverde', 'Pedri', 'Emiliano Martínez', 'Enzo Fernández', 'Bukayo', 'Saka', 'Rafael Leão', 'Phil Foden', 'Jamal Musiala', 'Son', 'Virgil van Dijk', 'Bruno Fernandes', 'Bernardo Silva', 'Olivier Giroud', 'Cristiano Ronaldo']
        rating_ranges = {'1': (60, 70), '2': (70, 80), '3': (80, 90), '4': (90, 100)}
        random_player = random.choice(players)
        print('                  _    ')
        print('                 | |   ')
        print(' _ __   __ _  ___| | __          ___  _ __   ___ _ __   ___ _ __ ')
        print("| '_ \ / _` |/ __| |/ /         / _ \| '_ \ / _ \ '_ \ / _ \ '__|")
        print("| |_) | (_| | (__|   <         | (_) | |_) |  __/ | | |  __/ |   ")
        print("| .__/ \__,_|\___|_|\_\         \___/| .__/ \___|_| |_|\___|_|")
        print("| |                                  | |")
        print("|_|                                  |_|")
        print('+-----------------------------------------------------------------------------------------+')
        print('1. 20 coins for 60 - 70 rated player pack')
        print('2. 30 coins for 70 - 80 rated player pack')
        print('3. 50 coins for 80 - 90 rated player pack')
        print('4. 100 coins for 90 - 100 rated player pack')
        print('+-----------------------------------------------------------------------------------------+')
        pack_choice = input('>')
        if pack_choice:
            rating_range = rating_ranges[pack_choice]
            random_rating = random.randint(rating_range[0], rating_range[1])
            
            pack_cost = 0
            if pack_choice == '1':
                pack_cost = 20
            elif pack_choice == '2':
                pack_cost = 30
            elif pack_choice == '3':
                pack_cost = 50
            elif pack_choice == '4':
                pack_cost = 1
                
            
            if coins < pack_cost:
                print("You don't have enough coins to buy this pack.")
            if coins > pack_cost:
                random_rating = random.randint(rating_range[0], rating_range[1])
                
                # Deduct coins based on the chosen pack
                coins -= pack_cost
                
                print(f'You packed {random_rating} rated {random_player}')
                save_player(random_rating, random_player, saved_players)
        else: 
            print('Invalid choice. Please choose a valid pack.')

            input('Press Enter to go back to the menu...')
        
    def show_saved_players(saved_players):
        os.system('cls')
        if not saved_players:
            print('No players saved.')
        else:
            display_limit = 5  # Adjust this number based on your preference
            for index, saved_player in enumerate(saved_players[:display_limit], start=1):
                print(f"{index}. {saved_player['rating']} rated {saved_player['player']}")
            
            if len(saved_players) > display_limit:
                print(f"... and {len(saved_players) - display_limit} more. Type 'more' to view all.")
                choice = input('>')
                if choice.lower() == 'more':
                    for index, saved_player in enumerate(saved_players[display_limit:], start=display_limit + 1):
                        print(f"{index}. {saved_player['rating']} rated {saved_player['player']}")

        input('Press Enter to go back to the menu...')
        menu()


    def balance():
        global coins
        os.system('cls')
        print(' _           _                      ')
        print('| |         | |                     ')
        print("| |__   __ _| | __ _ _ __   ___ ___ ")
        print("| '_ \ / _` | |/ _` | '_ \ / __/ _ \'")
        print('| |_| | (_| | | (_| | | | | (_|  __/')
        print('|_.__/ \__,_|_|\__,_|_| |_|\___\___|')
        print('+-----------------------------------------------------------------------------------------+')
        print('your balance is')
        print(coins)
        input('>')
        menu()
        
    intro()

def wordlefr():
    import os
    import random

    words = [
        "Apple", "Bread", "Chase", "Dream", "Eagle", "Flame", "Grace",
        "Heart", "Ivory", "Jewel", "Knife", "Light", "Maple", "North",
        "Olive", "Peace", "Quest", "River", "Stone", "Trust"
    ]

    target_word = random.choice(words)

    def get_feedback(guess, target):
        feedback = []
        for i in range(len(guess)):
            if guess[i] == target[i]:
                feedback.append(f'\033[92m{guess[i]}\033[0m')  # Green for correct letter in the correct position
            elif guess[i] in target:
                feedback.append(f'\033[33m{guess[i]}\033[0m')
            else:
                feedback.append(f'\033[91m{guess[i]}\033[0m')  # Red for incorrect letter
        return ''.join(feedback)


    def wordle():
        os.system('cls')
        print(' ___       __   ________  ________  ________  ___       _______      ')
        print('|\  \     |\  \|\   __  \|\   __  \|\   ___ \|\  \     |\  ___ \     ')
        print('\ \  \    \ \  \ \  \|\  \ \  \|\  \ \  \_|\ \ \  \    \ \   __/|    ')
        print(' \ \  \  __\ \  \ \  \ \  \ \   _  _\ \  \ \  \ \  \    \ \  \_|/__  ')
        print('  \ \  \|\__\_\  \ \  \ \  \ \   \   \ \  \_ \ \ \  \____\ \  \_|\ \ ')
        print('   \ \____________\ \_______\ \__\  _ \ \_______\ \_______\ \_______')
        print('    \|____________|\|_______|\|__|\|__|\|_______|\|_______|\|_______|')
        print('')
        print('[>] Created By   : ebola-cmd')
        print('[>] Version      : 1.0')
        print('')
        print('[!] What do you want to do? :')
        print('')
        print('[1] Play')
        print('[2] Tutorial')
        print('[3] Exit')
        c_1 = input('[>] ')
        if c_1 == "1":
            game()
            
        if c_1 == "2":
            tutorial()
            
        if c_1 == "3":
            exit()
            
    def game():
        os.system('cls')
        attempts = 6
        print('[!] Enter a 5-letter word')
        for attempt in range(1, attempts + 1):
            guess = input(f"[{attempt}] ").lower()
            
            if len(guess) != 5:
                print("Please enter a 5-letter word.")
                continue
            
            feedback = get_feedback(guess, target_word)
            print('[>]', feedback)
            
            if guess == target_word:
                input("Congratulations! You've guessed the word!")
                wordle()
            
        input(f"Sorry, you've used all your attempts. The word was: {target_word}")
        wordle()
        
    def tutorial():
        os.system('cls')
        print('[!] How to play')
        print('[!] Guess the word in 6 tries')
        print('[>] Each guess must be a valid 5-letter word.')
        print('[>] The color of the tiles will change to show how close your guess was to the word.')
        print('')
        print('[Examples:]')
        print('\033[92mW\033[0mEARY')
        print('W is in the word and in the correct spot.')
        print('')
        print('P\033[93mI\033[0mLLS')
        print('I is in the word but in the wrong spot.')
        print('')
        print('VAGUE')
        print('No letter is in the word')
        print('')
        print('press any key...')
        input('[>]')
        wordle()
        
    def exit():
        print('See you some other time...')
        zippy()
        
    wordle()
    
def fetch_news(category=None, query=None):
    params = {
        'apiKey': api_key,
        'category': category,
        'q': query,
        'pageSize': 5  # Number of headlines to fetch
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        news_data = response.json()
        if news_data['status'] == 'ok':
            return news_data['articles']
        else:
            print(f"Error: {news_data['message']}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return []

def display_news(articles):
    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   Published At: {article['publishedAt']}")
        print(f"   URL: {article['url']}")
        print()

def get_user_choice():
    print("Select the type of news you want:")
    print(f"{GREEN}[1] {RESET}{BLUE}World")
    print(f"{GREEN}[2] {RESET}{BLUE}Sports")
    choice = input(f"{GREEN}[>]{RESET}")
    return choice

def get_sport_choice():
    print("Select the sport news you want:")
    print(f"{GREEN}[1] {RESET}{BLUE}Cricket")
    print(f"{GREEN}[2] {RESET}{BLUE}Soccer")
    print(f"{GREEN}[3] {RESET}{BLUE}Basketball")
    choice = input(f"{GREEN}[>]{RESET}")
    return choice

def run_news_aggregator():
    user_choice = get_user_choice()
    if user_choice == '1':
        category = 'general'
        query = None
    elif user_choice == '2':
        category = 'sports'
        sport_choice = get_sport_choice()
        if sport_choice == '1':
            query = 'cricket'
        elif sport_choice == '2':
            query = 'soccer'
        elif sport_choice == '3':
            query = 'basketball'
        else:
            print("Invalid choice. Defaulting to general sports news.")
            query = None
    else:
        print("Invalid choice. Defaulting to world news.")
        category = 'general'
        query = None

    headlines = fetch_news(category=category, query=query)
    display_news(headlines)
    
    input('press any key to continue...')
    
    zippy()

# Function to load data from a file
def load_data(filename="fitness_data.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"workouts": [], "points": 0, "level": 1}

# Function to save data to a file
def save_data(data, filename="fitness_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Function to calculate points for a workout
def calculate_points(sets, reps, weight):
    return sets * reps * weight // 100 # Adjust this formula as needed

# Function to add a workout entry
def add_workout(data):
    date = input(f"{YELLOW}[!] Enter the date (YYYY-MM-DD) :{RESET} ")
    exercise = input(f"{YELLOW}[!] Enter the exercise name :{RESET} ")
    sets = int(input(f"{YELLOW}[!] Enter the number of sets :{RESET} "))
    reps = int(input(f"{YELLOW}[!] Enter the number of reps per set :{RESET} "))
    weight = float(input(f"{YELLOW}[!] Enter the weight used (in kg) :{RESET} "))

    points = calculate_points(sets, reps, weight)
    data["points"] += points

    workout = {
        "date": date,
        "exercise": exercise,
        "sets": sets,
        "reps": reps,
        "weight": weight,
        "points": points
    }
    data["workouts"].append(workout)
    save_data(data)
    print(f"Workout added successfully. You earned {points} points.")

    check_level_up(data)

# Function to view all workouts
def view_workouts(data):
    if not data["workouts"]:
        print("No workouts found.")
    else:
        for workout in data["workouts"]:
            print(f"Date: {workout['date']}, Exercise: {workout['exercise']}, Sets: {workout['sets']}, Reps: {workout['reps']}, Weight: {workout['weight']} kg, Points: {workout['points']}")

    print(f"\nTotal Points: {data['points']}")
    print(f"Current Level: {data['level']}")

# Function to check and handle leveling up
def check_level_up(data):
    level_thresholds = {1: 100, 2: 300, 3: 600, 4: 1000} # Example thresholds

    current_level = data["level"]
    points_needed = level_thresholds.get(current_level, float('inf'))

    if data["points"] >= points_needed:
        data["level"] += 1
        save_data(data)
        print(f"Congratulations! You've leveled up to Level {data['level']}.")

# Function to display the main menu and handle user input
def main():
    data = load_data()

    while True:
        print("\n===== Fitness Tracker =====")
        print(f"{YELLOW}[!] Select a Option :{RESET}")
        print('')
        print(f"{GREEN}[1] {RESET}{BLUE}Add Workout{RESET}")
        print(f"{GREEN}[2] {RESET}{BLUE}View Workoutt{RESET}")
        print(f"{GREEN}[3] {RESET}{BLUE}Exit{RESET}")
        choice = input(f"{GREEN}[>]{RESET}")

        if choice == "1":
            add_workout(data)
        elif choice == "2":
            view_workouts(data)
        elif choice == "3":
            print("Exiting...")
            zippy()
            break
        else:
            print("Invalid choice. Please try again.")


zippy()