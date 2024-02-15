# MADE BY GITHUB USER GabboClown

from PYTDownloader_func import mp4Download, mp3Download
from pytube import YouTube

if __name__ == '__main__':
    links = [] # Links list, in case the user uses the tool multiple links at a time
    print('Hi! Thanks for using this tool made by GitHub: GabboClown\nPlease, insert the links and write submit to download them...')

    links.append(input()) # Reads the first link
    # Reads the other links until the user writes 'submit'
    while links[-1].lower() != 'submit':
        links.append(input())
    links.pop() # Pops the last item, which is 'submit'

    path = input('\nThanks for that, now please insert the full path to the folder you want to download these files to...\n\n')

    for link in links:
        print(f'What format do you want the video \'{YouTube(link).title}\' to be downloaded in? [mp3/mp4]')

        filetype = input()
        if filetype.lower() == 'mp3': mp3Download(link, path) # Read PYTDownloader_func comments
        elif filetype.lower() == 'mp4': mp4Download(link, path) # Read PYTDownloader_func comments
        else: print('There was something wrong with your request for this link, please try again later...')
    
    print('Thanks for using this tool, bye...')