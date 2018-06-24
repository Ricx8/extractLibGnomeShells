import os

extratList = os.popen("gresource list /usr/lib/gnome-shell/libgnome-shell.so").read().split('\n')

for f in extratList:
    if (len(f) > 1):
        filename = f.split('/')[-1]
        extractPath = '/'.join(f.split('/')[1:-1])+'/'

        # Make the folders where to extract the files
        if not(os.path.exists(extractPath)):
            os.makedirs(extractPath)

        # Extract the files
        os.popen("gresource extract /usr/lib/gnome-shell/libgnome-shell.so "+f+" > "+extractPath+'/'+filename)
