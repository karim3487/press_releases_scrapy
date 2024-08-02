# Press Releases Scraper

---

## Description:

This project is a web scraping application built with Scrapy to scrape press releases from different government websites and store them in a database.

---

## Getting Started:

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites:

- Python 3.10 installed on your system.
- PostgreSQL/SQLite3
- Poetry installed (for managing dependencies).

### Installation:
- Clone the repository:
```shell
git clone <repository_url>
```

- Navigate to the project directory:
```shell
cd telegram_repost_bot
```

- Install project dependencies using Poetry:
```shell
poetry install
```

- Set up your PostgreSQL database:
```shell
createdb mydbname
```

### Configuration:

- Rename `env_example` on `.env` and modify values

### Usage:

- Activate the virtual environment created by Poetry:

```shell
poetry shell
```

- Run the spiders:

```sh
scrapy crawl kmkr
scrapy crawl mchs
scrapy crawl nesk
```

- Schedule the spiders to run every 10 minutes using cron:

    - Open the cron table for editing:

        ```sh
        crontab -e
        ```

    - Add the following lines to the crontab file to schedule the spiders:

        ```sh
        */10 * * * * cd /path/to/your/project && /path/to/your/venv/bin/scrapy crawl kmkr >> /path/to/your/project/logs/kmkr.log 2>&1
        */10 * * * * cd /path/to/your/project && /path/to/your/venv/bin/scrapy crawl mchs >> /path/to/your/project/logs/mchs.log 2>&1
        */10 * * * * cd /path/to/your/project && /path/to/your/venv/bin/scrapy crawl nesk >> /path/to/your/project/logs/nesk.log 2>&1
        ```

        Replace `/path/to/your/project` with the actual path to your project directory.
        Replace `/path/to/your/venv` with the actual path to your virtual environment directory.

    - These cron jobs will run the `kmkr`, `mchs` and `nesk` spiders every 10 minutes and log the output to `kmkr.log` and `mchs.log` respectively.
