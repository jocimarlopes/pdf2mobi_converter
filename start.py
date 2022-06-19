import graphics
import subprocess
import os
import platform


if __name__ == '__main__':
    if 'Linux' in platform.system():
        try:
            verify = (subprocess.check_output('ebook-convert --version', shell=True)).decode("utf-8")
            graphics.init()
        except Exception as e:
            print(e)
            print('You need install Calibre to convert PDF files! We will do this for you..')
            os.system('sudo apt install calibre')

#Developed by Jocimar Lopes (https://instagram.com/@jocimarlopes)