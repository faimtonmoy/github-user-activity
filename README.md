# GitHub User Activity Tracker

A simple Python CLI tool that fetches and displays recent GitHub activity for any user using the GitHub Events API.

## 🔗 Project URL

https://roadmap.sh/projects/github-user-activity

---

## 🚀 Features

- Fetches recent public activity of a GitHub user

- Groups **push events by repository** (commit counts)

- Displays meaningful messages for different event types:
  - Push events
  - Repository/branch creation & deletion
  - Issues & pull requests
  - Stars and forks
  - Comments on issues

- Clean and readable output format

---

## 🛠️ Tech Stack

- Python 3
- `requests` library
- GitHub REST API

---

## 📦 Installation

1. Clone the repository or copy the script:

```bash
git clone https://github.com/faimtonmoy/github-user-activity
cd github-user-activity
```

2. Install dependencies:

```bash
pip install requests
```

---

## ▶️ Usage

Run the script:

```bash
python activity-tracker.py
```

Enter a GitHub username when prompted:

```
Enter your user name: torvalds
```

---

## 📊 Example Output

```
- Pushed 3 commits to torvalds/linux
- Created repository torvalds/test-repo
- Opened issue #123 in torvalds/linux
- Starred python/cpython
- Forked repo-name to username/repo-name
```

---

## 🧠 How It Works

1. Takes a GitHub username as input

2. Calls GitHub API:

   ```
   https://api.github.com/users/{username}/events
   ```

3. Processes the response:
   - Groups push events by repository
   - Formats other events into readable messages

4. Prints formatted activity to the console

---

## ⚠️ Limitations

- Only fetches **public events**
- GitHub API returns a limited number of recent events (usually 30)
- No authentication → may hit **rate limits** if used frequently

---

## 💡 Possible Improvements

- Add GitHub authentication (token support)
- Show timestamps for each activity
- Filter by event type
- Export results to a file (JSON/CSV)
- Build a web UI (React / Next.js)

---

## 📄 License

This project is open-source and free to use.

---

## 🙌 Acknowledgements

- GitHub REST API
