# pip install azure-cognitiveservices-vision-customvision
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

# Now there is a trained endpoint that can be used to make a prediction
ENDPOINT = "INSERT_ENDPOINT"
projectid="INSERT_PROJECT_ID"
publishiterationname="INSERT_MODELNAME"
prediction_key = "INSERT_PREDICTION_KEY"


predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

with open("D:/Work/Pythonmeetup/Python-AI/gear_images/axes/21HnHt+LMDL._AC_US436_QL65_.jpg", "rb") as image_contents:
    results = predictor.classify_image(
        projectid, publishiterationname, image_contents.read())

    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))
