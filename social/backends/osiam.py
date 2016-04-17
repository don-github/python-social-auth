
from social.backends.oauth import BaseOAuth2

class OsiamOAuth2(BaseOAuth2):

    name = 'osiam-oauth2'
    ID_KEY = 'id'
    AUTHORIZATION_URL = 'https://dev-osiam.rapidthunder.io/osiam/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://dev-osiam.rapidthunder.io/osiam/oauth/token'
    ACCESS_TOKEN_METHOD = 'POST'
    USER_DATA_URL = 'https://dev-osiam.rapidthunder.io/osiam/Me'

    def get_user_details(self, response):
        if 'emails' in response:
            email = response['emails'][0]['value']
        else:
            email = response.get('userName', '')
        first_name = response['name']['givenName']
        last_name = response['name']['familyName']
        fullname = ' '.join((first_name, last_name))
        username = fullname
        return {'username': username,
                'email': email,
                'fullname': fullname,
                'first_name': first_name,
                'last_name': last_name}

    def user_data(self, access_token, response=None, *args, **kwargs):
        return self.get_json(self.USER_DATA_URL, headers={'Authorization': 'Bearer {0}'.format(access_token)})
