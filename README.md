# FHIR_Com_Dashboard

## How to launch backend
1. ```git clone https://github.com/Charlies-Kvit/FHIR_Com_Dashboard```
2. ```python3 -m venv venv```
3. Linux: ```source venv/bin/activate``` <br> Windows cmd: ```.\venv\Scripts\activate.bat``` <br> Windows PowerShell: ```.\venv\Scripts\activate.ps1```
4. ```pip install -r requirements.txt```
5. Check the presence of the "bd/" and "logs/" folders in the "backend/" folder
6. Create a file.env with the following contents in "config" directory:
```doctest
HOST=0.0.0.0 # or 127.0.0.1
PORT=8080 # port number
DEBUG=1 # 1 = True, 0 = False
API_KEY_AI=adsdsafdsfads # API KEY from openai
```
5. For the test, you can simply run app.py

## How to run frontend(vite server)

1. Run- back
2. Check proxy ip address to match api address in `vite.config.js`
3. Run `npm i; npm run dev -- --host`

## API documentation

### Account:
#### GET:
1. ```/api/accounts/<int:account_id>``` - get the data of a single account.<br>
   Example response:
```json
{
    "account": {
        "email":  "a@g.com",
        "group_id":  1,
        "id":  1,
        "name":  "Charlies",
        "avatar_url": "url"
    }
}
```
2. ```/api/accounts``` - get the data of all accounts.<br>
   Example response:
```json
{
    "accounts": [
        {
            "email": "a@g.com",
            "group_id": 1,
            "id": 1,
            "name": "Charlies",
            "avatar_url": "url"
        },
        {
            "email": "Charlies_Hot@g.com",
            "group_id": 2,
            "id": 2,
            "name": "Popgdse",
            "avatar_url": "url"
        }
    ]
}
```
#### PUT:
```/api/accounts/<int:account_id>```
Usage example:
```json
    {
   "name": "Hor", 
   "email": "a@g.com", 
   "group_id": 1,
   "avatar_url": "url"
}
```
Access response:
```json
{
    "account": {
        "email":  "a@g.com",
        "group_id":  1,
        "id":  1,
        "name":  "Hor",
        "avatar_url": "url"
    }
}
```
#### POST:
```/api/accounts```  
Usage example:
```json
{
   "name": "Popgdse", 
   "email": "Charlies_Hot@g.com", 
   "group_id": 1,
   "avatar_url": "url"
}
```
Access response:
```json
{
    "account": {
        "email":  "Charlies_Hot@g.com",
        "group_id": 1,
        "id": 1,
        "name":  "Popgdse",
        "avatar_url": "url"
    }
}
```
#### DELETE:
```/api/accounts/<int:accounts_id>```  
Access response:
```json
{
    "success": "OK"
}
```
<hr>

### Groups
1. ```/api/groups/<int:group_id>``` - get the data of a single group.<br>
   Example response:
```json
{
    "group": {
        "id": 1,
        "name": "Germany"
    }
}
```
2. ```/api/groups``` - get the data of all groups.<br>
   Example response:
```json
{
    "groups": [
        {
            "id": 1,
            "name": "Germany"
        },
        {
            "id": 2,
            "name": "Russia"
        }
    ]
}
```
#### PUT:
```/api/groups/<int:group_id>```  
Usage example:
```json
{
  "name": "Germany"
}
```
Access response:
```json
{
    "group": {
        "id": 1,
        "name": "Germany"
    }
}
```
#### POST:
```/api/groups```  
Usage example:
```json
{
  "name": "Germany"
}

```
Access response:
```json
{
    "group": {
        "id": 1,
        "name": "Germany"
    }
}
```
#### DELETE:
```/api/groups/<int:group_id>```  
Access response:
```json
{
    "success": "OK"
}
```
<hr>

### Group

#### POST:
```/api/parsing``` - to parse posts by mail.
Usage example:
```json
{
   "emails": ["sh@gefyra.de"]
}
```
So far so.  
Example response:
```json
{
    "accounts_ids": [
        1
    ]
}
```
#### GET
```/api/parsing/<int:account_id>``` - get data for drawing a diagram from email.  
```json
{
    "sh@gefyra.de": [
        {
            "timestamp": 12341224, 
            "user_post_count": 25,
            "title": "%patient vs. %subject",
            "id": 1,
            "account_id": 1,
            "url": "https://chat.fhir.org/#narrow/stream/179255-questionnaire/topic/.25patient.20vs..20.25subject",
            "text": "I'd be happy to help you summarize the thread from https://chat.fhir.org/#narrow/stream/179255-questionnaire/topic/.25patient.20vs..20.25subject. Here's a summary of the topic and three pieces of advice with the authors marked:\n\n**Topic Summary:**\nThe thread discusses the differences between \"patient\" and \"subject\" in the context of FHIR (Fast Healthcare Interoperability Resources) questionnaires. The main question is whether \"patient\" and \"subject\" are interchangeable terms or if they have distinct meanings.\n\n**Advice:**\n\n1. **Use \"patient\" for clinical data**: \"When referring to clinical data, it's best to use 'patient' to ensure clarity and consistency. This term is widely accepted in the healthcare industry.\" - **Name: John Doe**\n2. **Consider the context**: \"The choice between 'patient' and 'subject' depends on the context. If you're referring to a research subject, 'subject' might be more appropriate. However, if you're discussing clinical data, 'patient' is generally preferred.\" - **Name: Jane Smith**\n3. **Be precise in your terminology**: \"To avoid confusion, it's crucial to be precise in your terminology. If you're using 'subject,' make sure you're referring to a specific individual or group, and not a general term for a patient.\" - **Name: Michael Brown**\n\nPlease let me know if you need any further assistance or clarification on this topic."
        },
        {
            "timestamp": 12341224,
            "user_post_count": 13,
            "title": "Usage of ElementDefintion.definition vs .comment",
            "id": 2,
            "account_id": 1,
            "url": "https://chat.fhir.org/#narrow/stream/179177-conformance/topic/Usage.20of.20ElementDefintion.definition.20vs.20.comment",
            "text": "I'd be happy to help you with that. Unfortunately, the link provided appears to be experiencing technical difficulties, and I'm unable to access the thread directly. However, I can try to summarize the topic based on the title and provide some general advice.\n\n**Topic Summary:**\nThe topic \"Usage of ElementDefinition.definition vs. comment\" discusses the differences and best practices for using the `definition` and `comment` elements in FHIR (Fast Healthcare Interoperability Resources) ElementDefinitions.\n\n**Summary (300-500 characters):**\nThe thread explores the distinction between `definition` and `comment` in FHIR ElementDefinitions. The `definition` element provides a formal, machine-readable definition of the element, while the `comment` element offers additional context or explanations. Users discuss the importance of using these elements correctly to ensure clear and consistent communication in healthcare data exchange.\n\n**Advice:**\n\n1. **Use `definition` for formal definitions**: Use the `definition` element to provide a formal, machine-readable definition of the element, ensuring clarity and consistency in data exchange (Name: John Doe).\n2. **Use `comment` for additional context**: Utilize the `comment` element to provide additional context or explanations, helping users better understand the element's purpose and usage (Name: Jane Smith).\n3. **Be concise in `definition`**: Keep the `definition` concise and focused on the essential information, avoiding unnecessary details that might confuse users (Name: Michael Brown).\n4. **Use `comment` for examples**: Use the `comment` element to provide examples or illustrations, making it easier for users to understand the element's usage and application (Name: Emily Chen).\n\nPlease note that these pieces of advice are based on general best practices and might not be directly quoted from the original thread due to the technical issues with accessing the link. If you need more specific information or clarification, I recommend trying to access the thread directly or reaching out to the original authors for further guidance."
        },
        {
            "timestamp": 12341224,
            "user_post_count": 8,
            "title": "Observation based Questionnaire prepopulation",
            "id": 3,
            "account_id": 1,
            "url": "https://chat.fhir.org/#narrow/stream/179167-hapi/topic/Observation.20based.20Questionnaire.20prepopulation",
            "text": "I'd be happy to help you with that. Unfortunately, the link you provided seems to be experiencing some technical issues, and I couldn't access the thread directly. However, I can try to summarize the topic based on the title and provide some general advice.\n\n**Topic Summary:**\nThe topic \"Observation-based Questionnaire Prepopulation\" discusses the use of FHIR (Fast Healthcare Interoperability Resources) to prepopulate questionnaires based on patient observations. The thread likely explores the technical aspects of integrating FHIR observations with questionnaire systems to streamline clinical workflows.\n\n**Advice:**\n\n1. **Use FHIR Observations to Enhance Questionnaire Prepopulation**: Name: @FHIR_Guru\n   - Utilize FHIR observations to populate questionnaires with relevant patient data, improving the accuracy and efficiency of clinical workflows.\n\n2. **Consider Integration with Existing Systems**: Name: @HealthIT_Expert\n   - Ensure seamless integration with existing systems and tools to minimize disruptions and maximize the benefits of FHIR-based questionnaire prepopulation.\n\n3. **Focus on Standardization and Interoperability**: Name: @Standards_Guru\n   - Emphasize standardization and interoperability when implementing FHIR-based questionnaire prepopulation to ensure broad adoption and minimal technical hurdles.\n\n4. **Monitor and Adapt to Changing Requirements**: Name: @Clinical_Expert\n   - Continuously monitor changing clinical requirements and adapt the questionnaire prepopulation system accordingly to maintain its effectiveness and relevance.\n\n5. **Leverage FHIR's Query Capability**: Name: @FHIR_Developer\n   - Utilize FHIR's query capability to efficiently retrieve relevant patient data and populate questionnaires with the most up-to-date information.\n\nPlease note that these pieces of advice are based on general knowledge and might not reflect the exact discussions in the thread. If you need more specific information or clarification, I recommend reloading the page or reaching out to the original authors of the thread."
        },
        {
            "timestamp": 12341224,
            "user_post_count": 2,
            "title": "Start des Kommentierungsverfahrens für BfArM-Terminologien",
            "id": 4,
            "account_id": 1,
            "url": "https://chat.fhir.org/#narrow/stream/179183-german-.28d-a-ch.29/topic/Start.20des.20Kommentierungsverfahrens.20für.20BfArM-Terminologien",
            "text": "I'd be happy to help you summarize the thread from https://chat.fhir.org/#narrow/stream/179183-german-.28d-a-ch.29/topic/Start.20des.20Kommentierungsverfahrens.20für.20BfArM-Terminologien. Here's a summary of the topic and some pieces of advice from the discussion:\n\n**Topic Summary - Short (300-500 characters)**\n\nThe thread discusses the implementation of a commenting procedure for BfArM terminologies. Participants share their experiences and challenges in creating and maintaining terminologies for the German healthcare system. They also discuss the importance of standardization and collaboration to ensure consistency and accuracy in terminology usage.\n\n**3-5 Pieces of Advice with Authors**\n\n1. **Use Standardized Terminologies**: \"Use standardized terminologies to ensure consistency and accuracy in terminology usage. This will also facilitate collaboration and reduce errors.\" - **Name: Dr. Müller**\n2. **Create a Centralized Repository**: \"Create a centralized repository for storing and managing terminologies. This will help in maintaining a single source of truth and reduce duplication of effort.\" - **Name: Dr. Schäfer**\n3. **Involve Stakeholders**: \"Involve stakeholders from various departments and organizations to ensure that the commenting procedure is comprehensive and effective. This will also help in gaining buy-in and increasing adoption.\" - **Name: Dr. Weber**\n4. **Use Collaboration Tools**: \"Use collaboration tools like FHIR to facilitate the commenting procedure. This will enable real-time feedback and improve the overall efficiency of the process.\" - **Name: Dr. Kühn**\n5. **Establish Clear Guidelines**: \"Establish clear guidelines and rules for the commenting procedure to ensure that all participants understand the process and can contribute effectively.\" - **Name: Dr. Römer**\n\nPlease let me know if you need any further assistance or clarification on this summary."
        },
        {
            "timestamp": 12341224,
            "user_post_count": 2,
            "title": "[BFARM] ICD und OPS Versionsnummern",
            "id": 5,
            "account_id": 1,
            "url": "https://chat.fhir.org/#narrow/stream/179316-german.2Fterminologien/topic/.5BBFARM.5D.20ICD.20und.20OPS.20Versionsnummern",
            "text": "I'd be happy to help you summarize the thread from https://chat.fhir.org/#narrow/stream/179316-german.2Fterminologien/topic/.5BBFARM.5D.20ICD.20und.20OPS.20Versionsnummern. Here's a summary of the topic and three pieces of advice:\n\n**Topic Summary - Short (300-500 characters):**\nThe thread discusses the use of ICD and OPS versions in FHIR (Fast Healthcare Interoperability Resources) and how to handle versioning in medical terminologies. Participants share their experiences and best practices for managing different versions of ICD and OPS codes in FHIR-based systems.\n\n**Advice 1:**\nUse a centralized terminology server to manage different versions of ICD and OPS codes. This ensures consistency and reduces the complexity of versioning. - **Name: Dr. Müller**\n\n**Advice 2:**\nImplement a versioning strategy that allows for easy updates and backward compatibility. This can be achieved by using a versioning system like SemVer or Git tags. - **Name: Michael B.**\n\n**Advice 3:**\nUse a mapping table to map different versions of ICD and OPS codes to a common reference. This helps in maintaining consistency and reduces the impact of version changes. - **Name: Dr. Schmitz**\n\nPlease let me know if you need any further assistance or clarification on these points."
        }
    ]
}
```
<hr>

### Other

#### GET
```/ping``` - just an Easter egg and a way to find out if the server is alive.<br> 
Example response:
```json
{
   "answer": "pong!"
}
```
