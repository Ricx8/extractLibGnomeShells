import os

libs = ["/usr/lib/gnome-shell/libgnome-shell.so", "/usr/lib/libgjs.so.0"]

for libFile in libs:
    extratList = os.popen("gresource list "+libFile).read().split('\n')

    for f in extratList:
        if (len(f) > 1):
            filename = f.split('/')[-1]
            extractPath = '/'.join(f.split('/')[1:-1])+'/'

            # Make the folders where to extract the files
            if not(os.path.exists(extractPath)):
                os.makedirs(extractPath)

            # Extract the files
            os.popen("gresource extract "+libFile+" "+f+" > "+extractPath+'/'+filename)
