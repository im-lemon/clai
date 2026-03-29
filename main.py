import requests
from colorama import Style, Fore

url = "https://openrouter.ai/api/v1/chat/completions"



messages = []
token = input("Enter your token: ")

headers = {"Content-Type": "application/json",
           "Authorization": f"Bearer {token}"}
print(Fore.RED + "[NON-IMPORTANT WARNING] Your token is not saved, stored or used by me (lemon), so it is safe, please do not share your token with anyone else. You have control over what you share!" + Style.RESET_ALL)
while True:
    user_msg = input("You: ")
    if user_msg.lower() == "quit":
        break
    else:
        messages.append({"role": "user", "content": user_msg})
        payload = {"model": "arcee-ai/trinity-mini:free",
                   "messages": messages}
        request = requests.post(url, headers=headers, json=payload)
        data = request.json()
        ai_reply = data["choices"][0]["message"]["content"]
        if "choices" in data:
            print(Fore.RED + f"[ERROR] Choices was not found in request, here's some error info: {data}" + Style.RESET_ALL)
        print(f"AI: {ai_reply}")
        messages.append({"role": "assistant", "content": ai_reply})