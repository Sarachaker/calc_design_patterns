from dotenv import load_dotenv
import os

# Load environment variables from .student_env file
load_dotenv('.student_env')

# Access environment variables
student_env = os.getenv("STUDENT_ENV")
student_api_key = os.getenv("STUDENT_API_KEY")

print(f"Student Environment: {student_env}")
print(f"Student API Key: {student_api_key}")
