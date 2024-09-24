import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'config')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'notebooks')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data')))


from google.cloud import storage
from google.oauth2 import service_account

# Set the environment variable for the Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ''

# Verify that it has been set correctly
print("GOOGLE_APPLICATION_CREDENTIALS:", os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))

def main():
    print(".......")
if __name__ == "__main__":
    main()