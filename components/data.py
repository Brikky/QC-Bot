import re
from meya import Component

class response_switch(Component):

    def start(self):
        # read in the user's question
        question = self.db.flow.get('see_data')
        if re.search("yes", question, re.IGNORECASE):
            action = "yes_data"
        elif re.search("no", question, re.IGNORECASE):
            action = "no_data"
        

        # the action determines which transition is invoked
        # note that no message is returned, just an action
        return self.respond(message=None, action=action)

