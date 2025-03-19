# Time-Capsule-Message-Scheduler-API

A RESTful API built with Flask that allows users to schedule messages for future delivery, acting as a digital time capsule. Messages are stored in a SQLite database and retrieved based on their scheduled dates.

## Features
- Schedule messages with a specific delivery date.
- Retrieve pending messages or those due today.
- Lightweight SQLite database for persistent storage.
- Secure configuration using environment variables.

## Tech Stack
- **Backend**: Python, Flask
- **Database**: SQLite
- **Libraries**: dotenv (for environment variables)

## Prerequisites
- Python 3.x
- pip (Python package manager)
- Git

## Setup Instructions
1. **Clone the Repository** 
   ```bash
   git clone https://github.com/your-username/Time-Capsule-Message-Scheduler-API.git
   cd Time-Capsule-Message-Scheduler-API
