import pyautogui
from pygame import mixer
import time
import pygame
import os

gamers_name = ['Cekenar','Jorlleag','Ikatiar the Venom','Lady Mirenilla','Lady Nevederia','Lord Feshlak',"Lord Koi'Doken",'Sevalak','Aaryonar','Zlexak','Dagarn the Destroyer','Eashen of the Sky','Lord Kreizenn',"Vulak`Aerr",'Lord Vyemm','Dozekar the Cursed','Telkorenar','Gozzrem','Lendiniara the Keeper','King Tormax','Statue of Rallos Zek']


log_file = 'C:\P99\Logs\eqlog_Kodlar_project1999.txt'
search_text = "Attacking a greater skeleton Master"
music_file = 'C:\Users\Karl K\Downloads\beep-01a.wav'

def main():
    while True:
        try:
            with open(log_file, 'rb') as f:
                for each_gamer in gamers_name:
                    to_find = "Attacking " + each_gamer + " Master"
                    if to_find in f.read():
                        pyautogui.press('numlock')
                        pygame.init()
                        mixer.music.load(music_file) # you may use .mp3 but support is limited
                        mixer.music.play()
                        os.remove(log_file)
        except:
            continue
                
      


if __name__ == '__main__':
    main()
