import re
from meya import Component

class response_switch(Component):

    def start(self):
        # read in the user's question
        question = self.db.flow.get('own_or_public')
        if re.search("own|self|mine|my", question, re.IGNORECASE):
            action = "own"
        else:
            action = "public"
        

        # the action determines which transition is invoked
        # note that no message is returned, just an action
        return self.respond(message=None, action=action)

