from gtts import gTTS
from playsound import playsound
import os
import sys
import argparse


def say(text = None, language = "en", no_cache = False, reset = False):


    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--text", type=str, help="Text")
    parser.add_argument('-l', '--language', type=str, help='Language')
    parser.add_argument('-nc', '--nocache', action="store_true", help='No cache')
    parser.add_argument('-r', '--reset', action="store_true", help='Reset (removing the caches)')
    args = parser.parse_args()

    if not args.text is None:
        text = args.text
    if not args.language is None:
        language = args.language
    if args.nocache:
        no_cache = args.nocache
    if args.reset:
        reset = args.reset


    this_dir, this_filename = os.path.split(__file__)
    the_dir = os.path.join(this_dir, "cache")
    
    

    if reset:
        for root, dirs, files in os.walk(the_dir):
            for file in files:
                if not "empty.mp3" == file:
                    os.remove(os.path.join(root, file))
        if args.text is None and args.reset:
            exit()

    files = os.path.join(the_dir, f"{text[:10]}.mp3")
                
    if not os.path.exists(files) or no_cache:
        gTTS(text, lang = language).save(files)
    
    playsound(files)
