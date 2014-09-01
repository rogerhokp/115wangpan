# -*- coding: utf-8 -*-
import requests
import time
from hashlib import sha1


class RequestHandler(object):
    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None):
        return self.session.get(url, params=params)

    def post(self, url, data, params=None):
        return self.session.post(url, data=data, params=params)

    def __repr__(self):
        return self.session


class API(object):
    api_url = ''

    def __init__(self):
        self.passport = None
        self.http = RequestHandler()

    def login(self, username, password):
        passport = Passport(username, password)
        r = self.http.post(passport.logout_url, passport.form)
        if r.ok:
            print 'Login Sucess.'
        else:
            print r.json()['message']

    @property
    def has_logged_in(self):
        if self.passport is not None:
            return True
        return False

    def logout(self):
        self.http.get()


class Passport(object):
    login_url = 'http://passport.115.com/?ct=login&ac=ajax&is_ssl=1'
    logout_url = 'http://passport.115.com/?ac=logout'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.form = self._form()

    def _form(self):
        vcode = self._vcode()
        f = {
            'login[ssoent]': 'A1',
            'login[version]': '2.0',
            'login[ssoext]': vcode,
            'login[ssoln]': self.username,
            'login[ssopw]': self._ssopw(vcode),
            'login[ssovcode]': vcode,
            'login[safe]': '1',
            'login[time]': '0',
            'login[safe_login]': '0',
            'goto': 'http://115.com/',
        }
        return f

    def _vcode(self):
        s = '%.6f' % time.time()
        whole, frac = map(int, s.split('.'))
        res = '%x%x' % (whole, frac)
        assert len(res) == 13
        return res

    def _ssopw(self, vcode):
        p = sha1(self.password).hexdigest()
        u = sha1(self.username).hexdigest()
        return sha1(sha1(p + u).hexdigest() + vcode).hexdigest()