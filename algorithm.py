import math
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("pythonCredentials.json")
firebase_admin.initialize_app(cred)

db = firebase_admin.firestore.client()



def calculateMatch(PUID):
    users = list(db.collection(u'formData').stream())

    docs = db.collection(u'formData').stream()

    frames = []

    for doc in docs:
        userResponses = doc.to_dict()
        frames.append(pd.DataFrame(userResponses, index=[0,]))

    finalized_dataframe = pd.concat(frames)

    name_column = finalized_dataframe.pop('name')
    major_column = finalized_dataframe.pop('major')
    number_column = finalized_dataframe.pop('number')
    gender_column = finalized_dataframe.pop('gender')
    year_column = finalized_dataframe.pop('year')
    puid_column = finalized_dataframe.pop('puid')

    finalized_dataframe.insert(0, 'Gender', gender_column)
    finalized_dataframe.insert(0, 'Major', major_column)
    finalized_dataframe.insert(0, 'Year', year_column)
    finalized_dataframe.insert(0, 'Phone Number', number_column)
    finalized_dataframe.insert(0, 'PUID', puid_column)
    finalized_dataframe.insert(0, 'Name', name_column)

    total_data = []

    df_input = finalized_dataframe

    names = df_input.iloc[: , 0:2] # Get a dataframe of all the names

    person_info = df_input.iloc[: , 0:6]  # Get a dataframe of person information

    preference_info_temp = df_input.iloc[:, 36:37] # Get a dataframe of person preference info

    response_data_temp = df_input.iloc[: , 6:36] # Get a dataframe of all the responses

    response_frames = [names, response_data_temp]
    preference_frames = [names, preference_info_temp]

    response_data = pd.concat(response_frames, axis=1) # Concating the names and response dataframes together
    preference_data = pd.concat(preference_frames, axis=1) # Concating the names and preference dataframes together

    studentIdNumber = int(PUID) #Replace with user input

    student_response = response_data[response_data['PUID'] == str(studentIdNumber)]
    student_preference = preference_data[preference_data['PUID'] == str(studentIdNumber)]

    #return preference_data[preference_data['PUID']]
    gender_preference = int(student_preference['interested_gender'])

    # print(student_response) #Use to iterate through student responses


    person_scores = []


    for row in response_data.iterrows(): # Iterating through the rows

        currentId = row[1][1]


        if studentIdNumber!= currentId: # Checking to make sure not the same person

            currentName = row[1][0]


            score = 0 # Need to iterate through 2-32 indexes

            for index in range(2, 32):

                student_choice = student_response.loc[0][index]
                current_choice = row[1][index]

                student_choice = int(student_choice)
                current_choice = int(current_choice)

                score += pow( (current_choice - student_choice), 2)

                percentage = 1 / ( 1 + pow( math.e, (0.045 * ( score - 67.5 ) ) ) )

                percentage = (percentage) * 100

                percentage = round(percentage, 2)

                percentage = str(percentage)

                percentage = percentage + "%"


            person_scores.append([currentName, currentId, percentage])



    person_scores = sorted(person_scores, key = lambda x: x[2], reverse=True)

    for index in range(0, len(person_scores)):

        if person_scores[index][1] == str(studentIdNumber):

            person_scores.pop(index)

        break;


    final_results = []

    # ReType to get id number curr3ent person gender intermeadgte and all values

    for index in range(0, len(person_scores)): #Note for personal information to check, 0-M, 1-F, 2-NB

        id_number = person_scores[index][1]

        current_person = person_info[person_info['PUID'] == str(id_number)]

        current_gender = int(current_person['Gender'])

        intermediate = person_scores[index]


        if gender_preference == 0:

            if current_gender == 0:

                intermediate.append('Male')

                final_results.append(intermediate)



        elif gender_preference == 1:

            if current_gender == 1:

                intermediate.append('Female')

                final_results.append(intermediate)



        elif gender_preference == 2:

            if current_gender == 2:

                intermediate.append('Non-Binary')

                final_results.append(intermediate)



        elif gender_preference == 3:

            if current_gender == 0:

                intermediate.append('Male')

                final_results.append(intermediate)

            elif current_gender == 1:

                intermediate.append('Female')

                final_results.append(intermediate)



        elif gender_preference == 4:

            if current_gender == 0:

                intermediate.append('Male')

                final_results.append(intermediate)

            elif current_gender == 2:

                intermediate.append('Non-Binary')

                final_results.append(intermediate)



        elif gender_preference == 5:

            if current_gender == 1:

                intermediate.append('Female')

                final_results.append(intermediate)

            elif current_gender == 2:

                intermediate.append('Non-Binary')

                final_results.append(intermediate)

        else:

            if current_gender == 0:

                intermediate.append('Male')

                final_results.append(intermediate)

            elif current_gender == 1:

                intermediate.append('Female')

                final_results.append(intermediate)

            else:

                intermediate.append('Non-Binary')

                final_results.append(intermediate)
    return final_results