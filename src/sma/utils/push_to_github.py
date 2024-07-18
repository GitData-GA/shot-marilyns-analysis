import os
import getpass
import textwrap
from datetime import datetime
import pytz


def push_to_github(
    username,
    repository,
    branch,
    from_path,
    to_path,
    delete_local_branch=True,
    timezone="UTC",
):
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
    :param delete_local_branch: Whether to delete the local copy of the branch after pushing (default: True).
    :type delete_local_branch: bool
    :param timezone: Timezone for the commit timestamp (default: 'UTC').
    :type timezone: str
    :raises ValueError: If the input for deleting old files is not 'Y' or 'N'.
    """
    if timezone not in pytz.all_timezones:
        raise ValueError(
            f"Invalid input of timezone. It must be one of {pytz.all_timezones}"
        )
    
    gh_email = getpass.getpass(
        f"gh_email: \nNote: Your email address of the GitHub account that can read and write https://github.com/{username}/{repository}/tree/{branch} \n"
    )
    gh_username = getpass.getpass(
        f"\n\ngh_username: \nNote: Your username of the GitHub account that can read and write https://github.com/{username}/{repository}/tree/{branch} \n"
    )
    gh_password = getpass.getpass(
        f"\n\ngh_password: \nNote: Your password of the GitHub account that can read and write https://github.com/{username}/{repository}/tree/{branch} \n"
    )
    gh_token = getpass.getpass(
        f"\n\ngh_token: \nNote: Your personal access token of the GitHub account that can read and write https://github.com/{username}/{repository}/tree/{branch} \nTo get a personal access token, please see https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic. \nIn the 'Select scopes' section, simply select all scopes.\n"
    )
    delete_all_old_files_before_pushing = input(
        "\n\nDelete all old files? (Y/N, recommendation is N): \nNote: If you type Y, before pushing new files, the old files in the directory of your GitHub repo will be deleted first.\n"
    )

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
        raise ValueError(
            "Invalid input. delete_all_old_files_before_pushing must be either Y or N."
        )

    os.system(f"cp {from_path}/* {branch}_copy/{to_path}")
    os.chdir(f"{branch}_copy")
    os.system("git add .")
    os.system(
        f"git commit -m '{gh_username} {datetime.now(pytz.timezone(timezone)).strftime('%Y/%m/%d - %H:%M:%S')} {timezone}'"
    )
    os.system(f"git push origin {branch}")
    os.chdir("..")
    if delete_local_branch:
        os.system(f"rm -r {branch}_copy")
