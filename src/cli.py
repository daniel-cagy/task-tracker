from main import Tracker
import argparse as arg
from sys import exit

def parse_command(subparser, action: str, arguments: list) -> arg.ArgumentParser:
    """
    Helper function to parse a command with its arguments.
    
    Parameters
    ----------
    subparser : _SubParsersAction
        The subparser to which the command will be added.
        action : str
        The name of the command.
        arguments : list
        The list of arguments for the command.
    
    Returns
    -------
        arg.ArgumentParser
        The parser for the command.
    """
    command = subparser.add_parser(action)
    for argument in arguments:
        command.add_argument(argument)
    return command

def parse_arguments() -> arg.Namespace:
    """
    Parses the command line arguments using argparse.
    
    Returns
    -------
    arg.Namespace
        The parsed arguments.
    """
    parser = arg.ArgumentParser(prog="categories")
    subparser = parser.add_subparsers(dest="command")

    file_command = parse_command(subparser, "new-file", ["file"])
    load_file_command = parse_command(subparser, "load-file", ["file"])
    add_course_command = parse_command(subparser, "add-category", ["c_name"])
    rem_course_command = parse_command(subparser, "rem-course", ["c_name"])
    add_task_command = parse_command(subparser, "add-task", ["t_cname", "t_name", "t_time"])
    rem_task_command = parse_command(subparser, "rem-task", ["t_cname", "t_name"])
    show_command = subparser.add_parser("show")

    return parser.parse_args()

def error_handler(status: bool, fail_msg: str = "Failed to save changes" \
                  , success_msg: str = "Changes succesfully saved") -> None:
    """ 
    Simple error handler to avoid code repetition.
    
    Parameters
    ----------
    status : bool
        The status of the operation that was just performed.
    fail_msg : str, optional
        The message to be printed if the operation failed, by default
        "Failed to save changes"
    success_msg : str, optional
        The message to be printed if the operation succeeded, by default
        "Changes succesfully saved"
    
    Returns
    -------
    None
        Exits the program if the operation failed, else prints a success
        message.
    """
    if not status:
        print(fail_msg)
        exit()
    else:
        print(success_msg)


if __name__ == "__main__":
    

    trck = Tracker()
    args = parse_arguments()

    match args.command:

        case "new-file":
            file = f"saves/{args.file}"
            trck.savefile_path = file
            trck.categories = {}
            trck.add_file_to_mainjson()
            status = trck.save()
            error_handler(status, "Failed to save file", f"Save file {args.file} succesfully added")

        case "load-file":
            file = f"saves/{args.file}"
            l_status = trck.load_other_file(file)
            error_handler(l_status, "Failed to load file", f"File {args.file} succesfully loaded")
            trck.add_file_to_mainjson()
            
        case "add-category":
            trck.add_category(args.c_name)
            print("-----Categories-----")
            print(trck.show_categories())
            status = trck.save()
            error_handler(status, success_msg=f"Category {args.c_name} succesfully added")

        case "rem-category":
            trck.rem_category(args.c_name)
            print("-----Categories-----")
            print(trck.show_categories())
            status = trck.save()
            error_handler(status, success_msg=f"Category {args.c_name} succesfully removed")

        case "add-task":
            task = {"name": args.t_name, "time": args.t_time}
            a_status = trck.add_task(args.t_cname, task)
            error_handler(a_status, "Failed to find category. No changes were made", \
                          "Adding task...\n")
            print(trck.show_categories())
            s_status = trck.save()
            error_handler(s_status)

        case "rem-task":
            task_name = args.t_name
            task = trck.find_task_by_name(args.t_cname, task_name)
            print(task)
            trck.rem_task(args.t_cname, task)
            print(trck.show_categories())
            status = trck.save()
            error_handler(status)

        case "show":
            print("-----Categories-----")
            print(trck.show_categories())
