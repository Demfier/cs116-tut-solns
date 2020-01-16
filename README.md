# cs116-tut-solns
Solution to CS116 Tutorials

Follow the steps below to submit your changes:

* Fork this repo.
* Clone the forked repo in your local machine.
* Setup upstream: `git remote add upstream git@github.com:Demfier/cs116-tut-solns.git` (Note: don't push to upstream/master directly. I have protected it.)
* Change origin: `git remote set origin git@github.com:{yourUsername}/cs116-tut-solns.git`
* Make a seperate branch by `git checkout -b {yourUsername}` and do all the development in that particular branch (like adding missing contracts and tests for a function).

Normally, your chain of actions should be something like:
* Develop
* `git add fileName` (for e.g. `git add tut1.py` if you made changes to `tut1.py`)
* `git commit -m "A useful commit message"`
* `git pull upstream master` (very important to pull before pushing your code)
* `git push origin {yourUsername}` (note that you synchronize with upstream and push to origin)
* Submit a pull request through github

Once you've made a PR, I'll review it and merge if everything looks good.
