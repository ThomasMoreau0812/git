# Git Version Control Tutorial for Beginners

## Table of Contents
1. [What is This Tutorial About?](#what-is-this-tutorial-about)
2. [Before You Start - Basic Computer Terms](#before-you-start---basic-computer-terms)
3. [What is Git?](#what-is-git)
4. [What is GitHub?](#what-is-github)
5. [Basic Setup](#basic-setup)
6. [Your First Git Commands](#your-first-git-commands)
7. [Understanding the Git Workflow](#understanding-the-git-workflow)
8. [Practice Exercises](#practice-exercises)
9. [Pushing to GitHub](#pushing-to-github)

---

## What is This Tutorial About?

This tutorial will teach you **Git**, a tool that helps you track changes to your files. Think of it like the "Track Changes" feature in Microsoft Word, but much more powerful.

**By the end, you will:**
- Understand what Git and GitHub are
- Know basic Git commands
- Be able to save your code with Git
- Push your files to GitHub so they're backed up online

---

## Before You Start - Basic Computer Terms

Let me explain some terms you'll see in this tutorial:

### What is a Terminal (Command Line)?
A **terminal** (also called Command Prompt, PowerShell, or Bash) is a text-based way to talk to your computer. Instead of clicking buttons with your mouse, you type commands.

**Why use it?**
Many programming tools, including Git, are used through the terminal.

**How to open it:**
- **Windows**: Press `Win + R`, type `cmd`, press Enter
- **Mac**: Press `Cmd + Space`, type `terminal`, press Enter
- **Linux**: Press `Ctrl + Alt + T`

### What is a Folder (Directory)?
A **folder** on your computer is called a **directory** in the terminal world. They mean the same thing.

### What are Files?
**Files** are documents on your computer. Examples:
- `notes.txt` - a text document
- `sample_code.py` - a Python program
- `photo.jpg` - an image

### What is Code?
**Code** is instructions written in a programming language that tells your computer what to do. The file `sample_code.py` in this folder contains Python code.

---

## What is Git?

**Git** is a tool that tracks changes in your files over time. Here's why that's useful:

### Without Git:
- You create "final_v2.txt", then "final_v3.txt", then "final_FINAL.txt"
- You forget which file has what
- You accidentally delete something important
- You can't remember what you changed last week

### With Git:
- Git remembers every change you make
- You can go back to any previous version
- You can safely try new ideas (branches)
- You can collaborate with others without conflicts

### Real-World Analogy
Think of Git like a **save game system** in a video game:
- You can save your progress at any point
- You can load a previous save if something goes wrong
- You can have multiple save slots (branches)

---

## What is GitHub?

**GitHub** is a website where people store their Git repositories online. It's like "the cloud" for your code.

**The difference:**
- **Git** = The tool on your computer that tracks changes
- **GitHub** = A website that stores your Git history online

**Why use GitHub?**
1. **Backup** - If your computer breaks, your code is safe online
2. **Sharing** - Others can see and use your code
3. **Collaboration** - Multiple people can work on the same project

---

## Basic Setup

### Step 1: Install Git

**Windows:**
1. Go to https://git-scm.com/download/win
2. Download the installer
3. Run it and click "Next" through all options
4. Open "Git Bash" when done (this is your terminal for Git)

**Mac:**
1. Open the Terminal app
2. Type `git --version`
3. If not installed, it will prompt you to install it

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install git
```

### Step 2: Tell Git Who You Are

Git needs to know your name and email. This is required before you can save changes.

**In your terminal, type these commands** (replace with your info):

```bash
git config --global user.name "John Doe"
git config --global user.email "john.doe@example.com"
```

**What just happened?**
- `--global` means this info is saved for ALL your projects
- Git will attach your name to every change you save
- This is like signing your work

### Step 3: Verify It Worked

```bash
git config --list
```

You should see your name and email in the list.

---

## Your First Git Commands

Let's learn the essential Git commands step by step.

### Command 1: `git init`
**What it does:** Creates a new Git repository in your current folder.

**What is a repository?** A folder that Git is tracking. Git will watch for changes in all files in this folder.

```bash
git init
```

**Example:**
```
Before:  /my-project (regular folder)
After:   /my-project/.git (Git is now tracking this folder)
```

### Command 2: `git status`
**What it does:** Shows what's happening in your repository. Which files changed? Which are staged? Which are committed?

```bash
git status
```

**What you'll see:**
- **Untracked files** - New files Git doesn't know about yet
- **Changes to be committed** - Files you've staged (added)
- **Changes not staged** - Modified files you haven't staged yet

### Command 3: `git add`
**What it does:** Tells Git to track specific files. Files must be added before they can be "saved" (committed).

```bash
git add filename.txt           # Add one specific file
git add .                      # Add ALL files in current folder
```

**The dot (`.`) means "everything in this folder".**

### Command 4: `git commit`
**What it does:** Saves your staged changes. Think of it like taking a snapshot of your files at this moment.

```bash
git commit -m "Your message here"
```

**The message (-m "...") describes what you changed.** This is required and important! Good messages help you remember what you did.

**Examples of good messages:**
- "Add new feature to calculate totals"
- "Fix bug where save button didn't work"
- "Update README with installation instructions"

**Examples of BAD messages:**
- "Changes"
- "asdf"
- "stuff"

### Command 5: `git log`
**What it does:** Shows your history of commits (saved snapshots).

```bash
git log                        # Full history
git log --oneline              # Condensed (easier to read)
```

---

## Understanding the Git Workflow

Here's how Git actually works. This is important!

### The Three Stages

When you save something in Git, it goes through three stages:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   STAGE 1: WORKING DIRECTORY                                │
│   (Your files on your computer)                             │
│                                                             │
│   You make changes to your files here.                      │
│   Maybe you edited notes.txt and added a new file.          │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   STAGE 2: STAGING AREA                                     │
│   (Preparation area)                                       │
│                                                             │
│   You choose WHAT to include in your save.                  │
│   You "stage" files with git add.                            │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   STAGE 3: COMMITTED (SAVED)                                │
│   (Your Git repository)                                    │
│                                                             │
│   You "commit" with git commit.                             │
│   Now it's safely saved!                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### The Daily Workflow

```
1. You edit files in your code editor (Notepad, VS Code, etc.)
   ↓
2. You run: git add file.txt        (move to staging)
   ↓
3. You run: git commit -m "msg"     (save permanently)
   ↓
4. Repeat!
```

### Why This Matters

You might ask: "Why can't I just save directly?"

The staging area lets you choose:
- Maybe you fixed 3 things, but only want to save 2 of them
- You can write different commit messages for different changes
- It makes you think about what you're actually saving

---

## Practice Exercises

Let's practice! I'll guide you step by step.

### Before You Start

Make sure you're in the correct folder. In your terminal:

```bash
cd /mnt/c/Users/thoma/OneDrive/Bureaublad/Git
ls
```

You should see your practice files:
```
GIT_TUTORIAL.md  PUSH_TO_GITHUB.md  notes.txt  sample_code.py  shopping_list.txt
```

### Exercise 1: Initialize Git

**Step 1:** Tell Git to start tracking this folder:
```bash
git init
```

**What happened?**
- A hidden `.git` folder was created
- Git is now watching this folder for changes

**Step 2:** Check the status:
```bash
git status
```

You should see something like:
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to stage them)
    GIT_TUTORIAL.md
    PUSH_TO_GITHUB.md
    notes.txt
    sample_code.py
    shopping_list.txt
```

Git is saying: "I see these files, but I'm not tracking them yet!"

### Exercise 2: Stage and Commit One File

**Step 1:** Let's start simple. Stage just one file:
```bash
git add notes.txt
```

**Step 2:** Check the status again:
```bash
git status
```

Now you should see `notes.txt` in a different color or under "Changes to be committed".

**Step 3:** Commit (save) this file:
```bash
git commit -m "Add notes.txt with basic Git commands"
```

**Step 4:** Check the history:
```bash
git log --oneline
```

You should see your first commit!

### Exercise 3: Stage and Commit All Files

**Step 1:** Stage everything else:
```bash
git add .
```

**Step 2:** Commit:
```bash
git commit -m "Add all practice files: tutorial, Python code, and shopping list"
```

**Step 3:** Check status and log:
```bash
git status
git log --oneline
```

Now you should see 2 commits!

### Exercise 4: Make Changes

**Step 1:** Open `notes.txt` in a text editor and add something new.

Or, use the terminal to add a line:
```bash
echo "Added this line from terminal" >> notes.txt
```

**Step 2:** Check what changed:
```bash
git status
git diff notes.txt
```

`git diff` shows you exactly what changed (in green what's added, in red what's removed).

**Step 3:** Save your changes:
```bash
git add notes.txt
git commit -m "Add new line to notes"
```

### Exercise 5: View History

```bash
git log
```

This shows:
- Who made each commit (your name)
- When they made it (date/time)
- The message they wrote

```bash
git log --oneline
```

This is a shorter version, easier to read.

---

## Pushing to GitHub

Now let's put your code on GitHub so it's backed up online!

### Step 1: Create a GitHub Account

1. Go to https://github.com
2. Click **Sign up**
3. Choose a username, enter your email, create a password
4. Verify your account

### Step 2: Create a New Repository

A **repository** (repo) is like a folder on GitHub.

1. After logging in, click the **+** icon in the top-right corner
2. Select **New repository**
3. Fill in the details:

| Field | What to enter |
|-------|---------------|
| **Repository name** | `git-practice` (or any name you like) |
| **Description** | `My first Git repository - learning Git!` |
| **Public/Private** | Choose **Public** (it's free and visible to everyone) |
| **Add a README** | **DO NOT check this** (we already have files) |
| **Add .gitignore** | Leave as "None" for now |

4. Click **Create repository**

### Step 3: Connect Your Computer to GitHub

After creating the repo, you'll see a page with a URL. It looks like:
```
https://github.com/YOURUSERNAME/git-practice
```

**In your terminal, type** (replace YOURUSERNAME with your GitHub username):

```bash
git remote add origin https://github.com/YOURUSERNAME/git-practice.git
```

**What did this do?**
- "remote" = a connection to GitHub
- "origin" = the nickname for your GitHub repo (standard name)
- Now your computer knows where to send your code

### Step 4: Push Your Code

```bash
git push -u origin main
```

**What does this mean?**
- `push` = send your commits to GitHub
- `-u origin main` = to the "origin" repo, on the "main" branch

**You'll be asked for:**
- **Username**: Your GitHub username
- **Password**: Your GitHub password

> **Important:** If you have two-factor authentication (2FA) enabled on GitHub, you need to use a "Personal Access Token" instead of your password. See the "Token Help" box below.

### Step 5: Verify It Worked!

1. Go to `https://github.com/YOURUSERNAME/git-practice`
2. You should see all your files listed!
3. Click on any file to view its contents

**Congratulations!** Your code is now on GitHub!

---

## Token Help (Only if Password Doesn't Work)

If GitHub says your password is wrong, you may need a token:

### Creating a Token:
1. Go to https://github.com/settings/tokens
2. Click **Generate new token (classic)**
3. Name it something like "My Git Practice"
4. Check **repo** (full control)
5. Click **Generate token**
6. **COPY THE TOKEN NOW** (you won't see it again!)

### Using the Token:
When Git asks for your password, paste the token instead of your actual password.

---

## Your Daily GitHub Workflow

From now on, every time you make changes:

```
1. Edit your files (in your code editor)
2. git add .                  (stage all changes)
3. git commit -m "message"    (save with a note)
4. git push origin main       (upload to GitHub)
```

That's it! You'll do these four steps over and over.

---

## Common Mistakes and How to Fix Them

### "I accidentally staged the wrong file!"
```bash
git reset HEAD filename.txt
```
This removes the file from staging (your changes are still there).

### "I committed too early!"
```bash
git commit --amend -m "New message"
```
This changes the message of your last commit.

### "I want to undo all my changes to a file!"
```bash
git checkout -- filename.txt
```
**Warning:** This deletes your changes! Make sure you want this.

### "My terminal is stuck!"
- Press `q` to exit
- Press `Ctrl + C` to cancel

---

## Quick Reference

| What You Want To Do | Command |
|---------------------|---------|
| Start tracking a folder | `git init` |
| See what's happening | `git status` |
| Track a file | `git add filename.txt` |
| Track all files | `git add .` |
| Save changes | `git commit -m "message"` |
| See history | `git log --oneline` |
| Send to GitHub | `git push origin main` |
| Get from GitHub | `git pull origin main` |

---

## What Are These Practice Files?

Here's what's in this folder for you to practice with:

| File | What It Is |
|------|------------|
| `sample_code.py` | A simple Python program that prints greetings |
| `notes.txt` | A text file with notes about Git commands |
| `shopping_list.txt` | A simple shopping list |

Feel free to edit these files and practice the Git commands!

---

## What to Do Next?

Now that you know the basics, here's what you can learn next:

1. **Branching** - Creating alternate versions of your code
2. **Merging** - Combining branches back together
3. **Gitignore** - Ignoring files you don't want to track
4. **Collaboration** - Working with others on GitHub

---

## Need More Help?

- Type `git --help` in your terminal
- Visit https://git-scm.com/docs
- Visit https://docs.github.com
