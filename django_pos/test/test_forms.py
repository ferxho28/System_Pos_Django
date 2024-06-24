# myapp/tests/test_forms.py
from django.test import SimpleTestCase
from authentication.forms import LoginForm, SignUpForm

class LoginFormTest(SimpleTestCase):

    def test_login_form_fields(self):
        form = LoginForm()
        self.assertIn('username', form.fields)
        self.assertIn('password', form.fields)
        self.assertEqual(form.fields['username'].widget.attrs['placeholder'], 'Username')
        self.assertEqual(form.fields['username'].widget.attrs['class'], 'form-control form-control-user')
        self.assertEqual(form.fields['password'].widget.attrs['placeholder'], 'Password')
        self.assertEqual(form.fields['password'].widget.attrs['class'], 'form-control form-control-user')


class SignUpFormTest(SimpleTestCase):

    def test_signup_form_fields(self):
        form = SignUpForm()
        self.assertIn('username', form.fields)
        self.assertIn('email', form.fields)
        self.assertIn('password1', form.fields)
        self.assertIn('password2', form.fields)
        self.assertEqual(form.fields['username'].widget.attrs['placeholder'], 'Username')
        self.assertEqual(form.fields['username'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['email'].widget.attrs['placeholder'], 'Email')
        self.assertEqual(form.fields['email'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['password1'].widget.attrs['placeholder'], 'Password')
        self.assertEqual(form.fields['password1'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['password2'].widget.attrs['placeholder'], 'Password confirmation')
        self.assertEqual(form.fields['password2'].widget.attrs['class'], 'form-control')
