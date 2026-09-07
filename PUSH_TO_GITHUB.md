# Push to GitHub - Step by Step Guide for Beginners

This guide will help you upload your practice files to GitHub so they're safely stored online.

---

## What Are We Doing?

```
YOUR COMPUTER                          GITHUB (WEBSITE)
┌─────────────────┐                   ┌─────────────────┐
│  Your files     │    push ─────────►│  Online copy    │
│  (local repo)   │                   │  (remote repo)  │
└─────────────────┘                   └─────────────────┘
```

You'll send (push) your code from your computer to your GitHub account.

---

## Step 1: Create a GitHub Account

If you already have a GitHub account, skip to Step 2.

1. Open your web browser and go to **https://github.com**
2. Click the **Sign up** button
3. Enter your email address
4. Create a **password**
5. Choose a **username** (this will be part of your URL!)
6. Verify you're human (complete the puzzle)
7. Click **Create account**

**Tip:** Choose a simple username you'll be comfortable sharing.

---

## Step 2: Create a New Repository

A **repository** (or "repo") is like a folder on GitHub where your project lives.

### 2a: Start Creating a New Repo

1. After logging into GitHub, look at the top-right corner
2. Click the **+** icon (plus sign)
3. A menu appears - click **New repository**

```
[Your Avatar]  ▼   +
                   ├── New repository
                   ├── Import repository
                   └── ...
```

### 2b: Fill In the Details

You'll see a form with these fields:

| Field | What to Type |
|-------|-------------|
| **Repository name** | `git-practice` (or any name you want) |
| **Description** | `Learning Git with practice files` (optional) |
| **Public** or **Private** | Click **Public** (it's free!) |
| **Add a README** | ❌ DO NOT check this |
| **Add .gitignore** | Leave as "None" |

It should look like this:
```
┌─────────────────────────────────────┐
│ Repository name: git-practice       │
│ Description: Learning Git           │
│ ○ Public  ● Private                 │
│ ☐ Add a README file                 │
│ .gitignore: None ▼                  │
│                                     │
│         [Create repository]         │
└─────────────────────────────────────┘
```

### 2c: Click Create!

After clicking, you'll see a page that says "Quick setup".

**Keep this page open!** You need the URL from it.

The URL will look like:
```
https://github.com/YOURUSERNAME/git-practice
```

---

## Step 3: Connect Your Computer to GitHub

Now your computer needs to know about your GitHub repository.

### 3a: Find Your Repository URL

On the GitHub page you just created, look for a green button that says **"Code"**. Click it. A box appears with a URL. It should be:
```
https://github.com/YOURUSERNAME/git-practice.git
```

Click the clipboard icon to copy this URL (or select and copy it manually).

### 3b: Add the URL to Git

In your terminal, type this command (paste your URL instead of the placeholder):

```bash
git remote add origin https://github.com/YOURUSERNAME/git-practice.git
```

**What does this do?**
- "remote" = a connection to another computer (GitHub)
- "origin" = a nickname for that connection (standard name)
- Your computer now knows where to send your files

### 3c: Verify It Worked

```bash
git remote -v
```

You should see something like:
```
origin  https://github.com/YOURUSERNAME/git-practice.git (fetch)
origin  https://github.com/YOURUSERNAME/git-practice.git (push)
```

This confirms the connection is set up!

---

## Step 4: Save Your Files (Git Commit)

Before sending to GitHub, your files need to be saved (committed) locally first.

### 4a: Check What Files Git Sees

```bash
git status
```

Git will list all your files. They'll be shown as "Untracked files" (Git doesn't know about them yet).

### 4b: Tell Git to Track All Files

```bash
git add .
```

The dot (`.`) means "everything in this folder".

### 4c: Save Your Changes

```bash
git commit -m "Add my first Git practice files"
```

**What did you just do?**
- Git took a "snapshot" of all your files
- The message describes what you added
- Your changes are now safely stored on YOUR computer

---

## Step 5: Send to GitHub (Git Push)

Now let's upload your files to GitHub!

```bash
git push -u origin main
```

**What does this mean?**
- `push` = send to GitHub
- `origin` = to the repository called "origin" (your GitHub repo)
- `main` = to the "main" branch (don't worry about branches yet)
- `-u` = remember these settings for future pushes

### 5a: Enter Your Credentials

GitHub will ask for your username and password:

```
Username: YOURUSERNAME
Password: (your GitHub password)
```

**Important:** If you have two-factor authentication (2FA) enabled, you need a **Personal Access Token** instead of your password.

#### How to Get a Token (if password doesn't work):

1. Go to GitHub.com
2. Click your profile picture → **Settings**
3. Scroll down to **Developer settings** (bottom of page)
4. Click **Personal access tokens** → **Tokens (classic)**
5. Click **Generate new token**
6. Give it a name (like "My Git Practice")
7. Check the **repo** checkbox (first one)
8. Click **Generate token**
9. **COPY THE TOKEN NOW!** (you won't see it again)

When GitHub asks for your password, paste this token instead.

---

## Step 6: Check Your GitHub Repository

1. Go to `https://github.com/YOURUSERNAME/git-practice`
2. **Refresh the page** if you already have it open
3. You should see all your files listed!
4. Click on any file to see its contents

**🎉 Congratulations! Your code is now on GitHub!**

---

## Your Daily GitHub Workflow

Every time you make changes to your files, you'll do these 4 steps:

```
1. Edit your files (in your code editor)
         │
         ▼
2. git add .                  (select all changes)
         │
         ▼
3. git commit -m "message"    (save changes locally)
         │
         ▼
4. git push origin main       (upload to GitHub)
```

**Example:**
1. You edit `notes.txt` to add new notes
2. You stage the changes with `git add .`
3. You commit with `git commit -m "Add more notes"`
4. You push with `git push origin main`

---

## Troubleshooting

### Problem: "Permission denied" error

**Solutions:**
1. Double-check your username is spelled correctly
2. Make sure you're using your password or token correctly
3. If you enabled 2FA, you MUST use a token (see above)

### Problem: "Could not resolve host"

This means your computer can't reach GitHub. Check your internet connection.

### Problem: "Repository does not exist"

You might have the wrong URL. Go to GitHub and check your repository exists.

### Problem: "Nothing to commit"

This means you haven't made any changes since your last commit. All your files are already saved!

### Problem: "Please tell me who you are"

Git doesn't know your name yet. Run these commands:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## What If I Make Mistakes?

Git is designed to be safe! Here are some common fixes:

### Undo Staging (file is staged but not committed):
```bash
git reset HEAD filename.txt
```

### Undo a Commit (you committed but didn't push):
```bash
git commit --amend -m "New message"
```

### Discard All Changes to a File:
```bash
git checkout -- filename.txt
```
**Warning:** This permanently deletes your changes!

---

## Quick Reference Card

| What You Want To Do | Command |
|---------------------|---------|
| Connect to GitHub | `git remote add origin <URL>` |
| Check the connection | `git remote -v` |
| See what changed | `git status` |
| Track all files | `git add .` |
| Save everything | `git commit -m "message"` |
| Upload to GitHub | `git push -u origin main` |
| Download from GitHub | `git pull origin main` |

---

## What's Next?

Once your code is on GitHub, you can:

- **Share your URL** with friends or potential employers
- **Add collaborators** so others can work on your project
- **Enable GitHub Pages** to make a website from your files
- **Keep practicing** by making changes and pushing them!

---

## Need Help?

- **GitHub Help:** https://docs.github.com
- **Git Help:** https://git-scm.com/docs
- **Google:** Search for your error message - someone has probably solved it!
