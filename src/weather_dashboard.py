# src/weather_dashboard.py

import os
import json
import boto3
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class WeatherDashboard:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.bucket_name = os.getenv('AWS_BUCKET_NAME')
        self.s3_client = boto3.client('s3','us-west-2')

    def create_bucket(self):
        """Create S3 bucket if it doesn't exist"""
        try:
            self.s3_client.create_bucket(
                Bucket=self.bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': 'us-west-2'
                }
            )
            print(f"Created bucket: {self.bucket_name}")
        except self.s3_client.exceptions.BucketAlreadyExists:
            print(f"Bucket already exists: {self.bucket_name}")
        except Exception as e:
            print(f"Error creating bucket: {e}")
            raise

    def fetch_weather(self, city):
        """Fetch weather data from OpenWeather API"""
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def save_to_s3(self, data, city):
        """Save weather data to S3"""
        if not data:
            return False

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f"weather-data/{city}_{timestamp}.json"
        
        try:
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=file_name,
                Body=json.dumps(data),
                ContentType='application/json'
            )
            print(f"Saved weather data to {file_name}")
            return True
        except Exception as e:
            print(f"Error saving to S3: {e}")
            return False

def main():
    try:
        dashboard = WeatherDashboard() 

        # Create S3 bucket
        dashboard.create_bucket()

        # List of cities to track
        cities = ["Seattle", "New York", "San Francisco"]

        for city in cities:
            print(f"\nProcessing weather data for {city}")
            weather_data = dashboard.fetch_weather(city)
            if weather_data:
                dashboard.save_to_s3(weather_data, city)
                print(f"Successfully processed {city}")
            else:
                print(f"Failed to process {city}")

    except Exception as e:
        print(f"Main execution failed: {e}")

if __name__ == "__main__":
    main()

