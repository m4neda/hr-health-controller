import fitbit
import os


def load_fitbit_client():
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
    REFRESH_TOKEN = os.environ.get('REFRESH_TOKEN')
    authd_client = fitbit.Fitbit(
        CLIENT_ID,
        CLIENT_SECRET,
        access_token=ACCESS_TOKEN,
        refresh_token=REFRESH_TOKEN,
    )

    return authd_client


def fetch_activities(fitbit_client):
    return fitbit_client.activities()


def fetch_resting_hr_rate(activities):
    return activities['summary']['restingHeartRate']


def main():
    fitbit_client = load_fitbit_client()
    activities = fetch_activities(fitbit_client)
    resting_hr_rate = fetch_resting_hr_rate(activities)
    print(resting_hr_rate)


if __name__ == '__main__':
    main()