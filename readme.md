# 🔐 Automated Email Alias Grabber

This Python script **automates pulling SimpleLogin email aliases** using the **SimpleLogin API**. It saves the email aliases in a **JSON** file, ready for input into another script/automation.

---

## 🚀 Features

- 📡 **Automated email grabbing** – Gets all SimpleLogin email aliases you have.
- 🛠 **JSON output** – Saves output in JSON for input into script/automation.
- 🔁 **Runs Automatically** – Can be scheduled with Task Scheduler/Cron job.

---

## 🛠 Installation & Setup

### 1️⃣ Prerequisites

- **Python 3.x**
- **SimpleLogin account**
- Windows **Task Scheduler**/Cron (for automation)

### 2️⃣ Install Dependencies

```bash
pip install requests
```

### 3️⃣ Get SimpleLogin API key

1. Log into your SimpleLogin account.
2. Click "API Keys" in drop down menu on username (top right).
3. Enter password to enter sudo mode.
4. Enter name for API key and click "Create" button to generate API key.
5. Copy API key and save into environment variable.

### 4️⃣ Configure Environment Variables

Set the following environment variable:

``` bash
simple_login_api_key = "your api key"
```

### 5️⃣ Automate with Task Scheduler/Cron Jobs

Task Scheduler

1. Open Task Scheduler (taskschd.msc).
2. Create a new task.
3. Set trigger: Every X days/weeks.
4. Set action: Run Python with the script.

Cron Job

1. Run ```crontab -e```
2. Add ```0 0 */2 * * /usr/bin/python3 /path/to/script.py```
3. Replace ```/path/to/script.py``` with the actual path to your script
4. Adjust when and how often you would like the script to run (command in 2. runs every 2 days at mightnight(00:00))
5. Note: check documentation for help on how to use cron jobs

---

### 📌 How It Works

1. Queries /aliases API endpoint.
2. loops through each item in json output and adds the email address to list.
3. Saves all email aliases and their state (enabled/disabled) to JSON file.

---

### License

This project is licensed under the **MIT License**. Feel free to **use, modify, and distribute** it, but **please provide attribution** by keeping my name in the copyright notice.

If you improve the script or use it in a project, a **shoutout** or a mention would be appreciated! 😊
