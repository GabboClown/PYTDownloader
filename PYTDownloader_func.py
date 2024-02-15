from pytube import YouTube as YT
import os

def mp4Download(link, path):
    video = YT(link).streams.get_highest_resolution()
    print(f'I\'m downloading the video named \'{YT(link).title}\'')

    try:
        video.download(path)
        print(f'Video named \'{YT(link).title}\' successfully downloaded!')
    except:
        print(f'Unfortunately, the video named \'{YT(link).title}\' could not be parsed...')

    return path

def ConvertToMP3(file):
    # Rename the file to .mp3 extension
    base = os.path.splitext(file)
    new_file = base + '.mp3'
    os.rename(file, new_file)
    return new_file

def mp3Download(link, path):
    # Filters the whole stream list to an audio only stream, then returns a .mp4 without a video encoding
    # Basically a video, with the lowest compression audio codec, but with no video codec
    # The downloaded file will then be renamed to .mp3 extension
    video = YT(link).streams.filter(only_audio=True).first() 

    print(f'I\'m downloading the audio named \'{YT(link).title}\'')

    try:
        ConvertToMP3(video.download(path))
        print(f'Video named \'{YT(link).title}\' successfully downloaded in folder {path}!')
    except:
        print(f'Unfortunately, the audio named \'{YT(link).title}\' could not be parsed...')
    
    return path