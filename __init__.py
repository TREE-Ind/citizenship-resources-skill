from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.audio import wait_while_speaking
from mycroft.skills.context import *

import time


class CitizenshipResources(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    def initialize(self):
        self.eligibility = {'family': 'false', 'employment': 'false', 'special': 'false', 'refugee': 'false', 'victim': 'false',
                            'lottery': 'false', 'cuba': 'false', 'hrifa': 'false', 'lautenberg': 'false', 'vietnam': 'false',
                            'na_ca': 'false', 'diplomat1': 'false', 'diplomat2': 'false', 'nineteenseventytwo': 'false' }
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
        time.sleep(30)
        eligibility_info = self.ask_yesno('eligibility.more.info')
        wait_while_speaking()
        if eligibility_info == 'yes':
            self.speak_dialog('list.eligibility')
            wait_while_speaking()
            family = self.ask_yesno('family')
            wait_while_speaking()
            if family == 'yes':
                self.eligibility['family'] = 'true'
                print(self.eligibility['family'])
            else:
                pass
            employment = self.ask_yesno('employment')
            wait_while_speaking()
            if employment == 'yes':
                self.eligibility['employment'] = 'true'
            else:
                pass
            special = self.ask_yesno('special')
            wait_while_speaking()
            if special == 'yes':
                self.eligibility['special'] = 'true'
            else:
                pass
            refugee = self.ask_yesno('refugee')
            wait_while_speaking()
            if refugee == 'yes':
                self.eligibility['refugee'] = 'true'
            else:
                pass
            victim = self.ask_yesno('victim')
            wait_while_speaking()
            if victim == 'yes':
                self.eligibility['victim'] = 'true'
            else:
                pass
            lottery = self.ask_yesno('lottery')
            wait_while_speaking()
            if lottery == 'yes':
                self.eligibility['lottery'] = 'true'
            else:
                pass
            cuba = self.ask_yesno('cuba')
            wait_while_speaking()
            if cuba == 'yes':
                self.eligibility['cuba'] = 'true'
            else:
                pass
            hrifa = self.ask_yesno('hrifa')
            wait_while_speaking()
            if hrifa == 'yes':
                self.eligibility['hrifa'] = 'true'
            else:
                pass
            lautenberg = self.ask_yesno('lautenberg')
            wait_while_speaking()
            if lautenberg == 'yes':
                self.eligibility['lautenberg'] = 'true'
            else:
                pass
            vietnam = self.ask_yesno('vietnam')
            wait_while_speaking()
            if vietnam == 'yes':
                self.eligibility['vietnam'] = 'true'
            else:
                pass
            na_ca = self.ask_yesno('na_ca')
            wait_while_speaking()
            if na_ca == 'yes':
                self.eligibility['na_ca'] = 'true'
            else:
                pass
            diplomat1 = self.ask_yesno('diplomat1')
            wait_while_speaking()
            if diplomat1 == 'yes':
                self.diplomat1 = True
                self.eligibility['diplomat1'] = 'true'
            else:
                pass
            diplomat2 = self.ask_yesno('diplomat2')
            wait_while_speaking()
            if diplomat2 == 'yes':
                self.eligibility['diplomat2'] = 'true'
            else:
                pass
            nineteenseventytwo = self.ask_yesno('nineteenseventytwo')
            wait_while_speaking()
            if nineteenseventytwo == 'yes':
                self.eligibility['nineteenseventytwo'] = 'true'
            else:
                pass
            
            if "true" in self.eligibility.values():
                confirm = self.ask_yesno('eligible')
                wait_while_speaking()
                if confirm == 'yes':
                    self.speak_dialog('confirmed')
                    wait_while_speaking()
                else:
                    confirm = self.ask_yesno('start.over')
                    wait_while_speaking()
                    if confirm == 'yes':
                        #restart questionnaire
                        pass
                    else:
                        self.speak_dialog('call')
                        wait_while_speaking()
            else:
                self.speak_dialog('not.eligible')
                wait_while_speaking()
                
            
        else:
            self.speak_dialog('here.to.assist')
            wait_while_speaking()


def create_skill():
    return CitizenshipResources()

