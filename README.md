# veeammaclogparse
Veeam Agent for Mac Log Parse

### Log Processing Program for Mac

This program is designed to handle log files on Mac. To get started, follow these steps:

1. Download the repository and unzip it.
2. Create a Google account and obtain a password for the application.
3. Create and populate the .env file.
4. [Instructions]

**Setting Up a Cron Job for Mac**:

To schedule the execution of `main.py` at 18:31 every day, follow these steps:

1. Open Terminal.
2. Type `crontab -e` and press Enter.
3. In the crontab file, add the following line:

```shell
31 18 * * * /usr/bin/python3 /path/to/main.py >> /path/to/logfile.log 2>&1
```

Replace `/path/to/main.py` with the actual path to your `main.py` file.

4. Save and exit the crontab file.

This will run the script `main.py` at 18:31 every day. The output will be logged to `logfile.log`.

---

## Certificate verify failed(MAC OS ONLY)

https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org[https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org]
