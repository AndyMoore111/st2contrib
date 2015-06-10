import json
import httplib
import urllib

import requests

from st2actions.runners.pythonrunner import Action

__all__ = [
    'SendInviteAction'
]


class SendInviteAction(Action):
    def run(self, email, channels, first_name, token, set_active, attempts):
        config = self.config['send_invite_action']
        token = token if token else config['token']
        set_active = set_active if set_active else config['set_active']
        attempts = attempts if attempts else config['attempts']
        auto_join_channels = config['auto_join_channels']
        url = "https://%s.slack.com/api/users.admin.invite" % \
            config['organization']

        headers = {}
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        body = {
            'email': email,
            'channels': " ".join(auto_join_channels),
            'first_name': first_name,
            'token': token,
            'set_active': set_active,
            '_attempts': attempts
        }

        data = urllib.urlencode(body)
        response = requests.get(url=url,
                                 headers=headers, params=data)
        results = response.json()
        
        if results['ok'] == True:
            return 'Invite successfully sent to %s. RESPONSE: %s' % (email, results)
        else:
            failure_reason = ('Failed to send invite to %s: %s \
                              (status code: %s)' % (email, response.text,
                              response.status_code))
            self.logger.exception(failure_reason)
            raise Exception(failure_reason)

        return True
