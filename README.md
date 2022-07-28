# **COLFLIX**

A short video streaming platform for college students. 

## What It Does
This platform allows user (authennticated) to create, view, upload and delete videos.  
General user (unuthenticated) can only view videls but can't interact with the platform.

## Technology Used
- HTML and CSS
- Javascript 
- Django
- PostgreSQL
- Django rest framework

## Project Status
> Project is : In progress

# Setup
## Setup local environment
1. Create a folder cd into the folder and `git clone https://github.com/zuri-training/colflix_team117.git` to your local.
2. `env/Scripts/activate` to activate virtual environment
3. Run `git fetch origin` to fetch for remote updates
4. Pull latest changes from the *main* branch. `git pull origin main`.

## Branching
### Frontend
All branch names should be prefix with *fn_* which stands for `frontend` example *`fn_login-page`*
1. Create a new branch to make your changes. Run `git checkout -b fn_<branch-name>` to create your working branch e.g *`git checkout -b fn_login-page`*
2. Make the required changes.
3. Push from your branch

### Backend
All branch names should be prefix with *bn_* which stands for `backend` example *`bn_login-page`*
1. Create a new branch to make your changes. Run `git checkout -b bn_<branch-name>` to create your working branch e.g *`git checkout -b bn_login-page`*
2. Make the required changes.

## Commits
1. Stage the file. `git add <your-file>` that has changed. e.g `git add frontend/index.html` because I made changes to the *index.html* file in the frontend folder. You can use *vscode* or *github Desktop*.
2. Write an explanatory commit message using `git commit -m "<your-message>"` e.g `git commit -m "link style.css file"`.

## Pushing
1. Push your local changes using `git push -u origin <your_branch_name>` e.g `git push -u origin fn_login-page`
2. Visit the remote url to create a pull request (PR).
3. Check if you have merge conflict. If so, then resolve. Get assistance if possible.

#Collaborators
- 
-
-
-

# License
MIT License

Copyright (c) 2021 Joseph Busayo Jayeoba

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.