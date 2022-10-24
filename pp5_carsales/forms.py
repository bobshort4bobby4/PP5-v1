from allauth.account.forms import LoginForm
class MyCustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):

        # Add your own processing here.
        
        if "trade_flag" in self.request.session:
            self.request.session['trade_flag'] = {}
        if "bag" in self.request.session:
            del self.request.session["bag"]
        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)