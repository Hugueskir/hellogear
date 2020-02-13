
# Code marche maintenant mettre le data dans un json


from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
import sys


from SCOPES import SCOPES

# print(SCOPES)


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
path_json = "events.json"
with open(path_json, 'r') as f:
    event_json = json.load(f)
# print(event_json)


# Your VAR
# Your VAR
# Your VAR
# Your VAR


def cal(userEvent):

    # def cal(userEvent):
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

    # print('Printing events from', cal_name)

    events_result = service.events().list(calendarId=calid, timeMin=now,
                                          maxResults=100, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])


# ---------------- grabing old events ALL EVENTS ----------------------
# prior to deletion if parsing is succefull
    old_list = []

    for old_event in events:
        # print(calendarId)
        # service.events().delete(calendarId=cal_id,
        #                         eventId=event['id']).execute()

        old_event = service.events().get(
            calendarId=cal_id, eventId=old_event['id']).execute()

        old_list.append(old_event['id'])

    # print(old_list)


# ---------------- Creating EVENTS ----------------------

    # event est une variable puisée dans json file (deprecated INFO)
    # event = event_json (deprecated INFO)

    for k in range(len(userEvent)):

        try:

            userEvent[k] = service.events().insert(
                calendarId=cal_id, body=userEvent[k]).execute()

            deleteGO = True

        except HttpError as err:

            # print(sys.exc_info()[1])

            if err.resp.status in [400, 404]:

                if err.resp.get('content-type', '').startswith('application/json'):
                    reason = json.loads(err.content).get(
                        'error').get('errors')[0].get('message')

            print('\n', "Veuillez remplir tous les champs")
            print("L'événement comportant l'erreur a été ignoré")
            exit()
            #         print(reason)

            # service.events().delete(calendarId=cal_id,
            #                         eventId=userEvent[k]).execute()

            deleteGO = False


# ---------------- Printing EVENTS ----------------------
# TB Shoot les events apparaissent avec un délai
    # print(events)
    # if not events:
    #     print('No upcoming events found.')
    # for event in events:
    #     start = event['start'].get('dateTime', event['start'].get('date'))
    #     print(start, event['summary'])

# ---------------- deleting old EVENTS ----------------------

    if deleteGO:

        for event2go in old_list:

            service.events().delete(calendarId=cal_id,
                                    eventId=event2go).execute()


# ------------------ LOOPING PROGRAM -----------------------
if __name__ == '__main__':
    cal(event_json)
