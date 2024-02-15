import google.generativeai as genai
api_key = '<YOUR_API_KEY'
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

def generate_poem(prompt):
  """Generates a poem based on a given prompt using Gemini-Pro model."""
  try:
    response = model.generate_content(prompt)
    return response.text
  except Exception as e:
    print(f"Error generating poem: {e}")
    return None

def analyze_sentiment(text):
  """Analyzes the sentiment of a given text"""
  try:
    prompt = "Generate a detailed sentiment analysis of this text: {}".format(text)
    response = model.generate_content(prompt)
    return response.text
  except Exception as e:
    print(f"Error analyzing sentiment: {e}")
    return None

def identify_poetic_devices(text):
  """Identifies poetic devices used in a given text"""
  try:
    prompt = "Tell me about the poetic devices of this poem, without repetition."
    response = model.generate_content(prompt + text)
    return response.text
  except Exception as e:
    print(f"Error identifying poetic devices: {e}")
    return None

def explore_themes(text):
  """Explores themes explored in a given text"""
  try:
    prompt = "Tell me about the themes this poem explores."
    response = model.generate_content(prompt + text)
    return response.text
  except Exception as e:
    print(f"Error exploring themes: {e}")
    return None

def main():
  """Prompts user for input, generates poem, and performs analysis."""

  prompt = input("\nPlease enter your poem prompt (e.g., 'Write a sonnet about a sunrise'):\n")

  poem = generate_poem(prompt)
  if poem:
    print("\nPoem:\n", poem)
    sentiment = analyze_sentiment(poem)
    if sentiment:
      print("\nSentiment Analysis:\n", sentiment)
    poetic_devices = identify_poetic_devices(poem)
    if poetic_devices:
      print("\nPoetic Devices:\n", poetic_devices)
    themes = explore_themes(poem)
    if themes:
      print("\nThemes Explored:\n", themes)
  else:
    print("An error occurred. Please try again.")

if __name__ == "__main__":
  main()
