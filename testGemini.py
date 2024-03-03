import google.generativeai as genai

import PIL.Image
import os

img = PIL.Image.open('image.jpg')
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro-vision')
#response = model.generate_content(img)
#print(response)

prompt = "recommend a three course from this menu"
response = model.generate_content([prompt, img], stream=True)
response.resolve()
print(response)

prompt = response._result.candidates[0].content.parts[0].text
print(prompt)

prompt += ". What is the total prices of those food?"
response = model.generate_content([prompt, img], stream=True)
response.resolve()
print(response._result.candidates[0].content.parts[0].text)