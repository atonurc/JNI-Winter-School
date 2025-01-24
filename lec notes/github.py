import os
os.system(r"copy /y main.pdf C:\Users\ASUS\web\atonurc.github.io\assets\MAT433_func.pdf")

from git import Repo

from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H:%M:%S")


PATH_OF_GIT_REPO = r'C:\Users\ASUS\web\atonurc.github.io\.git' 
COMMIT_MESSAGE = 'Func update '+dt_string

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')

git_push()
