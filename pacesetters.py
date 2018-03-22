import sys
import requests


subscription_key = "5c28af14efc04dc9988e119d9f6eafcb"
assert subscription_key
vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
vision_analyze_url = vision_base_url + "analyze"
#image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"
#image_url = ""

path_to_file = sys.argv[1]

# Read file
with open(path_to_file, 'rb') as f:
    data = f.read()
headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
headers['Content-Type'] = 'application/octet-stream'
params   = {'visualFeatures': 'Categories,Description,Color'}
#data     = {'url':"http://./Cool.jpg"}
response = requests.post(vision_analyze_url, headers=headers, params=params, data=data)
#response.raise_for_status()
analysis = response.json()
image_caption = analysis["description"]["captions"][0]["text"].capitalize()
tags = analysis["description"]["tags"]
hasFood = False
for tag in tags:
    if tag == "food":
        #print("We have food in the picture")
        hasFood = True

###predicting happiness

subscription_key = "918242e7f71e4022bef92cc180205b79"
assert subscription_key
face_base_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"
face_analyze_url = face_base_url + "analyze"
#image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"
#image_url = ""

# Read file
with open(path_to_file, 'rb') as f:
    data = f.read()
headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
headers['Content-Type'] = 'application/octet-stream'
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,emotion',
}#data     = {'url':"http://./Cool.jpg"}
response = requests.post(face_base_url, headers=headers, params=params, data=data)
max_emo  = "Neutral"
try:
    response.raise_for_status()
    analysis = response.json()
    #print(analysis["description"][4])
    emotion = analysis[0]["faceAttributes"]["emotion"]
    max = 0


    for i in emotion:
        if max < emotion[i]:
            max = emotion[i]
            max_emo = i

    #print(hasFood)
except Exception as e:
    pass

if max_emo == "happiness" and hasFood == True:
    print("Person is happy with the food")
elif max_emo == "happiness" and hasFood == False:
    print("Person is happy even with out the food")
elif max_emo != "happiness" and hasFood == True:
    print("Person is not happy Looks like  food is not good ")
elif max_emo != "happiness" and hasFood == False:
    print("No food No Life")
elif max_emo == "happiness":
    print("Looks like person is happy not sure about food")
elif max_emo != "happiness":
    print("Looks like person is happy not sure about food")




