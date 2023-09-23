import openai

class Wrapper:

    __SYSTEM_CONTENT = ""
    __TEMPERATURE = 1


    def __init__(self, first_message: str) -> None:
        self.first_message = first_message
    
    def boot(self):
        completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": self.__SYSTEM_CONTENT 
            },
            
            {
                "role": "user",
                "content": self.first_message
            }
        ])

        return completion['choices'][0]['message']['content']
    
    def send_prompt(self, messages):
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages,
            temperature=self.__TEMPERATURE
        )

        return completion['choices'][-1]['message']['content']



        
