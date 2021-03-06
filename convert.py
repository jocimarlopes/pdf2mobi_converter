import os
import sys
import graphics

extensions = [
    '.pdf'
]

def pdf2mobi(fromdir, todir, ignore_if=None):
    if not os.path.exists(todir):
        os.makedirs(todir)
    if len(fromdir) > 0:
        graphics.show_info('Converting PDF(s)', 'Please, wait..')
    if len(fromdir) == 1:
        mobi = fromdir[0].split('/')
        mobi = todir + (mobi[-1].replace('.pdf', '.mobi'))
        if not os.path.exists(mobi):
            try:
                os.system('ebook-convert "{}" "{}"'.format(fromdir[0], mobi))
                graphics.progress(len(fromdir))
                graphics.show_info('Success!', 'PDF converted!\nYour file(s) are in folder "output"')
            except Exception as e:
                print(e)
                graphics.show_info('Error', 'Failed to convert files to MOBI, \ntry again')
                exit()
            return
    if len(fromdir) > 1:
        for item in fromdir:
            mobi = item.split('/')
            mobi = todir + (mobi[-1].replace('.pdf', '.mobi'))
            if not os.path.exists(mobi):
                try:
                    os.system('ebook-convert "{}" "{}"'.format(item, mobi))
                    graphics.progress(len(fromdir))
                except Exception as e:
                    print(e)
                    graphics.show_info('Error', 'Failed to convert files to MOBI, try again')
                    exit()
        graphics.show_info('Success!', 'PDF converted! Your file(s) are in folder "output"')
        
def init(document):
    if len(document) < 1:
        return
    fromdir, todir = document, './output/'
    if len(sys.argv) > 1:  fromdir = sys.argv[1]
    if len(sys.argv) == 3: todir = sys.argv[2]
    pdf2mobi(fromdir, todir, ignore_if=['ninios'])

#Developed by Jocimar Lopes (https://instagram.com/@jocimarlopes)