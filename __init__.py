from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.audio import wait_while_speaking
from mycroft.skills.context import *
from mycroft.messagebus.client.ws import WebsocketClient
from mycroft.messagebus.message import Message

import time
import smtplib

import socket


class CitizenshipResources(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
        socket.setdefaulttimeout(20)
        
        self.sender = "info@tree.industries"
        self.recipient = "info@tree.industries"
        self.password = "globalhack7" # Your SMTP password for Gmail
        
    def initialize(self):
        self.eligibility = {'family': 'false', 'employment': 'false', 'special': 'false', 'refugee': 'false', 'victim': 'false',
                            'lottery': 'false', 'cuba': 'false', 'hrifa': 'false', 'lautenberg': 'false', 'vietnam': 'false',
                            'na_ca': 'false', 'diplomat1': 'false', 'diplomat2': 'false', 'nineteenseventytwo': 'false' }
        self.eligibility_items = []

    @intent_file_handler('green.card.intent')
    def handle_resources_citizenship(self, message):
        self.speak_dialog('green.card.eligibility')
        wait_while_speaking()
        #time.sleep(15)
        eligibility_info = self.ask_yesno('eligibility.more.info')
        wait_while_speaking()
        if eligibility_info == 'yes':
            self.speak_dialog('list.eligibility')
            wait_while_speaking()
            family = self.ask_yesno('family')
            wait_while_speaking()
            if family == 'yes':
                self.eligibility['family'] = 'true'
                self.eligibility_items.append("family")
            else:
                pass
            employment = self.ask_yesno('employment')
            wait_while_speaking()
            if employment == 'yes':
                self.eligibility['employment'] = 'true'
                self.eligibility_items.append("employment")
            else:
                pass
            special = self.ask_yesno('special')
            wait_while_speaking()
            if special == 'yes':
                self.eligibility['special'] = 'true'
                self.eligibility_items.append("special immigrant")
            else:  
                pass
            refugee = self.ask_yesno('refugee')
            wait_while_speaking()
            if refugee == 'yes':
                self.eligibility['refugee'] = 'true'
                self.eligibility_items.append("refugee or asylee")
            else:
                pass
            victim = self.ask_yesno('victim')
            wait_while_speaking()
            if victim == 'yes':
                self.eligibility['victim'] = 'true'
                self.eligibility_items.append("victim of abuse")
            else:
                pass
            lottery = self.ask_yesno('lottery')
            wait_while_speaking()
            if lottery == 'yes':
                self.eligibility['lottery'] = 'true'
                self.eligibility_items.append("Diversity Immigration Visa Program")
            else:
                pass
            cuba = self.ask_yesno('cuba')
            wait_while_speaking()
            if cuba == 'yes':
                self.eligibility['cuba'] = 'true'
                self.eligibility_items.append("Cuban Adjustment Act")
            else:
                pass
            hrifa = self.ask_yesno('hrifa')
            wait_while_speaking()
            if hrifa == 'yes':
                self.eligibility['hrifa'] = 'true'
                self.eligibility_items.append("H R I F A")
            else:
                pass
            lautenberg = self.ask_yesno('lautenberg')
            wait_while_speaking()
            if lautenberg == 'yes':
                self.eligibility['lautenberg'] = 'true'
                self.eligibility_items.append("Lautenberg Parolee")
            else:
                pass
            vietnam = self.ask_yesno('vietnam')
            wait_while_speaking()
            if vietnam == 'yes':
                self.eligibility['vietnam'] = 'true'
                self.eligibility_items.append("Orderly Departure Program")
            else:
                pass
            na_ca = self.ask_yesno('na_ca')
            wait_while_speaking()
            if na_ca == 'yes':
                self.eligibility['na_ca'] = 'true'
                self.eligibility_items.append("Native American born in Canada")
            else:
                pass
            diplomat1 = self.ask_yesno('diplomat1')
            wait_while_speaking()
            if diplomat1 == 'yes':
                self.eligibility['diplomat1'] = 'true'
                self.eligibility_items.append("Child of foreign diplomat")
            else:
                pass
            diplomat2 = self.ask_yesno('diplomat2')
            wait_while_speaking()
            if diplomat2 == 'yes':
                self.eligibility['diplomat2'] = 'true'
                self.eligibility_items.append("Stationed as foreign diplomat")
            else:
                pass
            nineteenseventytwo = self.ask_yesno('nineteenseventytwo')
            wait_while_speaking()
            if nineteenseventytwo == 'yes':
                self.eligibility['nineteenseventytwo'] = 'true'
                self.eligibility_items.append("Lived in the United States before 1972")
            else:
                pass
            
            if "true" in self.eligibility.values():
                confirm = self.ask_yesno('eligible', data=dict(eligibility_items=self.eligibility_items))
                wait_while_speaking()
                if confirm == 'yes':
                    self.speak_dialog('confirmed')
                    wait_while_speaking()
                    email_title = "Green Card Eligibility Application"
                    email_body = "Joshua Johnson has confirmed eligibility for a green card through the following, {}.".format(self.eligibility_items)
                    email_message = "Subject: {}\n\n{}".format(email_title, email_body)
                    smtp_server = smtplib.SMTP_SSL('mail.tree.industries', 465)
                    smtp_server.login(self.sender, self.password)
                    smtp_server.sendmail(self.sender, self.recipient, email_message)
                    smtp_server.close()
                else:
                    start_over = self.ask_yesno('start.over')
                    wait_while_speaking()
                    if start_over== 'yes':
                        self.emitter.emit(Message('recognizer_loop:utterance', {"utterances": ["How do I apply for a green card"]}))
                        pass
                    else:
                        call = self.ask_yesno('call')
                        wait_while_speaking()
                        if call == 'yes':
                            self.speak_dialog('yes.call')
                        else:
                            self.speak_dialog('here.to.assist')
            else:
                self.speak_dialog('not.eligible')
                wait_while_speaking()
                
        else:
            self.speak_dialog('here.to.assist')
            wait_while_speaking()

    @intent_file_handler('set.appointment.intent')
    def handle_set_appointment(self, message):
        self.speak_dialog('appointment.greeting')
        wait_while_speaking()
        name = self.get_response('gather.name')
        wait_while_speaking()
        number = self.get_response('gather.number')
        wait_while_speaking()
        time = self.get_response('gather.time')
        wait_while_speaking()
        confirm = self.ask_yesno('confirm.appointment.info', data=dict(name=name,number=number,time=time))
        wait_while_speaking()
        if confirm == 'yes':
            self.speak_dialog('appointment.confirmed')
            email_title = "Immigration Services Appointment Request"
            email_body = "{} has requested an appointment with a case worker, their phone number is {}, and their preferred call back time is {}.".format(name, number, time)
            email_message = "Subject: {}\n\n{}".format(email_title, email_body)
            smtp_server = smtplib.SMTP_SSL('mail.tree.industries', 465)
            smtp_server.login(self.sender, self.password)
            smtp_server.sendmail(self.sender, self.recipient, email_message)
            smtp_server.close()
        else:
            start_over = self.ask_yesno('start.appointment.over')
            wait_while_speaking()
            if start_over== 'yes':
                self.emitter.emit(Message('recognizer_loop:utterance', {"utterances": ["I need to schedule an appointment"]}))
            else:
                pass
            
    


def create_skill():
    return CitizenshipResources()

