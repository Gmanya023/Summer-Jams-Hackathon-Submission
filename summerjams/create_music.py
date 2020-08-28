from flask import url_for
from pydub import AudioSegment
import random
import string
import pandas as pd
import os

global prev_overlay

def process_labels(labels):
    print(labels)
    list_of_sounds = []
    df = pd.read_csv(os.path.join('summerjams/media/','music_labels.csv'))
    tags = df['tags'].tolist()
    location = df['file'].tolist()

    for label in labels:
        if label.lower() in tags:
            print(label)
            pos = int(tags.index(label.lower()))
            list_of_sounds.append(location[pos])
    return (list_of_sounds)

def sound_manipulation(theme_type = "Piano", sounds = []):
    if (theme_type == "Acoustic"):
        theme = AudioSegment.from_wav(os.path.join('summerjams/media/background_themes/','Acoustic.wav'))
    elif (theme_type == "Electronic"):
        theme = AudioSegment.from_wav(os.path.join('summerjams/media/background_themes/','Electronic.wav'))
    else:
        theme = AudioSegment.from_wav(os.path.join('summerjams/media/background_themes/','Piano.wav'))


    if (len(sounds)!= 0):
        audio_files = {}
        # limit the number of sounds to a max of 4
        if (len(sounds)>4):
            choosen_sounds = random.sample(range(len(sounds)), 4)
            for x in choosen_sounds:
                audio_files["sound_{0}".format(choosen_sounds.index(x))] = AudioSegment.from_wav(os.path.join('summerjams/media/sound files/',str(sounds[x])))
        else:
            for x in range(len(sounds)):
                audio_files["sound_{0}".format(x)] = AudioSegment.from_wav(os.path.join('summerjams/media/sound files/', str(sounds[x])))

        overlay1 = theme.overlay(audio_files["sound_0"],
                                position = 0.1 * len(theme),
                                gain_during_overlay=-2)
        prev_overlay = overlay1

        for i in range (len(audio_files)):
            current_overlay = overlay_music(prev_overlay, audio_files["sound_"+str(i)], i*0.3, -2)
            prev_overlay = current_overlay
        wave_obj = current_overlay.fade_out(duration = 3000)
    else:
        wave_obj = theme

    file_name = nameGenerator()
    wave_obj.export(os.path.join("summerjams/media/generated_files/",file_name), format = "wav")
    # return value - file name to be used to play the exported file
    return (file_name)

def overlay_music (prev_sound, file, pos, volume):
    overlay_clip = prev_sound.overlay(file,
                                position = (pos*len(prev_sound))+500,
                                gain_during_overlay = volume)
    return overlay_clip

# Generates a random file name - everytime a new music file is created
def nameGenerator(string_length = 8):
    character = string.ascii_lowercase + string.digits
    return ((''.join(random.choice(character) for i in range(string_length)))+".wav")
