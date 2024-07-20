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
    print(f"{GREEN}[>] {RESET}{BLUE}Version{RESET}      : 1.0")
    print('')
    print(f"{YELLOW}[!] Select a Option :{RESET}")
    print('')
    print(f"{GREEN}[0] {RESET}{BLUE}Youtube Downloader")
    print('')
    
    choice = input(f"{GREEN}[>]{RESET}")
    if choice == "0":
        yt()
        
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


        
zippy()