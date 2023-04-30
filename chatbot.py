import openai
from dotenv import dotenv_values
import argparse # this module allows Python to accept arguments in the command line

config = dotenv_values('.env')
openai.api_key=config["API_KEY"]

def main():
    
    parser = argparse.ArgumentParser(description="Simple command line chatbot with GPT-3.5")

    ## Adding an argument for calling a personality
    parser.add_argument("--personality", type=str, help="A brief summary of the chatbot's personality", default="friendly and helpful")

    ## using parse_args to parse through the arguments
    args = parser.parse_args()
    

    initial_prompt = f"You are a conversational chatbot. Your personality is: {args.personality}"
    messages = [{"role": "system", "content": initial_prompt}]


    while True:
        try:
            user_input = input("You: ")
            messages.append({"role": "user", "content": user_input})
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            messages.append(res["choices"][0]["message"].to_dict())
            print("Assistant:", res["choices"][0]["message"]["content"])


        except KeyboardInterrupt:
            print("Exiting...")
            break

    print(res)

if __name__ == "__main__":
    main()