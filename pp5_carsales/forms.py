"""
    Custom allauth form to clear session variables at login

"""

from allauth.account.forms import LoginForm


class MyCustomLoginForm(LoginForm):
    """ login form inheriting the allauth login
        clears the session variables """

    def login(self, *args, **kwargs):
        """ over-ride the login method"""
        if "trade_flag" in self.request.session:
            self.request.session['trade_flag'] = {}
        if "trade_details" in self.request.session:
            del self.request.session["trade_details"]
        if "bag" in self.request.session:
            del self.request.session["bag"]

        return super(MyCustomLoginForm, self).login(*args, **kwargs)
