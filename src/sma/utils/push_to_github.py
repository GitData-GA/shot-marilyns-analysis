import os
import getpass


def push_to_github(username, repository, branch, from_path, to_path):
    """
    Push Local Changes to GitHub Repository.

    This function automates the process of pushing local changes to a specified branch
    of a GitHub repository. It prompts the user for necessary credentials and configuration,
    clones the repository, optionally deletes old files, copies new files, commits, and
    pushes the changes.

    :param username: GitHub username.
    :type username: str
    :param repository: Name of the GitHub repository.
    :type repository: str
    :param branch: Branch of the repository to push changes to.
    :type branch: str
    :param from_path: Local path of the files to be pushed.
    :type from_path: str
    :param to_path: Destination path in the repository where files will be copied.
    :type to_path: str
    :raises ValueError: If the input for deleting old files is not 'Y' or 'N'.
    """
    gh_email = getpass.getpass("Email address: ")
    gh_username = getpass.getpass("Username: ")
    gh_password = getpass.getpass("Password: ")
    gh_token = getpass.getpass("Personal access token: ")
    delete_all_old_files_before_pushing = input("Delete all old files? (Y/N): ")

    os.system(f"git config --global user.email {gh_email}")
    os.system(f"git config --global user.name {gh_username}")
    os.system(f"git config --global user.password {gh_password}")
    os.system(
        f"git clone --branch {branch} https://{gh_token}@github.com/{username}/{repository} {branch}_copy"
    )

    if delete_all_old_files_before_pushing == "Y":
        os.system(f"rm -r {branch}_copy/{to_path}/*")
    elif delete_all_old_files_before_pushing == "N":
        pass
    else:
        ValueError(
            "Invalid input. delete_all_old_files_before_pushing must be either Y or N."
        )

    os.system(f"cp {from_path}/* {branch}_copy/{to_path}")
    os.chdir(f"{branch}_copy")
    os.system("git add .")
    os.system(f"git commit -m '{gh_username} commits from Colab'")
    os.system(f"git push origin {branch}")
    os.chdir("..")
    os.system(f"rm -r {branch}_copy")
