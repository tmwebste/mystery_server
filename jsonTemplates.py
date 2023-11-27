characterBackgroundTemplate = {
                    "firstName":"null",
                    "lastName":"null",
                    "age":"null",
                    "occupation":"null",
                    "backstory":"null",
                    "bias":"null",
                    "_connectionComments":"create a list of connections to the other characters, they should not be connected to everyone",
                    "connections":["victim", "null"]
                }

storyTemplate = {
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