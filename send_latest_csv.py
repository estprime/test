import os
import glob
import smtplib
from email.message import EmailMessage
from datetime import datetime

def find_latest_csv(folder: str) -> str:
    pattern = os.path.join(folder, "ROJEN*.csv")
    csv_files = glob.glob(pattern)
    if not csv_files:
        raise FileNotFoundError(f"No files match {pattern}")
    # assume filename ends with YYYYMMDD or MMDD digits
    def extract_key(path: str):
        name = os.path.basename(path)
        # Example: ROJEN0520.csv -> 0520
        digits = ''.join(filter(str.isdigit, name))
        return int(digits)
    latest = max(csv_files, key=extract_key)
    return latest

def send_mail(sender: str, password: str, recipient: str, subject: str, body: str, attachment_path: str):
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)

    with open(attachment_path, 'rb') as f:
        data = f.read()
    filename = os.path.basename(attachment_path)
    msg.add_attachment(data, maintype='text', subtype='csv', filename=filename)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)


def main():
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    target_dir = os.path.join(desktop, 'ROJEN')
    latest_csv = find_latest_csv(target_dir)

    sender = os.environ['EMAIL_USERNAME']
    password = os.environ['EMAIL_PASSWORD']
    recipient = 'odakecho1234@gmail.com'
    subject = f"Latest ROJEN file {datetime.now().strftime('%Y-%m-%d')}"
    body = 'Attached is the latest ROJEN CSV file.'

    send_mail(sender, password, recipient, subject, body, latest_csv)

if __name__ == '__main__':
    main()
