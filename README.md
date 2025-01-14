# weather-dashboard-demo

A weather dashboard leveraging **OpenWeather API** and **AWS S3** to fetch, store, and display real-time weather data. This project demonstrates core **DevOps principles** and showcases cloud integration.

---

## Features
- **API Integration**: Fetch real-time weather data using OpenWeather API.
- **Cloud Storage**: Automatically stores weather data in AWS S3.
- **Multi-City Support**: Tracks and saves weather data for multiple cities.
- **Historical Tracking**: Timestamps all saved data for future reference.
- **Error Handling**: Graceful error handling for API and cloud operations.

---

## Project Architecture
![Project Architecture Diagram](path/to/your/diagram.png) *(optional)*

---

## Technologies Used
- **Programming Language**: Python
- **Cloud Provider**: AWS (S3)
- **External API**: OpenWeather API
- **Key Libraries**:
  - `boto3` (AWS SDK)
  - `requests`
  - `python-dotenv`

---

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Bigworm9/weather-dashboard-demo.git
   cd weather-dashboard-demo

---

## Create and activate a virtual environment

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

---
## Install dependencies

pip install -r requirements.txt

---

##  Create a .env file in the src/ folder

OPENWEATHER_API_KEY=your_openweather_api_key
AWS_BUCKET_NAME=your_s3_bucket_name

---

##  Run the project

python src/weather_dashboard.py

---

## Example Usage
After running the script, the weather data is saved in your specified S3 bucket under the weather-data/ folder in the AWS Console

---

##  weather-dashboard-demo/
│
├── src/                       # Source code for the weather dashboard
│   ├── weather_dashboard.py    # Main script to fetch weather data and save to S3
│   └── __init__.py             # Initialization file
│
├── .gitignore                  # Git ignore file
├── .env                        # Environment variables (for your API key and AWS bucket)
├── README.md                   # Project documentation
├── requirements.txt            # List of dependencies
└── tests/                      # Unit tests (if any)

---

## What I learned

AWS S3 bucket creation and management
Environment variable management for secure API keys
Python best practices for API integrationGit 
Git workflow for project developement
Error handling in distrubuted systems
Cloud resource management

---

## Errors Troubleshooting and Fixes

Error 1: Changes not staged for commit
Mistake:
While working in the project directory, I encountered a message stating:
Changes not staged for commit: 
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
This was due to the presence of untracked files in the repository, which weren’t yet committed to Git.

Correction:
I ran the following commands to clean up untracked files: git clean -fd
This cleared the unnecessary untracked files and directories, allowing me to proceed with my work without errors.

Error 2: Invalid location constraint for the S3 bucket
Mistake:
When running the script to create an S3 bucket, I encountered the following error:
An error occurred (IllegalLocationConstraintException) when calling the CreateBucket operation: The us-west-2 location constraint is incompatible for the region specific endpoint this request was sent to.
This error occurred because I was using an incorrect region for the S3 bucket creation (us-west-2), which was incompatible with the default endpoint.

Correction:
I corrected the region by changing the location constraint to the correct AWS region (us-west-2) in the script where the bucket was being created:
'LocationConstraint': 'us-west-2'
This fixed the error and allowed me to successfully create the S3 bucket.

Error 3: Issues with .gitignore not working as expected
Mistake:
I noticed that some files, such as .vscode/ and .aws/, were showing up in my Git repository, even though I had tried to exclude them with the .gitignore file. This led to an accumulation of unnecessary files in my repository.
Correction:
I ensured that .gitignore contained the correct file paths to exclude unwanted files like .vscode/, .aws/, and other unnecessary directories. I then staged the changes and committed the .gitignore file correctly.

Final Notes:
Throughout the process, I learned important troubleshooting skills, especially in cleaning up unnecessary files, fixing S3-related errors, and resolving issues with GitHub pushes. This will serve as a guide for future projects, ensuring smooth version control and deployment processes.

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---
