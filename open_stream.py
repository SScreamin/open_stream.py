import subprocess

twitch_link = input('Enter Twitch stream URL: ')
subprocess.run(['python3', '-m', 'streamlink', '--player', 'mpv', twitch_link, 'best'])