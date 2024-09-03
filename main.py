import gspread
from google.oauth2.service_account import Credentials
import openai

openai.api_key = ''

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1rR1QIuDh8bM1FJrq3V07TD7e_2c1m4EcrPAfZgSHmvk"
sheet = client.open_by_key(sheet_id)

# values_list = sheet.sheet1.row_values(1)
# print(values_list)

#########################################################

def get_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(    
            model="gpt-4o", 
            # prompt=prompt,
            max_tokens=50,  
            temperature=0.7 ,
            messages= [
            { 'role': "system", 'content': "You are a helpful assistant." },
            {
                'role': "user",
                'content': f"{prompt}",
            },
    ],
        )
        print('response : ', response)
        return response["choices"][0]["message"]["content"]
    
    except Exception as e:
        return f"An error occurred: {e}"


######################################################## 
for i in range(1,2):
    question = sheet.sheet1.row_values(i)
    prompt = question[0]+' give me direct answer only !'
    print(prompt)

    response = get_chatgpt_response(prompt)
    print("Response from ChatGPT:", response)

    sheet.sheet1.update_cell(i,2,response)


