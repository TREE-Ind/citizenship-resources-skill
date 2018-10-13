from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.audio import wait_while_speaking
from mycroft.skills.context import *


class CitizenshipResources(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    def initialize(self):
        self.family = False
        self.employment = False
        self.special = False
        self.refugee = False
        self.victim = False
        self.lottery = False
        self.cuba = False
        self.hrifa = False
        self.lautenberg = False
        self.vietnam = False
        self.na_ca = False
        self.diplomat1 = False
        self.diplomat2 = False
        self.nineteenseventytwo = False

    @intent_file_handler('green.card.intent')
    def handle_resources_citizenship(self, message):
        self.speak_dialog('green.card.eligibility')
        wait_while_speaking()
        eligibility_info = self.ask_yesno('eligibility.more.info')
        wait_while_speaking()
        if eligibility_info == 'yes':
            self.speak_dialog('list.eligibility')
            wait_while_speaking()
            family = self.ask_yesno('family')
            if family == 'yes':
                self.family = True
            else:
                pass
            employment = self.ask_yesno('employment')
            if employment == 'yes':
                self.employment = True
            else:
                pass
            special = self.ask_yesno('special')
            if special == 'yes':
                self.special = True
            else:
                pass
            refugee = self.ask_yesno('refugee')
            if refugee == 'yes':
                self.refugee = True
            else:
                pass
            victim = self.ask_yesno('victim')
            if victim == 'yes':
                self.victim = True
            else:
                pass
            lottery = self.ask_yesno('lottery')
            if lottery == 'yes':
                self.lottery = True
            else:
                pass
            cuba = self.ask_yesno('cuba')
            if cuba == 'yes':
                self.cuba = True
            else:
                pass
            hrifa = self.ask_yesno('hrifa')
            if hrifa == 'yes':
                self.hrifa = True
            else:
                pass
            lautenberg = self.ask_yesno('lautenberg')
            if lautenberg == 'yes':
                self.lautenberg = True
            else:
                pass
            vietnam = self.ask_yesno('vietnam')
            if vietnam == 'yes':
                self.vietnam = True
            else:
                pass
            na_ca = self.ask_yesno('na_ca')
            if na_ca == 'yes':
                self.na_ca = True
            else:
                pass
            diplomat1 = self.ask_yesno('diplomat1')
            if diplomat1 == 'yes':
                self.diplomat1 = True
            else:
                pass
            diplomat2 = self.ask_yesno('diplomat2')
            if diplomat2 == 'yes':
                self.diplomat2 = True
            else:
                pass
            nineteenseventytwo = self.ask_yesno('nineteenseventytwo')
            if nineteenseventytwo == 'yes':
                self.nineteenseventytwo = True
            else:
                pass
            
        else:
            self.speak_dialog('here.to.assist')
            wait_while_speaking()


def create_skill():
    return CitizenshipResources()

