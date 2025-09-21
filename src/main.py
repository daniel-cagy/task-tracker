import json

class Tracker:
    """
    A class used for tracking categories and its tasks, saving them in a json
    file.
    
    Attributes
    ----------
    MAINJSON_PATH : str
        The path to the main json file, which stores a list of all files saved
        and the last file used.
    savefile_path : str
        The path to the save file, which stores a dict that maps categories
        with its list of tasks. It is initialized with the last file used,
        saved in main.json, or an empty str if it's the user's first access.
    categories : dict
        A dict that maps categories with its list of tasks. It is initialized
        by loading the save file.

    Methods
    -------
    show_categories() -> str
        Exibits all courses and tasks currently saved.
    add_task(category_name: str, task: dict) -> bool
        Tries to save the task in the tasks list, inside the categories dict.
        True if succeeded, else False.
    rem_task(category_name: str, task: dict) -> bool
        Tries to remove the task from the tasks list, inside the categories
        dict.
        True if succeeded, else False.
    find_task_by_name(category_name: str, target_name: str) -> dict
        Finds a task by its name, inside the tasks list of a given category.
        Returns the task if found, else an empty dict.
    add_category(category_name: str) -> None
        Adds a new category with an empty list of tasks.
    rem_category(category_name: str) -> None
        Removes the category and its tasks from the categories dict.
    save() -> bool
        Tries to save the save file with the updated categories dict.
        True if succeeded, else False.
    load() -> dict
        The categories dict saved in the save file, or an empty
        dict if it fails to find the file.
    is_first_access() -> bool
        Tries to open the mainjson file. If succesfull, then it isn't the
        user's first access. Else, it is.
        Called on the init method, for verifying if there's a save file for
        looking at.
    get_last_savefile() -> str
        The name of the last save file used. It is saved in main.json.
    create_first_file() -> str
        An empty str, saving it in the mainjson file.
        It's just a temporary solution while the user doesn't creates it's
        first file.
    add_file_to_mainjson() -> None
        Gets the old json_dict, checks if the file was already saved in mainjson, 
        saving it in case it wasn't, and rewrites the json with the updated dict.
    get_files() -> list
        A list of files, saved on the mainjson dict. Used for checking if
        a file was already used before reading it.
    load_other_file(file: str) -> bool
        Checks if the file was already saved on the mainjson dict. If it was,
        updates the mainjson file and loads it, returning True. Else, it just
        returns False.
    get_mainjson_dict() -> dict
        Returns the mainjson dict, which contains information about
        files already saved and the last file used.
    update_mainjson(json_dict: dict) -> None
        Updates the mainjson with the new json_dict by rewriting it.
        The entire json is replaced by the new json_dict. It's not
        adding information, but replacing it.
    """


    def __init__(self):
        # mainjson stores a list of all files saved and the last file used
        self.MAINJSON_PATH = "saves/main.json"
        # savefile stores a dict that maps categories with its list of tasks
        self.savefile_path = (
            self.get_last_savefile() 
            if not self.is_first_access()   # if so, there's no 'last savefile'
            else self.create_first_file()   # empty str. also, mainjson is initialized
            )    
        self.categories = self.load()

    def show_categories(self) -> str:
        """


        Returns
        -------
        str
            Exibits all courses and tasks currently saved.

        """
        s_out = ""
        for category in self.categories:
            tasks = self.categories[category]
            s_out += f"{category}: \n"
            if not tasks:
                s_out += "No pending tasks\n"
            else:
                for task in tasks:
                    s_out += f"""- {task["name"]}, for {task["time"]}\n"""
            s_out += "\n"
        return s_out

    def add_task(self, category_name: str, task: dict) -> bool:
        """


        Parameters
        ----------
        category_name : str
            The category's name, used as a key, in the categories dict, to
            its tasks.
        task : dict
            The task that the user wants to save.

        Returns
        -------
        bool
            Tries to save the task in the tasks list, inside the categories
            dict. True if succeeded, else False

        """
        try:
            l_tasks = self.categories[category_name]
            l_tasks.append(task)
            return True
        except:
            return False

    def rem_task(self, category_name: str, task: dict) -> bool:
        """


        Parameters
        ----------
        category_name : str
            The category's name, used as a key, in the categories dict, to
            its tasks.
        task : dict
            The task that the user wants to remove.

        Returns
        -------
        bool
            Tries to remove the task from the tasks list, inside the categories
            dict.

        """
        try:
            l_tasks = self.categories[category_name]
            l_tasks.remove(task)
            return True
        except:
            return False
        
    def find_task_by_name(self, category_name, target_name) -> dict:
        """
        Parameters
        ----------
        category_name : str
            The category's name, used as a key, in the categories dict, to
            its tasks.
        target_name : str
            The name of the task we want to find.
        Returns
        -------
        dict
            The task with the name target_name, if it exists. Else, an empty
            dict.
        """
        l_tasks = self.categories[category_name]

        # getting all tasks that contains target_name as value of "name"
        tasks_with_target_name = [task for task in l_tasks if task.get("name") == target_name]
        # getting the first element only if the list is not empty
        target_task = tasks_with_target_name[0] if tasks_with_target_name else {}
        return target_task

    def add_category(self, category_name: str) -> None:
        """


        Parameters
        ----------
        category_name : str
            The category's name, used as a key, in the categories dict, to
            its tasks.

        Returns
        -------
        None
            Adds a new category with an empty list of tasks.

        """
        self.categories[category_name] = []

    def rem_category(self, category_name: str) -> None:
        """


        Parameters
        ----------
        category_name : str
            The category's name, used as a key, in the categories dict, to
            its tasks.

        Returns
        -------
        None
            Removes the category and its tasks from the categories dict.

        """
        self.categories.pop(category_name)

    def save(self) -> bool:
        """


        Returns
        -------
        bool
            Tries to save the save file with the updated categories dict.
            True if succeeded, else False


        """
        try:
            with open(self.savefile_path, "w", encoding="utf-8") as file:
                json.dump(self.categories, file, ensure_ascii=False, indent=2)
            return True
        except:
            return False

    def load(self) -> dict:
        """


        Returns
        -------
        dict
            The categories dict saved in the save file, or an empty
            dict if it fails to find the file.

        """
        try:
            with open(self.savefile_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except:
            return {}

    def is_first_access(self) -> bool:
        """
        

        Returns
        -------
        bool
            Tries to open the mainjson file. If succesfull, then it isn't the
            user's first access. Else, it is.
            Called on the init method, for verifying if there's a save file for
            looking at.
            
        """
        try:
            open(self.MAINJSON_PATH, "r", encoding="utf-8")
            return False
        except:
            return True

    def get_last_savefile(self) -> str:
        """

        Returns
        -------

        str
            The name of the last save file used. It is saved in main.json.
        """
        json_dict = self.get_mainjson_dict()
        save_file = json_dict["last_file"]
        return save_file

    def create_first_file(self) -> str:
        """
        

        Returns
        -------
        str
            An empty str, saving it in the mainjson file.
            It's just a temporary solution while the user doesn't creates it's
            first file.

        """
        json_dict = {"files": [], "last_file": ""} # empty list of files, and no last file
        self.update_mainjson(json_dict)
        return ""

    def add_file_to_mainjson(self) -> None:
        """
        

        Returns
        -------
        None
            Gets the old json_dict, checks if the file was already saved in mainjson, 
            saving it in case it wasn't, and rewrites the json with the updated dict.

        """
        json_dict = self.get_mainjson_dict()
        files = json_dict["files"]
        if not self.savefile_path in files:
            files.append(self.savefile_path)
        json_dict["last_file"] = self.savefile_path
        self.update_mainjson(json_dict)

    def get_files(self) -> list:
        """
        

        Returns
        -------
        list
            A list of files, saved on the mainjson dict. Used for checking if
            a file was already used before reading it.

        """
        json_dict = self.get_mainjson_dict()
        files = json_dict["files"]
        return files

    def load_other_file(self, file: str) -> bool:
        """
        

        Returns
        -------
        bool
            Checks if the file was already saved on the mainjson dict. If it was,
            updates the mainjson file and loads it, returning True. Else, it just
            returns False.

        """
        if file in self.get_files():
            self.savefile_path = file
            self.categories = self.load()
            return True
        else:
            return False
    
    def get_mainjson_dict(self) -> dict:
        """
        

        Returns
        -------
        dict
            Returns the mainjson dict, which contains information about
            files already saved and the last file used.

        """
        with open(self.MAINJSON_PATH, "r", encoding="utf-8") as main_file:
            json_dict = json.load(main_file)
            return json_dict
    
    def update_mainjson(self, json_dict: dict) -> None:
        """
        

        Parameters
        ----------
        json_dict : dict
            The dict we want the mainjson to update to. The dict needs to meet
            the format {"files": [], "last_file": ""}.

        Returns
        -------
        None
            Updates the mainjson with the new json_dict by rewriting it.
            The entire json is replaced by the new json_dict. It's not
            adding information, but replacing it.

        """
        with open(self.MAINJSON_PATH, "w", encoding="utf-8") as new_main_file:
            json.dump(json_dict, new_main_file, ensure_ascii=False, indent=2)