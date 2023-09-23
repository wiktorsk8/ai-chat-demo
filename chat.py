from wrapper import Wrapper

class Chat:
    __messages = []
    __wrapper: Wrapper

    def add_message(self, message, is_user) -> None:
        if is_user != True: print(message)
        self.__messages.append(self.__create_message(message, is_user))
    
    def get_messages(self) -> []:
        return self.__messages
    
    def handle_conversation(self):
        prompt = input("Start conversation: ")
        
        self.__start_chat(prompt)
        
        while(prompt != "stop"):
            prompt = input("Enter your message: ")        
            self.add_message(prompt, True)
            
            response = self.__wrapper.send_prompt(self.get_messages())
            self.add_message(response, False)


        print("Chat has been stopped!")

    def __start_chat(self, prompt):
        self.__wrapper = Wrapper(prompt)
        response = self.__wrapper.boot()

        self.add_message(prompt, True)
        self.add_message(response, False)


    def __create_message(self, content, is_user):
        if is_user:
            role = "user"
        else:
            role = "assistant"

        return {
            "role": role,
            "content": content
        }
