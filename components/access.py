import re
from meya import Component

class response_switch(Component):

    def start(self):
        # read in the user's question
        question = self.db.flow.get('answer')
        if re.search("yes", question, re.IGNORECASE):
            action = "access"
        elif re.search("no", question, re.IGNORECASE):
            action = "no_access"
        

        # the action determines which transition is invoked
        # note that no message is returned, just an action
        return self.respond(message=None, action=action)

