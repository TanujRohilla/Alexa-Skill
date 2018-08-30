def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()

def onIntent(intentRequest, session):
             
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']
    if intentName == "whatisblockchain":
        return blockchain_fact(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello"
    speechOutput =  "Hello , Welcome to Blockchain Guru! " \
                    "You can know interesting facts about Blockchain by saying Tell me facts about blockchain "
    repromptText =  "You can know interesting facts about Blockchain by saying Tell me facts about blockchain"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def blockchain_fact(intent, session):
    import random
    index = random.randint(0,len(blockchain)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    #speechOutput = "Blockchain Guru is actually a blockchain fact is that " + blockchain[index]
    speechOutput = blockchain[index]
    repromptText = "You can know interesting facts about blockchain by saying Tell me about blockchain"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using Blockchain Guru Alexa Skills Kit. " \
                    "Have a great time! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }


def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }



blockchain = [ "A blockchain is considered as a real-time ledger or decentralized database that is implemented to maintain a gradually increasing list of records, called blocks. Each one of the blocks contains a     timestamp and a link to a previous block. Basically, it is a database, a huge network, called as a distributed ledger, which keeps track of ownership and value, and allows anyone with access to view and take part",
               "The person or team behind the service is known by the pseudonym Satoshi Nakamoto, but the entity’s real identity is cloaked in secrecy",
               "Blockchains can be public (like the internet) or private (like an intranet)",
               "Only 0.5% of the world’s population is using blockchain today, but 50% or 3.77 billion people use the internet",
               "The global blockchain market is expected to be worth $20 billion by 2024",
               "90% of major North American and European banks are exploring blockchain solutions",
               "Blockchains are highly transparent, because anyone with access to a blockchain can view the entire chain"
               "Similar to a Google doc, all participants within a network see all changes to the ledger. The ledger is constantly updated and each participant has their own copy of it",
               "It is estimated that bank could save $8-12 billion annually if they use block chain technology",
               "After japan , switserland is the next to begin accepting Bitcoin payments to cover yuor taxes 64% Bitcoins were never user and might never be used",
               "FBI owns 1.5% of world's total Bitcoins",
               "There is significant investment by today’s tech giants such as IBM and Microsoft in blockchain technology. IBM dedicates $200 million and 1,000 employees to blockchain-powered projects. The average investment in blockchain projects is $1 million.",
               "Over the last five years, VCs have invested more than $1 billion into blockchain companies.",
               "A blockchain is most vulnerable to a breach when it first come online.",
               "9 out of 10 agree that blockchain will disrupt the banking and financial industry. It is estimated that banks could save $8-12 billion annually if they used blockchain technology.",
               "50% of banks are working with technology company to augment their transaction process via blockchain"
]
