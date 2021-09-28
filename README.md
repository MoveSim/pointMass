# pointMass
Simulation of a point mass in 2D

### initial setup
Clone the project: ```git clone https://github.com/MoveSim/pointMass.git```

Install virtual environment: 
1. ``pip install virtualenv``
2. ``python -m venv .env``

Activate virtual environment
1. ``.env\Scripts\activate``

Install depencies
1. ``pip install -U pip``
2. ``pip install -Ur requirements.txt``

# Developing
When developing, always work on a child branch. (main) is the parent branch.
The name of the branch should clearly show what is done on it.
To create a child branch, go to the parent branch and type:
1. ``git checkout -b [NAME_OF_BRANCH]``

To check existing branches:
1. ``git branch``

To go to a different branch:
1. ``git checkout [NAME_OF_BRANCH]``

When you added/changed code, type this to commit your work:
1. ``git commit -am "[COMMIT_MESSAGE]"``

When you want to push your work for the first time see option 1, else option 2:
1. ``git push --set-upstream origin [BRANCH_NAME]``
2. ``git push``

Go to github to ask for a merge request.
