# ROJEN Mailer

This repository includes a Python script that emails the latest `ROJEN*.csv`
file from the Desktop `ROJEN` folder.

## Usage

1. Install Python 3 and required dependencies:
   ```bash
   pip install --upgrade pip
   pip install schedule
   ```

2. Set environment variables with your Gmail address and app password:
   ```bash
   export EMAIL_USERNAME='your_gmail@gmail.com'
   export EMAIL_PASSWORD='your_app_password'
   ```
   *Google requires an app password when two-factor authentication is enabled.*

3. Run the script manually:
   ```bash
   python send_latest_csv.py
   ```

4. To send the file every day at 9:00, add a cron job:
   ```cron
   0 9 * * * /usr/bin/env python /path/to/repo/send_latest_csv.py
   ```

The script finds the newest file in `~/Desktop/ROJEN` whose name begins with
`ROJEN` and ends with `.csv`, then sends it to `odakecho1234@gmail.com`.
