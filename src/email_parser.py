import re


class EmailParser:
    def __init__(self):
        # regex pattern that validate email
        self.pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.keys = ['username', 'domain']


    def convert_to_dict(self, keys, email_list):
        '''
          Takes in two lists as params and return them as a dictionary.'''
        result = dict(zip(keys, email_list))
        print(result)


    def parse(self, email):
        ''' parse email and return a dictionary of username and domain if valid and return None otherwise'''
        # Add implementation here ...
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        check = re.match(self.pattern, email)
        if check:
            email_as_a_list = email.split("@")
            if email_as_a_list[0][0] in numbers or email_as_a_list[1][0] in numbers:
                print(None)
            else:
                self.convert_to_dict(self.keys, email_as_a_list)        
        else:
            print(None)


    
email = EmailParser()
mail = ' timothy-abiodun@gmail.com'
#mail = input('Enter your email address: ')
#remove trailing and leading whitespaces
#stripped_mail = mail.strip()
email.parse(mail)
