import re
from meya import Component

class response_switch(Component):

    def start(self):
        # read in the user's question
        question = self.db.flow.get('user_question')
        if re.search("(place|put|paste|insert|where does|add).+tag", question, re.IGNORECASE):
            action = "tag_placement"
        elif re.search("(where|find|what).+tag", question, re.IGNORECASE):
            action = "tag"
        elif re.search("pcode|p-code", question, re.IGNORECASE):
            action = "p_code"
        elif re.search("hi\Z|hello\Z|hey\Z", question, re.IGNORECASE):
            action = "say_hello"
        elif re.search("thanks|awesome|cool", question, re.IGNORECASE):
            action = "welcome"
        else:
            action = "email"

        # the action determines which transition is invoked
        # note that no message is returned, just an action
        return self.respond(message=None, action=action)

