## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- clone
  - Duplicates a repository into a new directory
  - `git clone git@github.com:WSU-kduncan/ceg3120-EthanK-WSU.git`
- add
  - Adds a file to tracking for git purposes
  - `git add README.md`
- rm
  - Deletes a file from tracking AND the directory
  - Use --cached to just delete from tracking
  - `git rm --cached README.md`
- commit
  - Stages files for syncing with remote repository
  - `git commit -m "A useful commit message"`
- push
  - "Push"es files to the remote repository that have been tracked and staged
  - `git push`
- fetch
  - Gets files from a remote repository into a directory that is already set up for git, does not affect local files
  - `git fetch git@github.com:WSU-kduncan/ceg3120-EthanK-WSU.git`
- merge
  - Synchronizes a branch with another, proabably the main branch
  - `git merge test-branch`
- pull
  - Performs a `git fetch` and then a `git merge` to effectively update a local branch with remote files
  - `git pull git@github.com:WSU-kduncan/ceg3120-EthanK-WSU.git`
- branch
  - Creates a branch to work on files in a git folder system that lets you edit files without affecting other versions
  - `git branch test-branch`
- checkout
  - Changes the branch you are currently working with
  - `git checkout main`

## git files & folders

- .git folder
  - Holds all the information required for git to function in a folder system
- .gitignore file
  - Lists files, file types, etc using regex that should not be acknowledged by git

## GitHub

- Pull requests
  - Details requests to merge forked content with the primary repository
- SSH authentication to repositories
  - Used to verify that only someone with proper access is able to modify a repository

## Resources

- [Pro Git Book](https://git-scm.com/book/en/v2)
