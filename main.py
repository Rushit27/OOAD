from browse import *
from edit import *

def main():
    input_file=openAVideoFile()
    # cut_video(rf'{input_file}',0,10)
    concatenate_video(input_file,input_file)

if __name__=="__main__":
    main()