import google.generativeai as genai

genai.configure(api_key='AIzaSyA0i4L_m40E30Vs0w4P2sX2m670rtRVZh0')

model = genai.GenerativeModel('gemini-pro')

prompt = input("\nPlease enter your prompt (e.g., 'Write a poem about a kitten.'):\n")
response = model.generate_content(prompt)
sentimentresponse = model.generate_content("Generate a detailed sentiment analysis of this text{}".format(response.text))
sentiment = sentimentresponse.text
pdevices = model.generate_content("Tell me about the poetic devices of this poem, try not to repeat the same words again and again, as in, don't ramble {}".format(response.text))
poetdevices = pdevices.text
themes = model.generate_content("Tell me about the themes this poem explores {}".format(response.text))
pthemes=themes.text

print("\n{}\n".format(response.text))
print("\nSentiment Analysis\n\n{}\n".format(sentiment))
print("\nPoetic Devices\n\n{}\n".format(poetdevices))
print("\nThemes Explored\n\n{}\n".format(pthemes))