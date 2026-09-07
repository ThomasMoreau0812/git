# Git & GitHub Instruction Manual

## How Git Push Works

```
git init          → Create repository
git add <file>    → Stage files
git commit -m ""  → Save changes locally
git push          → Upload to GitHub
```

---

## 1. Install gh (GitHub CLI) on Ubuntu

```bash
sudo apt update && sudo apt install gh -y
```

If the package is not found, add the official repository:

```bash
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update && sudo apt install gh -y
```

---

## 2. Authenticate with GitHub

```bash
gh auth login
```

Follow the prompts:
- Select `GitHub.com`
- Select `HTTPS`
- Select `Login with a web browser`
- Copy the one-time code
- Press Enter to open browser
- Paste the code and authorize

---

## 3. Configure Git (one time)

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

---

## 4. Clone a Repository

```bash
git clone https://github.com/USERNAME/REPO.git
```

---

## 5. Make Changes and Push

```bash
# Check status
git status

# Stage all files
git add .

# Commit with message
git commit -m "Your message"

# Push to remote
git push
```

---

## 6. Set Upstream Branch (if needed)

```bash
git push --set-upstream origin main
```

Or configure Git to do it automatically:

```bash
git config --global push.autoSetupRemote true
```

---

## Useful Commands

| Command | Description |
|---------|-------------|
| `git status` | Check current state |
| `git log --oneline` | View commit history |
| `git remote -v` | View remote connections |
| `git branch` | List branches |
| `git checkout -b name` | Create and switch branch |
| `git merge <branch>` | Merge branch into current |
| `git pull` | Download from remote |

---

## Tips

- Commit often with clear messages
- Always pull before pushing: `git pull`
- Use `git status` frequently to check your state
