import re


class EmailParser:
    def __init__(self):
        # regex pattern that validate email
#        self.pattern = r'\b[A-Za-z][A-Za-z0-9+]+@[A-Za-z][A-Za-z0-9]+\.com$'
        self.pattern = r'^[A-Za-z][A-Za-z0-9+]+@[A-Za-z][A-Za-z0-9]+\.com$'
        self.keys = ['username', 'domain']


    def convert_to_dict(self, keys, email_list):
        '''
          Takes in two lists as params and return them as a dictionary.'''
        return dict(zip(keys, email_list))

    def parse(self, email):
        ''' parse email and return a dictionary of username and domain if valid and return None otherwise'''
        # Add implementation here ...
        check = re.search(self.pattern, email)
        if check:
            email_as_a_list = email.split("@")
            return self.convert_to_dict(self.keys, email_as_a_list)        
        else:
            return None

