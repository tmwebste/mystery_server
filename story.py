import os
import json
import random

import openai
from dotenv import dotenv_values

# Load the .env file
config = dotenv_values('.env')

# Access the specific key
KEY = config.get('KEY')

openai.api_key = KEY



characterBackgroundTemplate = {
                    "firstName":"null",
                    "lastName":"null",
                    "age":"null",
                    "occupation":"null",
                    "backstory":"null",
                    "bias":"null",
                    "connections":["victim"]
                }

characterResponseTemplate = {
    "responseSentament": "null",
    "response": "null"
}

def createCharacterAttributes():
    print("creating character attributes")
    return {
                "_comments":"all of theses should be float values between 0 and 1",
                "saddness":random.uniform(0.0, 1.0),
                "happiness":random.uniform(0.0, 1.0),
                "anger":random.uniform(0.0, 1.0),
                "anxiety":random.uniform(0.0, 1.0),
                "fear":random.uniform(0.0, 1.0),
            }

def createStoryTheme(storyYear):
    print("creating story theme")
    instructions = f"freate a 1 word theme for the world for a murder mystery set in the year {storyYear}. Only respont with a single word and do not provide any explaination."
    chat_completion = openai.chat.completions.create(model="gpt-3.5-turbo", 
                                                    messages=[{"role": "user", 
                                                                "content": f"{instructions}"}]).choices[0].message.content
    print(chat_completion)
    return chat_completion

def createStoryDescription(storyYear, storyTheme):
    print("creating story description")
    instructions = f"Create a paragraph describing the situation for a murder mystery in the theme of {storyTheme} in the year {storyYear} "
    chat_completion = openai.chat.completions.create(model="gpt-3.5-turbo", 
                                                messages=[{"role": "user", 
                                                            "content": f"{instructions}"}]).choices[0].message.content
    print(chat_completion)
    return chat_completion

def createOneWord(request):
    instructions = f"{request}. Only respond with a single word and do not provide any explaination."
    chat_completion = openai.chat.completions.create(model="gpt-3.5-turbo", 
                                                    messages=[{"role": "user", 
                                                                "content": f"{instructions}"}]).choices[0].message.content
    return chat_completion

def createCharacterBackground(storyYear, storyTheme, backgroundTemplate):
    print("creating character background")
    instructions = f"using this json template, replace all null values with character background information to support a {storyTheme} themed mystery murder in the year {storyYear}. Please consider the (_comments) within the template, the Json object should have narative consistancy with the theme. None of the characters should be detectives or investigators and they should all be pretty suspicious. All of the informationb should be known. Ensure the json matches all the requests and has no remaining null values. Please respond with only the completed json object and no comments, do not respond with any comments. "

    chat_completion = openai.chat.completions.create(model="gpt-3.5-turbo", 
                                                messages=[{"role": "user", 
                                                            "content": f"{instructions} {json.dumps(backgroundTemplate)}"}]).choices[0].message.content
    print(chat_completion)
    return json.loads(chat_completion)

storyTheme = ''
storyDescription = ''
weapon = ''

def createStoryTemplate():
    storyYear = random.randint(1800, 2100)
    storyTheme = createStoryTheme(storyYear)
    storyDescription = createStoryDescription(storyYear, storyTheme)
    weapon = createOneWord(f"pick a murder weapon matching the worlds theme {storyTheme} for this case {createStoryDescription}")
    return{
        "game":{
            "playing":"false",

            "story":{
                "year": storyYear,
                "theme":storyTheme,
                "synopsys":storyDescription,
                "numberOfCharacters":5,
                "evidence":{
                    "_wittnessesComment":"whitnesses should be a list of a sebset of all the characters",
                    "weapon":weapon,
                    "witnesses":"null"
                }
            },

            "characters":{
                "_comments":"fill this sections with several characters (this should match the numberOfCharacters value) that fit the story theme, only one person should be guilty",
                "judge":{
                    "_comments":"the judge should never be guilty",
                    "guilty":"false", 
                    "attributes":createCharacterAttributes(),
                    "background":createCharacterBackground(storyYear, storyTheme, characterBackgroundTemplate ),
                    "response":{
                        "responseSentiment":"null",
                        "responseText":"null"
                    }
                    
                },
                "character1":{
                    "_comments":"the judge should never be guilty",
                    "guilty":"false", 
                    "attributes":createCharacterAttributes(),
                    "background":createCharacterBackground(storyYear, storyTheme, characterBackgroundTemplate ),
                    "response":{
                        "responseSentiment":"null",
                        "responseText":"null"
                    }
                    
                },
                "character2":{
                    "_comments":"the judge should never be guilty",
                    "guilty":"false", 
                    "attributes":createCharacterAttributes(),
                    "background":createCharacterBackground(storyYear, storyTheme, characterBackgroundTemplate ),
                    "response":{
                        "responseSentiment":"null",
                        "responseText":"null"
                    }
                    
                },
                "character3":{
                    "_comments":"the judge should never be guilty",
                    "guilty":"false", 
                    "attributes":createCharacterAttributes(),
                    "background":createCharacterBackground(storyYear, storyTheme, characterBackgroundTemplate ),
                    "response":{
                        "responseSentiment":"null",
                        "responseText":"null"
                    }
                    
                },
                "character4":{
                    "_comments":"the judge should never be guilty",
                    "guilty":"true", 
                    "attributes":createCharacterAttributes(),
                    "background":createCharacterBackground(storyYear, storyTheme, characterBackgroundTemplate ),
                    "response":{
                        "responseSentiment":"null",
                        "responseText":"null"
                    }
                    
                }
            }
        }
    }


def exportjson(data):
    print("Dumping JSON file ")
    with open(f"json_data\data{random.randint(0,9999)}.json", 'w') as f:
        json.dump(data, f)


# print(storyDescription)
# print(createCharacterBackground(storyYear, storyTheme, characterBackgroundTemplate ))
# exportjson(storyTemplate)
def createStory(storyYear, storyTheme, storyTemplate):
    print("Finalizing story ")
    instructions = f"using this json template, replace all null values with information to support a {storyTheme} themed mystery murder with 5 characters set in the year {storyYear}. Please consider the (_comments) within the template, the Json object should have narative consistancy with all the information created under the (story) key. None of the characters should be investigators or detectives and they should all be suspicious. Ensure the json matches all the requests and has absolutely no remaining null values. Please respond with only the completed json object and no comments, do not respond with any comments. "
    
    chat_completion = openai.chat.completions.create(model="gpt-3.5-turbo", 
                                                   messages=[{"role": "user", 
                                                              "content": f"{instructions} {json.dumps(storyTemplate)}"}]).choices[0].message.content
    
    print(chat_completion)
    
    return json.loads(chat_completion)


def createCompleteStoryJSON():
    storyTemplate = createStoryTemplate()
    exportjson(storyTemplate)

def getMessageSentament(message, responseTemplate):
    print("Evaluating response sentament")
    instructions = f"You will be evaluating the sentament of the user message. The sentament can only be positive or negative. Please respond with only the word positive or negative and no comments. do not respond with any comments."

    try:
        chat_completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": f"{message}"},
            ],
             
        ).choices[0].message.content
        response = chat_completion
        return response

    except Exception as e:
        print(f"Error in createCharacterResponse: {e}")
        return {'error': str(e)}


def createCharacterResponse(message, characterProfile, responseTemplate, story):
    print("Generating character response")
    instructions = f"using plain language, create a 2 sentence response. you are the character here {json.dumps(characterProfile['background'])}. You are being investigated for a murder described by this story {json.dumps(story)}. Please respond with only the characters(who is a little angry) response in first person and no comments. Answer the question even if it is goofy or irrelevant but your response bust be realevant to the story and character. Do not break character; do not respond with any comments."

    try:
        chat_completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": f"{message}"},
            ],
             
        ).choices[0].message.content
        response = responseTemplate
        response['response'] = chat_completion
        response['responseSentament'] = getMessageSentament(chat_completion, responseTemplate)
        return response

    except Exception as e:
        print(f"Error in createCharacterResponse: {e}")
        return {'error': str(e)}

if (__name__ == "__main__" ):
    print("main method")

