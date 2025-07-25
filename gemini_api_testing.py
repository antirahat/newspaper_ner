from google import genai
from dotenv import load_dotenv
import os 

load_dotenv(dotenv_path=".env.local")

client = genai.Client()

# ...existing code...
response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""Your task is to perform Named Entity Recognition (NER) using the IOB2 tagging schema from CoNLL 2003 in this article:
{"article_3.txt"}
The entity types are:
ACCIDENT_DATE: Date of the accident (e.g., "Saturday morning", "2 May") 
ACCIDENT_TIME: Time of the accident (e.g., "10:30am Bangladesh time") 
ACCIDENT_TYPE: Description of the accident type (e.g., "crane accident", "fatal accident")
ACCIDENT_LOCATION: General location description of the accident (e.g., "Malaysia's Seremban city", "Kuril Bishwa Road area") 
ADDRESS: Specific street address or named location within a broader area (e.g., "Baguri Beltala village") 
DISTRICT: The district where the accident occurred (e.g., "Jashore district", "Dhaka") 
UPAZILLA: The upazilla (sub-district) where the accident occurred (e.g., "Sharsha upazila") 
LANDMARK_POI: Any significant landmark or point of interest near the accident (e.g., "construction site") 
ROAD_TYPE: Type of road involved (e.g., "railway tracks") 
ROAD_CONDITION: Condition of the road surface (e.g., "unprotected rail-crossing") 
ROAD_LAYOUT: Specific layout features of the road (e.g., "bend in the railway line") 
ROAD_MARKING: Descriptions of road markings 
ROAD_SIGNAGE: Descriptions of road signs 
WEATHER_CONDITION: Weather at the time of the accident (e.g., "summer") 
VISIBILITY_LEVEL: Visibility conditions 
LIGHTING_CONDITION: Lighting conditions (e.g., "night") 
SURFACE_CONDITION: Condition of the road surface (e.g., wet, dry, icy) 
TRAFFIC_DENSITY: Level of traffic density 
EMERGENCY_RESPONSE_LEVEL: Level or type of emergency response 
ROAD_SURFACE: The material or type of surface of the road (e.g., "pitched", "dirt") 
ROADSIDE_HAZARD_TYPE: Type of roadside hazard involved (e.g., "tree", "pole") 
PERSON_TYPE: Role or type of person involved (e.g., "Bangladeshi youth", "co-workers", "Chairman", "Officer") 
SEVERITY_LEVEL: Severity of injury or outcome (e.g., "dying on the spot", "tragic death") 
AGE: Age of the person (e.g., "35", "60") 
NAME: Full name of an individual (e.g., "Roni", "Mahmud Sardar", "Altaf Hossain") 
GENDER: Gender of the person 
SAFETY_EQUIPMENT_USED: Type of safety equipment used by a person 
DRIVING_EXPERIENCE: Experience level of a driver 
DRIVER_FATIGUE_LEVEL: Level of driver fatigue 
LAW_VIOLATION: Specific law or rule violation (e.g., "carelessness", "unlawful entry onto the railway tracks") 
INJURY_TYPE: Type of injury sustained (e.g., "beheaded body") 
CONTACT_DETAILS: Phone numbers, emails, etc. (if explicitly mentioned) 
IDENTIFICATION_NUMBER: ID numbers (e.g., NID, passport, if mentioned) 
VEHICLE_TYPE: Type of vehicle involved (e.g., "crane", "heavy equipment") 
VEHICLE_CONDITION: Condition of the vehicle 
VEHICLE_LOAD: Load status of the vehicle 
RUNNING_STATUS: Operational status of the vehicle 
REGISTRATION_NUMBER: Vehicle registration plate number 
VEHICLE_REGISTRATION_YEAR: Year of vehicle registration 
SOURCE_NAME: Name of the source (e.g., "family", "expatriate welfare ministry", "local administration") 
ARTICLE_URL: URL of the source article 
DOCUMENT_NAME: Name of any attached documents 
ADMIN_UNIT_TYPE_EN: Administrative unit type in English (e.g., "Union", "Upazila", "District") 
ADMIN_UNIT_TYPE_BN: Administrative unit type in Bengali 
ADMIN_UNIT_NAME_EN: Administrative unit name in English (e.g., "Kayba union", "Jashore") 
ADMIN_UNIT_NAME_BN: Administrative unit name in Bengali 
Tag each token as B-
JSON
{{
"id": "document_id_here",
"text": "The full article text goes here...",
"entities": [
    {{
    "text": "Entity text 1",
    "tag": "B-TAG_TYPE",
    "position": {{
        "start": 0,
        "end": 13
    }}
    }},
    {{
    "text": "Entity text 2",
    "tag": "I-TAG_TYPE",
    "position": {{
        "start": 14,
        "end": 27
    }}
    }}
]
}}
Example of CoNLL-2003 formatted token-tag pairs (which you will convert to the final JSON structure):
The O
deceased O
was O
identified O
as O
Roni B-NAME
, O
35 B-AGE
, O
son O
of O
Mahmud B-NAME
Sardar I-NAME
from O
Baguri B-ADDRESS
Beltala I-ADDRESS
village I-ADDRESS
i O
Kayba B-ADMIN_UNIT_NAME_EN
union I-ADMIN_UNIT_NAME_EN
under O
Sharsha B-UPAZILLA
upazila I-UPAZILLA
of O
Jashore B-DISTRICT
district I-DISTRICT

"""
    )
# ...existing code...
print(response.text)