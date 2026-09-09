# Git Branching, Merging, and Gitignore Tutorial

## Table of Contents
1. [What is This Tutorial About?](#what-is-this-tutorial-about)
2. [Branching - Working on Separate Copies](#branching---working-on-separate-copies)
3. [Merging - Combining Your Work](#merging---combining-your-work)
4. [Resolving Merge Conflicts](#resolving-merge-conflicts)
5. [Gitignore - Ignoring Files](#gitignore---ignoring-files)
6. [Practice Exercises](#practice-exercises)
7. [Quick Reference](#quick-reference)

---

## What is This Tutorial About?

This tutorial builds on the basics you learned in `GIT_TUTORIAL.md`. Now we will cover three powerful Git features:

- **Branching** — Create a separate copy of your project to work on safely
- **Merging** — Combine your work back into the main project
- **Gitignore** — Tell Git to ignore certain files you do not want to track

**Before reading this, make sure you know:**
- What a commit is (`git commit`)
- What a repository is (`git init`)
- Basic Git commands (`git add`, `git status`)

---

## Branching - Working on Separate Copies

### What is a Branch?

A **branch** is like an alternate timeline for your project. Imagine you are writing a book and you want to try a different ending, but you do not want to ruin what you already have. You make a copy, try your idea, and if it works, you add it to the original.

In Git, the main "timeline" is called **main** (or sometimes **master**). When you create a branch, you make a copy of the project that you can change freely.

### Real-World Analogy

Think of branches like cooking:
- You have a recipe that works perfectly
- You want to try adding a new ingredient, but what if it tastes terrible?
- You make a **copy** of the dish to experiment with
- If it is delicious, you use it as the new recipe
- If it is terrible, you throw it away and the original is still fine

### Why Use Branches?

| Without Branches | With Branches |
|-----------------|---------------|
| You break the main code while experimenting | You experiment safely on a separate branch |
| You cannot work on two things at once | Multiple people can work in parallel on different branches |
| Hard to tell what changes belong to what feature | Each branch has its own history |

### How Branches Look

```
main branch:    o------------------------------------------o
                                                           ^
                                                        (merge)
feature branch:          o----o----o----o----o-----------/
                          ^
                       (branch starts here)
```

The `o` symbols are commits (saved snapshots). The feature branch goes off in its own direction, then comes back when it is ready.

### Branch Commands

#### Creating a Branch

```bash
git branch feature/login
```

This creates a new branch called `feature/login`. You are still ON the `main` branch - you just created a new one.

**Tip:** Use descriptive names for branches. Common formats:
- `feature/add-login` - a new feature
- `bugfix/fix-typo` - fixing a bug
- `experiment/try-new-design` - trying something risky

#### Switching to a Branch

```bash
git checkout feature/login
```

Now you are ON the `feature/login` branch. Any changes you make will only affect this branch.

#### Create AND Switch in One Command

```bash
git checkout -b feature/login
```

This is a shortcut that does both steps at once. You will use this one a lot!

#### See All Branches

```bash
git branch
```

Example output:
```
* feature/login
  main
```

The `*` (asterisk) shows which branch you are currently on.

#### Delete a Branch

```bash
git branch -d feature/login
```

You usually do this after the branch has been merged. Use `-D` to force delete a branch that has not been merged:

```bash
git branch -D feature/login
```

---

## Merging - Combining Your Work

### What is Merging?

**Merging** is how you take the work from one branch and combine it into another. When your feature is done and tested, you merge it back into `main`.

### Real-World Analogy

Think of merging like editing a document together:
- You write your section of a report separately
- Your colleague writes their section separately
- You then **combine** both sections into one final document

Git does this automatically for your code files!

### How to Merge

**Step 1:** Switch to the branch you want to merge INTO (usually `main`):
```bash
git checkout main
```

**Step 2:** Merge the other branch into it:
```bash
git merge feature/login
```

That is it! Git will automatically combine the changes.

### Types of Merges

There are two common types of merges. Git handles it automatically.

#### Type 1: Fast-Forward Merge

This happens when `main` has not changed since you created your branch. Git simply moves forward to include your changes.

```
BEFORE:
main:     o----o
                \
feature:         o----o----o

AFTER (fast-forward):
main:     o----o----o----o----o
```

No extra merge commit is created. It is the cleanest type.

#### Type 2: Three-Way Merge

This happens when both `main` AND your branch have new commits. Git creates a special **merge commit** that combines both.

```
BEFORE:
main:     o----o----o  (new commits on main)
                \
feature:         o----o----o  (new commits on feature)

AFTER:
main:     o----o----o-----------o  (merge commit)
                \              /
feature:         o----o----o--
```

The merge commit has two parents - one from each branch.

### Merge Output Examples

**Fast-forward merge output:**
```
Updating a1b2c3d..e4f5g6h
Fast-forward
 notes.txt | 3 +++
 1 file changed, 3 insertions(+)
```

**Three-way merge output:**
```
Merge made by the 'ort' strategy.
 feature.txt | 5 +++++
 1 file changed, 5 insertions(+)
```

---

## Resolving Merge Conflicts

### What is a Merge Conflict?

A **merge conflict** happens when both branches changed the **same part of the same file**. Git does not know which version to keep, so it asks YOU to decide.

This sounds scary, but it is not! Git marks exactly where the problem is.

### When Do Conflicts Happen?

Example:
- On `main`: You changed line 5 of `notes.txt` to say "Hello World"
- On `feature`: Someone changed line 5 of the same file to say "Hi There"
- When you merge: Git says "I do not know which version to use!"

### What a Conflict Looks Like

When you run `git merge` and there is a conflict, Git edits the file to show you both versions:

```
<<<<<<< HEAD
Hello World
=======
Hi There
>>>>>>> feature/login
```

**How to read this:**
- `<<<<<<< HEAD` - This is YOUR version (on the current branch)
- `=======` - The divider between the two versions
- `>>>>>>> feature/login` - This is the version from the branch you are merging

### How to Fix a Conflict

**Step 1:** Open the file in a text editor and find the conflict markers.

**Step 2:** Decide what you want to keep. You have three options:

Option A - Keep YOUR version (HEAD):
```
Hello World
```

Option B - Keep THEIR version (feature/login):
```
Hi There
```

Option C - Keep BOTH (combine them):
```
Hello World and Hi There
```

**Step 3:** Delete the conflict markers (`<<<<<<`, `======`, `>>>>>>`). The file should look normal now.

**Step 4:** Stage and commit the resolved file:
```bash
git add notes.txt
git commit -m "Resolve merge conflict in notes.txt"
```

### Tips for Avoiding Conflicts

- **Communicate** - Tell your team which files you are working on
- **Merge often** - The longer you wait, the more conflicts pile up
- **Work in different files** - If possible, each person works on different files

---

## Gitignore - Ignoring Files

### What is a .gitignore File?

A `.gitignore` file is a list of files and folders that you want Git to **completely ignore**. Files in `.gitignore` will never show up in `git status` and will never be committed.

**You already have one!** Look at the `.gitignore` file in this folder.

### Why Would You Ignore Files?

Some files should NOT be stored in Git:

| Type | Examples | Why Ignore? |
|------|----------|-------------|
| **Secret files** | `.env`, `passwords.txt`, API keys | Do not share secrets publicly! |
| **Dependencies** | `node_modules/`, `venv/` | Too large, easily reinstalled |
| **Build output** | `dist/`, `*.class`, `*.exe` | Generated automatically |
| **OS files** | `.DS_Store` (Mac), `Thumbs.db` (Windows) | Not part of your project |
| **Editor files** | `.vscode/`, `*.swp` | Personal settings |

### How to Create a .gitignore File

Create a file called exactly `.gitignore` in your project folder (note the dot at the start). You can do this in any text editor.

Or, in the terminal:
```bash
# Windows (PowerShell)
New-Item .gitignore

# Mac/Linux
touch .gitignore
```

### .gitignore Syntax

The rules for writing a `.gitignore` file are simple:

#### Ignore a specific file
```gitignore
secret.env
passwords.txt
```

#### Ignore all files with an extension
```gitignore
*.log
*.tmp
*.class
```

#### Ignore an entire folder
```gitignore
node_modules/
dist/
build/
```

#### Ignore a file in a specific folder only
```gitignore
docs/secret.txt
```

#### Add a comment (for your own notes)
```gitignore
# This is a comment - Git ignores comment lines
# Ignore all log files
*.log
```

#### Ignore everything EXCEPT certain files (using !)
```gitignore
# Ignore all .txt files...
*.txt

# ...but NOT this one
!important-notes.txt
```

### A Complete Example .gitignore

Here is a useful `.gitignore` for a typical Python project:

```gitignore
# Secret files - never share these!
.env
*.pem
*.key

# Python virtual environment
venv/
.venv/
__pycache__/
*.pyc

# Testing output
.coverage
htmlcov/

# OS files
.DS_Store
Thumbs.db

# Editor settings
.vscode/
.idea/
*.swp
```

### What if I Already Committed a File I Want to Ignore?

If you accidentally committed a file BEFORE adding it to `.gitignore`, just adding it to `.gitignore` will not help - Git is already tracking it.

You need to **untrack** it first:

```bash
git rm --cached secret.env
```

**What this does:**
- Removes the file from Git tracking
- Does NOT delete the file from your computer
- After this, add `secret.env` to `.gitignore`
- Then commit

```bash
git add .gitignore
git commit -m "Remove secret.env from tracking and add to gitignore"
```

> **Warning:** If the file contained secrets and you already pushed it to GitHub, the secret is in Git history. You should consider changing the secret (password, API key, etc.)

---

## Practice Exercises

Let us practice all three concepts! Open your terminal and navigate to this folder.

```bash
cd /mnt/c/Users/thoma/OneDrive/Bureaublad/Git
```

---

### Exercise 1: Create and Use a Branch

**Goal:** Create a branch, make changes, and see that `main` is unaffected.

**Step 1:** Create and switch to a new branch:
```bash
git checkout -b feature/my-experiment
```

**Step 2:** Make a change. Add a line to `notes.txt`:
```bash
echo "This line was added on my experiment branch" >> notes.txt
```

**Step 3:** Commit the change:
```bash
git add notes.txt
git commit -m "Add experimental line to notes"
```

**Step 4:** Switch back to `main` and check `notes.txt`:
```bash
git checkout main
cat notes.txt
```

Notice that the line you added is **gone**! It only exists on `feature/my-experiment`. This is the magic of branches - your main code is safe.

---

### Exercise 2: Merge Your Branch

**Goal:** Bring the branch changes back into `main`.

**Step 1:** Make sure you are on `main`:
```bash
git checkout main
git branch
```

The `*` should be next to `main`.

**Step 2:** Merge your feature branch:
```bash
git merge feature/my-experiment
```

**Step 3:** Check `notes.txt` again:
```bash
cat notes.txt
```

The experimental line is back! It has been merged into `main`.

**Step 4:** Clean up the branch:
```bash
git branch -d feature/my-experiment
```

**Step 5:** Verify it is gone:
```bash
git branch
```

---

### Exercise 3: Create a Merge Conflict (and Fix It)

**Goal:** Understand what a conflict looks like and how to solve it.

**Step 1:** Create a new branch:
```bash
git checkout -b feature/conflict-test
```

**Step 2:** Add a specific line to `notes.txt`:
```bash
echo "Branch version: Hi from the feature branch!" >> notes.txt
git add notes.txt
git commit -m "Add greeting from feature branch"
```

**Step 3:** Switch back to main and add a DIFFERENT line:
```bash
git checkout main
echo "Main version: Hello from the main branch!" >> notes.txt
git add notes.txt
git commit -m "Add greeting from main branch"
```

**Step 4:** Try to merge - this will cause a conflict:
```bash
git merge feature/conflict-test
```

You should see a message like:
```
Auto-merging notes.txt
CONFLICT (content): Merge conflict in notes.txt
Automatic merge failed; fix conflicts and then commit the result.
```

**Step 5:** Open `notes.txt` in a text editor. Find the conflict markers and keep both greetings. Remove the `<<<<<<<`, `=======`, and `>>>>>>>` lines.

**Step 6:** Commit the resolution:
```bash
git add notes.txt
git commit -m "Resolve conflict: keep both greetings"
```

Congratulations - you resolved a merge conflict!

---

### Exercise 4: Practice Using .gitignore

**Goal:** Make Git ignore a file.

**Step 1:** Create a "secret" file:
```bash
echo "password=hunter2" > secret.txt
```

**Step 2:** Check git status - you will see the file:
```bash
git status
```

**Step 3:** Open `.gitignore` in a text editor and add this line:
```
secret.txt
```

**Step 4:** Check git status again:
```bash
git status
```

The `secret.txt` file is now gone from the list! Git is ignoring it.

**Step 5:** Commit the updated `.gitignore`:
```bash
git add .gitignore
git commit -m "Add secret.txt to gitignore"
```

---

## Common Mistakes and How to Fix Them

### "I am on the wrong branch!"
```bash
git branch          # Check which branch you are on
git checkout main   # Switch to main
```

### "I committed to main instead of my branch!"
```bash
git branch feature/oops           # Create a new branch at this point
git reset HEAD~1                  # Undo the commit on main (keep your changes)
git checkout feature/oops         # Switch to your new branch
git add . && git commit -m "msg"  # Re-commit on the right branch
```

### "I want to throw away my branch and start over!"
```bash
git checkout main
git branch -D feature/my-mess    # Force delete the branch
```

### "git status shows files I do not want to commit!"
Add them to `.gitignore` (see the Gitignore section above).

### "My terminal says 'you have unresolved conflicts'!"
You started a merge but did not finish fixing it. Find the conflicted files (listed in `git status`), fix them, then run:
```bash
git add <conflicted-file>
git commit
```

---

## Quick Reference

### Branch Commands

| What You Want To Do | Command |
|---------------------|---------|
| Create a new branch | `git branch branch-name` |
| Switch to a branch | `git checkout branch-name` |
| Create AND switch to a new branch | `git checkout -b branch-name` |
| List all branches | `git branch` |
| Delete a branch (safe) | `git branch -d branch-name` |
| Delete a branch (force) | `git branch -D branch-name` |

### Merge Commands

| What You Want To Do | Command |
|---------------------|---------|
| Merge a branch into current | `git merge branch-name` |
| See if there are conflicts | `git status` |
| Abort a merge (go back) | `git merge --abort` |

### Gitignore Commands

| What You Want To Do | Command |
|---------------------|---------|
| Check if a file is being ignored | `git check-ignore -v filename` |
| Untrack a file (keep it locally) | `git rm --cached filename` |
| Show all ignored files | `git ls-files --ignored --exclude-standard` |

---

## The Full Branching Workflow

Here is how a typical feature development works from start to finish:

```
1.  git checkout main               Start on main
2.  git pull origin main            Get the latest version
3.  git checkout -b feature/login   Create your feature branch
4.  (edit files, do your work...)
5.  git add .                       Stage your changes
6.  git commit -m "Add login page"  Save your changes
7.  (repeat steps 4-6 as needed)
8.  git checkout main               Switch back to main
9.  git merge feature/login         Bring in your feature
10. git push origin main            Upload to GitHub
11. git branch -d feature/login     Clean up the branch
```

---

## What to Do Next?

Now that you know branching, merging, and gitignore, here is what you can explore next:

1. **Rebasing** - An alternative to merging that keeps history cleaner
2. **Pull Requests** - How teams review code on GitHub before merging
3. **Stashing** - Temporarily saving work without committing (`git stash`)
4. **Tags** - Marking important commits like version releases (`git tag`)

---

## Need More Help?

- Type `git --help` in your terminal
- Visit https://git-scm.com/docs
- Visit https://docs.github.com
