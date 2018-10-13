from mycroft import MycroftSkill, intent_file_handler


class CitizenshipResources(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('resources.citizenship.intent')
    def handle_resources_citizenship(self, message):
        self.speak_dialog('resources.citizenship')


def create_skill():
    return CitizenshipResources()

