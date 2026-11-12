# Job Tracker

A command-line tool for tracking job applications: company, role, status,
dates and follow-ups.

> Work in progress — built as a Python learning project.

## Requirements

- Python 3.13.5
- [uv](https://docs.astral.sh/uv/)

## Setup

    git clone https://github.com/A1SHARIF/job-tracker.git
    cd job-tracker
    uv sync

## Running tests

    uv run pytest

## Roadmap

- [ ] Application model with status rules
- [ ] In-memory storage
- [ ] SQLite storage
- [ ] Command-line interface
- [ ] Follow-up dates that skip UK bank holidays