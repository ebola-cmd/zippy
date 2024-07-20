import os
import yt_dlp

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
    print(f"{GREEN}[>] {RESET}{BLUE}Version{RESET}      : 1.1")
    print('')
    print(f"{YELLOW}[!] Select a Option :{RESET}")
    print('')
    print(f"{GREEN}[0] {RESET}{BLUE}Youtube Downloader")
    print(f"{GREEN}[1] {RESET}{BLUE}To-do List")
    print('')
    
    choice = input(f"{GREEN}[>]{RESET}")
    if choice == "0":
        yt()
        
    if choice == "1":
        todo()
        
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

zippy()
