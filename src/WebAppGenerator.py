#!/usr/bin/python
import sys, getopt

def app(args):
    """Main function entry point e.t.c """
    project_name = ''
    if len(args) < 2:
        print 'WebAppGenerator.py -i <name>'
        sys.exit(2)

    try:
        opts, args = getopt.getopt(args, "h:p:", ["name="])
    except getopt.GetoptError:
        print 'WebAppGenerator.py -i <name>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'WebAppGenerator.py -i <name>'
            sys.exit()
        elif opt in ("-p", "--name"):
            project_name = arg
        else:
            print 'WebAppGenerator.py -i <name>'
            sys.exit()

    create_stubs(project_name)


def create_stubs(project_name):
    """Create the relevant libs, folders e.t.c """
    log("INFO", "Creating stub for project " + project_name)

def log(log_type, log_string):
    """Just do a simple log on terminal"""
    print log_type + ': ' + log_string

#Main entry point
if __name__ == "__main__":
    app(sys.argv[1:])
