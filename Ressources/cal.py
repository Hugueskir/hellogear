
# Code marche maintenant mettre le data dans un json


from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

from SCOPES import SCOPES

print(SCOPES)


# If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/calendar']
# SCOPES = ['https://www.googleapis.com/auth/calendar.events']

# are we therevv

# Your VAR
# Your VAR
# Your VAR
# Your VAR

calid = "2htlq72gu386ot4batnafe2lrc@group.calendar.google.com"
cal_id = "2htlq72gu386ot4batnafe2lrc@group.calendar.google.com"
someID = "bzhsNjcxZ20yMGdyc21iM29sMGhoMTJkNzQgMmh0bHE3Mmd1Mzg2b3Q0YmF0bmFmZTJscmNAZw"

cal_name = "pypy"

# # Va cherche le data ranger dans Json file
# path_json = "events.json"
# with open(path_json, 'r') as f:
#     event_json = json.load(f)
# print(event_json)


# Your VAR
# Your VAR
# Your VAR
# Your VAR


def cal(event):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time


# -------------  Calling the calendar --------------

    print('Printing events from', cal_name)

    events_result = service.events().list(calendarId=calid, timeMin=now,
                                          maxResults=100, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])


# ---------------- Deleting ALL EVENTS ----------------------

    for event in events:
        service.events().delete(calendarId=cal_id,
                                eventId=event['id']).execute()


# ---------------- Creating EVENTS ----------------------

    # event est une variable puisée dans json file
    # event = event_json

    for k in range(len(event)):
        event[k] = service.events().insert(
            calendarId=cal_id, body=event[k]).execute()
        # print(k)
    # print('Event created: %s' % (event.get('htmlLink')))


# ---------------- Printing EVENTS ----------------------

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


# ------------------ LOOPING PROGRAM -----------------------
if __name__ == '__main__':
    cal()
