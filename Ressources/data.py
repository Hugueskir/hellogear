from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
from SCOPES import SCOPES

allo = ['all', 'as']
# If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# service = googleapiclient.discovery.build(
#     'calendar', 'v3', developerKey=api_key)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_2 = "1Bi8_jqtMTKN21YdDpyi1YA44dgg0KNkE-v73JEdwO0g"
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

ident = "1Bi8_jqtMTKN21YdDpyi1YA44dgg0KNkE-v73JEdwO0g"
ident_id = 0
range_name = 'A1:E1000'


def data():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
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

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=ident,
                                range=range_name).execute()
    values = result.get('values', [])

    event_dict = {
        'summary': 'Projet Manquant',
        'description': 'Location',
        'location': 'Lieu Manquant',
        'start': {
            'dateTime': '',
            'timeZone': 'America/Toronto',

        },

        'end': {
            'dateTime': '',
            'timeZone': 'America/Toronto',
        }
    }

    almanac = []
    if not values:
        print('No data found.')
    else:

        i = 0
        for row in values:
            # if not values:
            #     pass
            # else:
            if i > 0:
                # j = values[i][0]

                new_dict = 'new'+str(i)
                new_dict = event_dict.copy()
                try:
                    new_dict["desciption"] = values[i][0]
                    new_dict["location"] = values[i][1]
                    new_dict["summary"] = values[i][2]
                    new_dict["start"]["dateTime"] = values[i][3] + \
                        'T00:00:00'
                    new_dict["end"]["dateTime"] = values[i][4]+'T23:59:00'

                    almanac.append(new_dict)

                except IndexError:
                    pass

            i += 1

    return almanac

    # print(event_dict)
    # print(*almanac, sep="\n"*2)

    # with open('events.json', 'w') as fp:
    #     json.dump(almanac, fp)


if __name__ == '__main__':
    data()
