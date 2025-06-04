# Remote Disk Check with Email Alerts

This repo contains a GitHub Actions workflow that checks disk usage on remote servers via SSH and sends email alerts if disk usage exceeds a threshold or if a server is unreachable.

## Setup

1. Replace `your_ssh_user` in `check_disk.sh` with your SSH username.
2. Add your remote servers IPs to `servers.txt`.
3. Set up secrets in your GitHub repository:
   - `SMTP_SERVER` (e.g., smtp.gmail.com)
   - `SMTP_PORT` (e.g., 587)
   - `SMTP_USER` (your email login)
   - `SMTP_PASSWORD` (your email password or app-specific password)
   - `EMAIL_FROM` (sender email)
   - `EMAIL_TO` (recipient email)

## Usage

Trigger the workflow manually from the GitHub Actions tab.

## Notes

- Make sure your SSH keys are configured to allow the workflow runner to SSH into your servers.
- Email alerts can be disabled by setting `SEND_EMAIL` to `false` in the workflow.
