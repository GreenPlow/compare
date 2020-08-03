
import sys
import args_helper
from Classes import File


def main():

    if sys.version_info.major < 3:
        raise ValueError("Python 3 or higher is required.")

    args_object = args_helper.parse_args(sys.argv[1:])
    File.src, File.dest, File.hidden = args_object.src, args_object.dest, args_object.hidden

    # TODO handle "" for paths with spaces
    # TODO unit test to make sure pathsdonotexist is called first

    if File.checkif_pathsdonotexist() or File.checkif_pathsaredupes():
        sys.exit(1)
    else:
        print('\n...both paths okay!')
    # print("path to copy files from...", File.src)
    # print("path to put copied files...", File.dest, "\n")


    """
    OPTION 1 - TRY TO COPY EACH FILE FIRST, ONLY CREATE OBJECT IF IT EXISTS
    
    BENEFITS
    Less memory - Creates less objects
    Faster - Requires at least one less pass over the files being analyzed
    
    OPTION 2 - MAKE OBJECT FOR EVERY FILE FIRST
    
    BENEFITS
    Time to implement - class and function already written
    """


if __name__ == "__main__":
    main()
