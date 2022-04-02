import shutil
import glob

source = "/Users/vojtechoravec/Downloads/"

pythonFolder = "/Users/vojtechoravec/Documents/Programming/Python/"
movieFolder = "/Users/vojtechoravec/Documents/Movies/"
imageFolder = "/Users/vojtechoravec/Documents/Images/"
schoolFolder = "/Users/vojtechoravec/Documents/School/"

dict = {
    pythonFolder: ['py'],
    movieFolder: ['mkv', 'avi', 'mp4'],
    imageFolder: ['jpg','png','gif'],
    schoolFolder: ['doc','docx','pdf','xls']
}

for destination, extensions in dict.items():
    for extension in extensions:
        for file in glob.glob(source + '*.' + extension):
            print(file)
            shutil.move(file, destination)