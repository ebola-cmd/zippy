import os
import yt_dlp
import random
import requests
import json
import datetime

api_key = 'f174e728b77748e08cdfffd339894c41'
base_url = 'https://newsapi.org/v2/top-headlines'

if not os.path.exists('videos'):
    os.makedirs('videos')

GREEN = "\033[32m"
BLUE = "\033[36m"
RESET = "\033[0m"
YELLOW = "\033[33m"
RED = '\033[91m'

def zippy():
    os.system('cls')
    print('███████╗██╗██████╗ ██████╗ ██╗   ██╗')
    print('╚══███╔╝██║██╔══██╗██╔══██╗╚██╗ ██╔╝')
    print('╚══███╔╝██║██╔══██╗██╔══██╗╚██╗ ██╔╝')
    print('  ███╔╝ ██║██████╔╝██████╔╝ ╚████╔╝ ')
    print(' ███╔╝  ██║██╔═══╝ ██╔═══╝   ╚██╔╝  ')
    print('███████╗██║██║     ██║        ██║   ')
    print('╚══════╝╚═╝╚═╝     ╚═╝        ╚═╝   ')
    print('')
    print(f"{GREEN}[>] {RESET}{BLUE}Created By{RESET}   : ebola-cmd")
    print(f"{GREEN}[>] {RESET}{BLUE}Version{RESET}      : 1.5")
    print('')
    print(f"{YELLOW}[!] Select a Option :{RESET}")
    print('')
    print(f"{GREEN}[0] {RESET}{BLUE}Youtube Downloader")
    print(f"{GREEN}[1] {RESET}{BLUE}To-do List")
    print(f"{GREEN}[2] {RESET}{BLUE}Games")
    print(f"{GREEN}[3] {RESET}{BLUE}News")
    print(f"{GREEN}[4] {RESET}{BLUE}Fitness Tracker")
    print(f"{GREEN}[5] {RESET}{BLUE}Flashcards")
    print(f"{GREEN}[6] {RESET}{BLUE}Habit Tracker")
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
        
    if choice == "5":
        flashcards()
        
    if choice == "6":
        habit()
        
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
    print(f"{GREEN}[2] {RESET}{BLUE}BlackJack")
    print('')
    game = input(f"{GREEN}[>]{RESET}")
    if game == "0":
        football()
    
    if game == "1":
        wordlefr()
    
    if game == "2":
        blackjack()
        
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

def blackjack():
    # Suits and values
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # ASCII art for cards
    cards_art = {
        'Hearts': {
            '2': [
                " _____ ",
                "|2    |",
                "|  ♥  |",
                "|    2|",
                " ¯¯¯¯ "
            ],
            '3': [
                " _____ ",
                "|3    |",
                "|  ♥  |",
                "|  ♥  |",
                " ¯¯¯¯ "
            ],
            '4': [
                " _____ ",
                "|4    |",
                "| ♥ ♥ |",
                "| ♥ ♥ |",
                " ¯¯¯¯ "
            ],
            '5': [
                " _____ ",
                "|5    |",
                "| ♥ ♥ |",
                "|  ♥  |",
                " ¯¯¯¯ "
            ],
            '6': [
                " _____ ",
                "|6    |",
                "| ♥ ♥ |",
                "| ♥ ♥ |",
                " ¯¯¯¯ "
            ],
            '7': [
                " _____ ",
                "|7    |",
                "| ♥ ♥ |",
                "| ♥ ♥ |",
                " ¯¯¯¯ "
            ],
            '8': [
                " _____ ",
                "|8    |",
                "| ♥ ♥ |",
                "| ♥ ♥ |",
                " ¯¯¯¯ "
            ],
            '9': [
                " _____ ",
                "|9    |",
                "| ♥ ♥ |",
                "| ♥ ♥ |",
                " ¯¯¯¯ "
            ],
            '10': [
                " _____ ",
                "|10   |",
                "| ♥ ♥ |",
                "| ♥ ♥ |",
                " ¯¯¯¯ "
            ],
            'J': [
                " _____ ",
                "|J    |",
                "| ♥ ♥ |",
                "| ♥ ♥ |",
                " ¯¯¯¯ "
            ],
            'Q': [
                " _____ ",
                "|Q    |",
                "| ♥ ♥ |",
                "| ♥ ♥ |",
                " ¯¯¯¯ "
            ],
            'K': [
                " _____ ",
                "|K    |",
                "| ♥ ♥ |",
                "| ♥ ♥ |",
                " ¯¯¯¯ "
            ],
            'A': [
                " _____ ",
                "|A    |",
                "| ♥ ♥ |",
                "| ♥ ♥ |",
                " ¯¯¯¯ "
            ],
        },
        'Diamonds': {
            '2': [
                " _____ ",
                "|2    |",
                "|  ♦  |",
                "|    2|",
                " ¯¯¯¯ "
            ],
            '3': [
                " _____ ",
                "|3    |",
                "|  ♦  |",
                "|  ♦  |",
                " ¯¯¯¯ "
            ],
            '4': [
                " _____ ",
                "|4    |",
                "| ♦ ♦ |",
                "| ♦ ♦ |",
                " ¯¯¯¯ "
            ],
            '5': [
                " _____ ",
                "|5    |",
                "| ♦ ♦ |",
                "|  ♦  |",
                " ¯¯¯¯ "
            ],
            '6': [
                " _____ ",
                "|6    |",
                "| ♦ ♦ |",
                "| ♦ ♦ |",
                " ¯¯¯¯ "
            ],
            '7': [
                " _____ ",
                "|7    |",
                "| ♦ ♦ |",
                "| ♦ ♦ |",
                " ¯¯¯¯ "
            ],
            '8': [
                " _____ ",
                "|8    |",
                "| ♦ ♦ |",
                "| ♦ ♦ |",
                " ¯¯¯¯ "
            ],
            '9': [
                " _____ ",
                "|9    |",
                "| ♦ ♦ |",
                "| ♦ ♦ |",
                " ¯¯¯¯ "
            ],
            '10': [
                " _____ ",
                "|10   |",
                "| ♦ ♦ |",
                "| ♦ ♦ |",
                " ¯¯¯¯ "
            ],
            'J': [
                " _____ ",
                "|J    |",
                "| ♦ ♦ |",
                "| ♦ ♦ |",
                " ¯¯¯¯ "
            ],
            'Q': [
                " _____ ",
                "|Q    |",
                "| ♦ ♦ |",
                "| ♦ ♦ |",
                " ¯¯¯¯ "
            ],
            'K': [
                " _____ ",
                "|K    |",
                "| ♦ ♦ |",
                "| ♦ ♦ |",
                " ¯¯¯¯ "
            ],
            'A': [
                " _____ ",
                "|A    |",
                "| ♦ ♦ |",
                "| ♦ ♦ |",
                " ¯¯¯¯ "
            ],
        },
        'Clubs': {
            '2': [
                " _____ ",
                "|2    |",
                "|  ♣  |",
                "|    2|",
                " ¯¯¯¯ "
            ],
            '3': [
                " _____ ",
                "|3    |",
                "|  ♣  |",
                "|  ♣  |",
                " ¯¯¯¯ "
            ],
            '4': [
                " _____ ",
                "|4    |",
                "| ♣ ♣ |",
                "| ♣ ♣ |",
                " ¯¯¯¯ "
            ],
            '5': [
                " _____ ",
                "|5    |",
                "| ♣ ♣ |",
                "|  ♣  |",
                " ¯¯¯¯ "
            ],
            '6': [
                " _____ ",
                "|6    |",
                "| ♣ ♣ |",
                "| ♣ ♣ |",
                " ¯¯¯¯ "
            ],
            '7': [
                " _____ ",
                "|7    |",
                "| ♣ ♣ |",
                "| ♣ ♣ |",
                " ¯¯¯¯ "
            ],
            '8': [
                " _____ ",
                "|8    |",
                "| ♣ ♣ |",
                "| ♣ ♣ |",
                " ¯¯¯¯ "
            ],
            '9': [
                " _____ ",
                "|9    |",
                "| ♣ ♣ |",
                "| ♣ ♣ |",
                " ¯¯¯¯ "
            ],
            '10': [
                " _____ ",
                "|10   |",
                "| ♣ ♣ |",
                "| ♣ ♣ |",
                " ¯¯¯¯ "
            ],
            'J': [
                " _____ ",
                "|J    |",
                "| ♣ ♣ |",
                "| ♣ ♣ |",
                " ¯¯¯¯ "
            ],
            'Q': [
                " _____ ",
                "|Q    |",
                "| ♣ ♣ |",
                "| ♣ ♣ |",
                " ¯¯¯¯ "
            ],
            'K': [
                " _____ ",
                "|K    |",
                "| ♣ ♣ |",
                "| ♣ ♣ |",
                " ¯¯¯¯ "
            ],
            'A': [
                " _____ ",
                "|A    |",
                "| ♣ ♣ |",
                "| ♣ ♣ |",
                " ¯¯¯¯ "
            ],
        },
        'Spades': {
            '2': [
                " _____ ",
                "|2    |",
                "|  ♠  |",
                "|    2|",
                " ¯¯¯¯ "
            ],
            '3': [
                " _____ ",
                "|3    |",
                "|  ♠  |",
                "|  ♠  |",
                " ¯¯¯¯ "
            ],
            '4': [
                " _____ ",
                "|4    |",
                "| ♠ ♠ |",
                "| ♠ ♠ |",
                " ¯¯¯¯ "
            ],
            '5': [
                " _____ ",
                "|5    |",
                "| ♠ ♠ |",
                "|  ♠  |",
                " ¯¯¯¯ "
            ],
            '6': [
                " _____ ",
                "|6    |",
                "| ♠ ♠ |",
                "| ♠ ♠ |",
                " ¯¯¯¯ "
            ],
            '7': [
                " _____ ",
                "|7    |",
                "| ♠ ♠ |",
                "| ♠ ♠ |",
                " ¯¯¯¯ "
            ],
            '8': [
                " _____ ",
                "|8    |",
                "| ♠ ♠ |",
                "| ♠ ♠ |",
                " ¯¯¯¯ "
            ],
            '9': [
                " _____ ",
                "|9    |",
                "| ♠ ♠ |",
                "| ♠ ♠ |",
                " ¯¯¯¯ "
            ],
            '10': [
                " _____ ",
                "|10   |",
                "| ♠ ♠ |",
                "| ♠ ♠ |",
                " ¯¯¯¯ "
            ],
            'J': [
                " _____ ",
                "|J    |",
                "| ♠ ♠ |",
                "| ♠ ♠ |",
                " ¯¯¯¯ "
            ],
            'Q': [
                " _____ ",
                "|Q    |",
                "| ♠ ♠ |",
                "| ♠ ♠ |",
                " ¯¯¯¯ "
            ],
            'K': [
                " _____ ",
                "|K    |",
                "| ♠ ♠ |",
                "| ♠ ♠ |",
                " ¯¯¯¯ "
            ],
            'A': [
                " _____ ",
                "|A    |",
                "| ♠ ♠ |",
                "| ♠ ♠ |",
                " ¯¯¯¯ "
            ],
        }
    }

    def display_card(card):
        suit, value = card
        art = cards_art[suit][value]
        for line in art:
            print(line)

    def deal_card():
        suit = random.choice(suits)
        value = random.choice(values)
        return (suit, value)

    def calculate_hand_value(hand):
        value = 0
        num_aces = 0
        for card in hand:
            _, rank = card
            if rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                num_aces += 1
                value += 11
            else:
                value += int(rank)
        
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value

    def print_hand(hand, title="Hand"):
        print(f"\n{title}:")
        for card in hand:
            display_card(card)
        print(f"Value: {calculate_hand_value(hand)}")

    def print_intro():
        os.system('cls' if os.name == 'nt' else 'clear')
        print('.------.            _     _            _    _            _    ')
        print('|A_  _ |.          | |   | |          | |  (_)          | |   ')
        print('|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __')
        print("| \  /|K /\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /")
        print('|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < ')
        print('`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\_|\\__,_|\\___|_|\\_\\\\')
        print('      |  \\/ K|                            _/ |                ')
        print('      `------`                           |__/                 \n')
        print(GREEN + "Let's play some Blackjack!" + RESET)
        print(YELLOW + "1) Start Game" + RESET)
        print(YELLOW + "2) View Tutorial" + RESET)
        print(YELLOW + "3) Quit" + RESET)
        
    def print_tutorial():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(GREEN + "Blackjack Tutorial" + RESET)
        print("""
        Welcome to Blackjack!

        The goal of Blackjack is to get a hand value as close to 21 as possible without going over.

        **Card Values:**
        - Number cards (2-10) are worth their face value.
        - Face cards (J, Q, K) are each worth 10 points.
        - Aces can be worth 1 or 11 points, whichever is more beneficial.

        **Gameplay:**
        - You start with two cards, and the dealer also gets two cards (one face-up, one face-down).
        - You can choose to 'Hit' (get another card) or 'Stand' (keep your current hand).
        - If your hand value exceeds 21, you 'bust' and lose the game.
        - The dealer must hit until their hand value is at least 17.
        - If you have a higher hand value than the dealer without busting, you win. If the dealer busts, you also win.

        **Commands:**
        - Press 'H' to Hit.
        - Press 'S' to Stand.
        - To quit the game, press 'Q' at any time.

        Good luck, and may the best hand win!
        """)
        input("\nPress Enter to return to the main menu...")


    while True:
        print_intro()
        choice = input("Enter your choice (1,2 or 3): ")
        if choice == '1':
            player_hand = [deal_card(), deal_card()]
            dealer_hand = [deal_card(), deal_card()]

            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(GREEN + "Your Turn" + RESET)
                print_hand(player_hand)
                print(RED + "\nDealer's Face-Up Card:" + RESET)
                display_card(dealer_hand[0])
                
                action = input("\nDo you want to (H)it or (S)tand? ").lower()
                if action == 'h':
                    player_hand.append(deal_card())
                    if calculate_hand_value(player_hand) > 21:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print_hand(player_hand, "Busted Hand")
                        print(RED + "You busted! Dealer wins." + RESET)
                        break
                elif action == 's':
                    break
                else:
                    print(RED + "Invalid choice! Please enter H or S." + RESET)
            
            if calculate_hand_value(player_hand) <= 21:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nDealer's Turn")
                print_hand(dealer_hand)
                while calculate_hand_value(dealer_hand) < 17:
                    dealer_hand.append(deal_card())
                    print_hand(dealer_hand)
                
                player_value = calculate_hand_value(player_hand)
                dealer_value = calculate_hand_value(dealer_hand)
                
                if dealer_value > 21 or player_value > dealer_value:
                    print(GREEN + "You win!" + RESET)
                elif player_value < dealer_value:
                    print(RED + "Dealer wins!" + RESET)
                else:
                    print(YELLOW + "It's a tie!" + RESET)
            
            input("\nPress Enter to return to the main menu...")
              
        elif choice == '2':
            print_tutorial()
        elif choice == '3':
            print(GREEN + "Thanks for playing!" + RESET)
            break
        else:
            print(RED + "Invalid choice! Please enter 1 or 2." + RESET)

 
#News
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

#Fitness Tracker
def load_data(filename="fitness_data.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"workouts": [], "points": 0, "level": 1}
def save_data(data, filename="fitness_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
def calculate_points(sets, reps, weight):
    return sets * reps * weight // 100 # Adjust this formula as needed
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
def view_workouts(data):
    if not data["workouts"]:
        print("No workouts found.")
    else:
        for workout in data["workouts"]:
            print(f"Date: {workout['date']}, Exercise: {workout['exercise']}, Sets: {workout['sets']}, Reps: {workout['reps']}, Weight: {workout['weight']} kg, Points: {workout['points']}")

    print(f"\nTotal Points: {data['points']}")
    print(f"Current Level: {data['level']}")
def check_level_up(data):
    level_thresholds = {1: 100, 2: 300, 3: 600, 4: 1000} # Example thresholds

    current_level = data["level"]
    points_needed = level_thresholds.get(current_level, float('inf'))

    if data["points"] >= points_needed:
        data["level"] += 1
        save_data(data)
        print(f"Congratulations! You've leveled up to Level {data['level']}.")
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

def flashcards():
    def load_flashcards(filename):
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            return []
        with open(filename, 'r') as file:
            lines = file.read().strip().split('\n')
            flashcards = []
            for i in range(0, len(lines), 3):
                if i+1 < len(lines):
                    question = lines[i]
                    answer = lines[i+1]
                    flashcards.append({"question": question, "answer": answer})
            return flashcards

    def save_flashcards(filename, flashcards):
        with open(filename, 'w') as file:
            for flashcard in flashcards:
                file.write(f"{flashcard['question']}\n")
                file.write(f"{flashcard['answer']}\n")
                file.write("\n")

    def display_question(flashcard):
        print(f"{BLUE}Question: {RESET}{flashcard['question']}")

    def check_answer(flashcard, user_answer):
        return flashcard["answer"].lower() == user_answer.lower()

    def add_flashcard(flashcards):
        question = input(f"{YELLOW}Enter the question: {RESET}")
        answer = input(f"{YELLOW}Enter the answer: {RESET}")
        flashcards.append({"question": question, "answer": answer})

    def print_menu():
        print("\n===== Flashcard App =====")
        print(f"{YELLOW}[!] Select a Option :{RESET}")
        print('')
        print(f"{GREEN}[1] {RESET}{BLUE}Practice Flashcards{RESET}")
        print(f"{GREEN}[2] {RESET}{BLUE}Add a New Flashcard{RESET}")
        print(f"{GREEN}[3] {RESET}{BLUE}Quit{RESET}")

    def main():
        flashcards = load_flashcards('flashcards.txt')
        
        while True:
            print_menu()
            choice = input(f"{GREEN}[>]{RESET} ")
            
            if choice == '1':
                if not flashcards:
                    print(f"{RED}No flashcards are available. Please add some flashcards first.{RESET}")
                else:
                    random.shuffle(flashcards)
                    score = 0
                    for flashcard in flashcards:
                        display_question(flashcard)
                        user_answer = input(f"{YELLOW}Your answer: {RESET}")
                        if check_answer(flashcard, user_answer):
                            print(f"{GREEN}Correct!{RESET}")
                            score += 1
                        else:
                            print(f"{RED}Wrong. The correct answer is {flashcard['answer']}{RESET}")
                    print(f"{BLUE}Your final score is {score}/{len(flashcards)}{RESET}")
            
            elif choice == '2':
                add_flashcard(flashcards)
            
            elif choice == '3':
                save_flashcards('flashcards.txt', flashcards)
                zippy()
                break
            
            else:
                print(f"{RED}Invalid choice. Please try again.{RESET}")

    if __name__ == "__main__":
        main()
        
def habit():
    def progress_bar(percentage, bar_length=20):
        bar_fill = '█'
        bar_empty = '░'
        filled_length = int(bar_length * percentage // 100)
        bar = bar_fill * filled_length + bar_empty * (bar_length - filled_length)
        return f"[{bar}] {percentage}%"

    HABIT_FILE = "habits.json"

    # Load habits from file
    def load_habits():
        if os.path.exists(HABIT_FILE):
            with open(HABIT_FILE, 'r') as file:
                return json.load(file)
        else:
            return {}

    # Save habits to file
    def save_habits(habits):
        with open(HABIT_FILE, 'w') as file:
            json.dump(habits, file, indent=4)

    # Initialize habits
    habits = load_habits()

    # Update habit completion
    def mark_habit_done(habit):
        today = datetime.date.today().strftime("%Y-%m-%d")
        if habit in habits:
            if today not in habits[habit]["dates"]:
                habits[habit]["dates"].append(today)
                habits[habit]["streak"] += 1

    # Add a new habit
    def add_habit(habit):
        if habit not in habits:
            habits[habit] = {"dates": [], "streak": 0}

    # Remove an existing habit
    def remove_habit(habit):
        if habit in habits:
            del habits[habit]

    # Create a progress bar
    def progress_bar(percentage, bar_length=20):
        bar_fill = '█'
        bar_empty = '░'
        filled_length = int(bar_length * percentage // 100)
        bar = bar_fill * filled_length + bar_empty * (bar_length - filled_length)
        return f"[{bar}] {percentage}%"

    # Display the habit tracker
    def display_habits():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("+----------------------------------------------------------------------------------------------------+")
        print("|                                           Habit Tracker                                            |")
        print("+----------------------------------------------------------------------------------------------------+")
        print("| Habit Name                   | Status Today     | Streak  | Progress                               |")
        print("+----------------------------------------------------------------------------------------------------+")
        
        today = datetime.date.today().strftime("%Y-%m-%d")
        
        for habit, data in habits.items():
            status = "Done" if today in data["dates"] else "Not Done"
            streak = data["streak"]
            progress = progress_bar(streak * 10)  # Example: each streak point equals 10%
            print(f"| {habit.ljust(28)} | {status.ljust(16)} | {str(streak).ljust(6)} | {progress.ljust(14)} |")
        
        print("+---------------------------------------------------------------------------------------------------+")

    # Display the main menu
    def main_menu():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(' ___  ___  ________  ________  ___  _________        _________  ________  ________  ________  ___  __    _______   ________     ')
        print('|\  \|\  \|\   __  \|\   __  \|\  \|\___   ___\     |\___   ___\\   __  \|\   __  \|\   ____\|\  \|\  \ |\  ___ \ |\   __  \    ')
        print('\ \  \\\  \ \  \|\  \ \  \|\ /\ \  \|___ \  \_|     \|___ \  \_\ \  \|\  \ \  \|\  \ \  \___|\ \  \/  /|\ \   __/|\ \  \|\  \   ')
        print(' \ \   __  \ \   __  \ \   __  \ \  \   \ \  \           \ \  \ \ \   _  _\ \   __  \ \  \    \ \   ___  \ \  \_|/_\ \   _  _\  ')
        print('  \ \  \ \  \ \  \ \  \ \  \|\  \ \  \   \ \  \           \ \  \ \ \  \\  \\ \  \ \  \ \  \____\ \  \\ \  \ \  \_|\ \ \  \\  \| ')
        print('   \ \__\ \__\ \__\ \__\ \_______\ \__\   \ \__\           \ \__\ \ \__\\ _\\ \__\ \__\ \_______\ \__\\ \__\ \_______\ \__\\ _\ ')
        print('    \|__|\|__|\|__|\|__|\|_______|\|__|    \|__|            \|__|  \|__|\|__|\|__|\|__|\|_______|\|__| \|__|\|_______|\|__|\|__|')
        print('')
        print(f"{YELLOW}[!] Select a Option :{RESET}")
        print('')
        print(f"{GREEN}[0]{RESET} {BLUE}View Habits{RESET}")
        print(f"{GREEN}[1]{RESET} {BLUE}Mark Habit Done{RESET}")
        print(f"{GREEN}[2]{RESET} {BLUE}Add Habit{RESET}")
        print(f"{GREEN}[3]{RESET} {BLUE}Remove Habit{RESET}")
        print(f"{GREEN}[4]{RESET} {BLUE}EXIT{RESET}")
        print('')

    # Main function
    def main():
        while True:
            main_menu()
            choice = input("Choose an option: ")
            if choice == "0":
                display_habits()
                input("Press Enter to return to the menu...")
            elif choice == "1":
                habit = input("Enter the habit to mark as done: ")
                mark_habit_done(habit)
                save_habits(habits)
                print(f"Habit '{habit}' marked as done for today.")
                input("Press Enter to return to the menu...")
            elif choice == "2":
                habit = input("Enter the habit to add: ")
                add_habit(habit)
                save_habits(habits)
                print(f"Habit '{habit}' added successfully.")
                input("Press Enter to return to the menu...")
            elif choice == "3":
                habit = input("Enter the habit to remove: ")
                remove_habit(habit)
                save_habits(habits)
                print(f"Habit '{habit}' removed successfully.")
                input("Press Enter to return to the menu...")
            elif choice == "4":
                print("Exiting the habit tracker. Keep up the good work!")
                zippy()
                break
            else:
                print("Invalid choice, please try again.")
                input("Press Enter to return to the menu...")

    if __name__ == "__main__":
        main()

zippy()