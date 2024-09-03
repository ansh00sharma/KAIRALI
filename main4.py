
# from openai import OpenAI
import openai
import base64
import requests
# client = OpenAI()

api_key = ""

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  

base64_image_1 = encode_image('F:\k\Girish Chaturvedi.jpg')
base64_image_2 = encode_image('F:\k\IMG-1724999266127.png')


payload = {
    "model":"gpt-4o",
    "messages":[
        {"role": "system", "content": "You are a computer vision expert, and you have ability to extract texts, find similarity between images and also provide accuracy measures as well."},
        {
        "role": "user",
        "content": [
            {"type": "text", 
            "text": """Instructions : 
            Text Extraction and Verification: "Check if the text 'Shiva ayurvedic store' is present in the first image. Provide the extracted text from the first image, if available, and the accuracy of the text match."
            Image Similarity and Person Verification: "Determine if there is any similarity between the two images. Verify if the person in the second image is present in the first image based on facial expressions, eye color, hair color, and other distinguishable features. Provide the accuracy of the image match"
            Output Format : 
            {
                "text_present": "Yes/No",
                "text_extracted": "some_text",
                "accuracy_of_text_match": "some_value",+
                "explanation": "some_explanation",
                "accuracy_of_image_matched": "some_value",
                "images_matched": "Yes/No",
                "is_valid_image": "Yes/No",
            }
            Notes :
                'is_valid_image' should be 'Yes' only if both text_extracted and images_matched are 'Yes'.
                'images_matched' should be 'Yes' only if accuracy_of_image_matched is higher than 70%.
                'text_extracted' is the text extracted from the first image.
                'accuracy_of_text_match' is the accuracy of the text match.
                'accuracy_of_image_matched' is the similarity percentage between the two persons in the images.
                'explanation' provides the reason for the accuracy_of_image_matched value.
                'images_matched' should be 'Yes' only if the 'accuracy_of_image_matched' is more than 70%
            """
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image_1}",
                "detail": "low"
            },
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image_2}",
                "detail": "low"
            },
            },
        ],
        }
    ]
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
print(response)
print(response.json())
 