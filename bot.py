from chai_py import ChaiBot, Update
from gpt import ChatAI, FineTunedAPI
from utils import truncate


class Replica(ChaiBot):
    def setup(self):
        self.logger.info("Setting up...")
        self.model = ChatAI(FineTunedAPI(temp=0.5, rep_penalty=1.15))
        self.max_len = 100

    async def on_message(self, update):
        return self.respond(update.latest_message.text)

    def respond(self, message):
        if message == hello how are you sir/ma'am :
            output = "Hi there"
            
        else:
            output = self.model.get_resp(hi)
            if len(output) > self.max_len:
                output = truncate(output, self.max_len)
        return output
