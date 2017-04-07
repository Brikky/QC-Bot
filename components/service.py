import re
from meya import Component

class response_switch(Component):

    def start(self):
        # read in the user's question
        question = self.db.flow.get('service')
        if re.search("wordpress", question, re.IGNORECASE):
            action = "wordpress"
        elif re.search("blogger", question, re.IGNORECASE):
            action = "blogger"
        elif re.search("google", question, re.IGNORECASE):
            action = "tag_manager"
        elif re.search("manager", question, re.IGNORECASE):
            action = "tag_manager"
        else:
            action = "none"

        # the action determines which transition is invoked
        # note that no message is returned, just an action
        return self.respond(message=None, action=action)

