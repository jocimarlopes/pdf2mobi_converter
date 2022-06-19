import os
import sys
import graphics

extensions = [
    '.pdf'
]

def epub2mobi(fromdir, todir, ignore_if=None):
    
    if not os.path.exists(todir):
        os.makedirs(todir)

    if len(fromdir) > 0:
        graphics.show_info('Warning', 'Converting PDF(s)... \nWait..')
    if len(fromdir) == 1:
        mobi = fromdir[0].split('/')
        mobi = todir + (mobi[-1].replace('.pdf', '.mobi'))

        if not os.path.exists(mobi):
            try:
                graphics.progress(len(fromdir))
                os.system('ebook-convert "{}" "{}"'.format(fromdir[0], mobi))
                graphics.show_info('Success!', 'PDF converted!\nYour file(s) are in folder "output"')
            except Exception as e:
                print(e)
                graphics.show_info('Error', 'Failed to convert files to MOBI, \ntry again')
                exit()
            return
    
    if len(fromdir) > 1:
        for item in fromdir:
            print(item)
            mobi = item.split('/')
            mobi = todir + (mobi[-1].replace('.pdf', '.mobi'))
            try:
                graphics.progress(len(fromdir))
                os.system('ebook-convert "{}" "{}"'.format(item, mobi))
            except Exception as e:
                print(e)
                graphics.show_info('Error', 'Failed to convert files to MOBI, try again')
                exit()
        graphics.show_info('Success!', 'PDF converted! Your file(s) are in folder "output"')
        

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

def init(document):
    if len(document) < 1:
        graphics.show_info('Warning!', 'You need to select any PDF')
        return
    fromdir, todir = document, './output/'
    if len(sys.argv) > 1:  fromdir = sys.argv[1]
    if len(sys.argv) == 3: todir = sys.argv[2]
    epub2mobi(fromdir, todir, ignore_if=['ninios'])

#Developed by Jocimar Lopes (https://instagram.com/@jocimarlopes)