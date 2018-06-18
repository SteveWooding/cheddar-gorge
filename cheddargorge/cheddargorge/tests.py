"""Tests for user management."""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class SignupViewTests(TestCase):
    """Tests for the user signup view."""

    def test_signing_up(self):
        """Test user signup and automatic login."""
        response = self.client.post(
            reverse('signup'),
            data={'username': 'testuser',
                  'password1': '2RfuJh30At',
                  'password2': '2RfuJh30At'},
            follow=True
        )
        self.assertContains(response, 'aria-expanded="false">testuser</a>')

        new_user = get_user_model().objects.first()
        self.assertEqual(new_user.username, 'testuser')


class DeleteAccountViewTests(TestCase):
    """Tests for the account deletion view."""

    def test_deleting_user_account(self):
        """Test deleting a user account."""
        get_user_model().objects.create_user(username='testuser',
                                             password='12345')
        self.client.login(username='testuser', password='12345')

        response = self.client.get(reverse('delete_account'))
        self.assertContains(
            response,
            ('<p>Are you sure you want to delete your account (can not be '
             'reversed)?</p>')
        )

        response = self.client.post(reverse('delete_account'), follow=True)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, 'success')
        self.assertTrue(
            'Your account has been successfully deleted.' in message.message
        )

        no_user = get_user_model().objects.first()
        self.assertEqual(no_user, None)
