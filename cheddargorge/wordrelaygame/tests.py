"""Unit tests for the wordrelaygame app."""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Story

# pylint: disable=locally-disabled, C0103

class HomeViewTests(TestCase):
    """Tests for HomeView."""

    def test_login_link_when_no_user_is_logged_in(self):
        """
        Test to ensure the login link is displayed when no user is logged in.
        """
        response = self.client.get(reverse('wordrelaygame:home'))
        self.assertContains(response, '<a href="/login/">Login </a>')

class AddWordViewTests(TestCase):
    """Tests for the AddWordView."""

    def test_adding_new_word(self):
        """
        Test that a new word appears on the homepage.
        """
        get_user_model().objects.create_user(username='testuser',
                                             password='12345')
        self.client.login(username='testuser', password='12345')
        self.client.post(reverse('wordrelaygame:new_story'), follow=True)

        response = self.client.post(reverse('wordrelaygame:addword'),
                                    {'content': 'Extraordinarily'},
                                    follow=True)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, 'success')
        self.assertTrue('Your word as been added.' in message.message)

        self.assertContains(response, 'Extraordinarily')

    def test_user_cannot_add_two_words_consecutively(self):
        """
        Ensure that consecutive words cannot be created by the same user.
        """
        get_user_model().objects.create_user(username='testuser',
                                             password='12345')
        self.client.login(username='testuser', password='12345')
        self.client.post(reverse('wordrelaygame:new_story'), follow=True)

        self.client.post(reverse('wordrelaygame:addword'), {'content': 'Once'},
                         follow=True)

        response = self.client.post(reverse('wordrelaygame:addword'),
                                    {'content': 'upon'}, follow=True)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue("You added the last word." in message.message)

        new_story = Story.objects.first()
        self.assertEqual(new_story.words.count(), 1)

    def test_adding_word_when_no_story_exists(self):
        """
        Test adding a word when there is no story exists.
        """
        get_user_model().objects.create_user(username='testuser',
                                             password='12345')
        self.client.login(username='testuser', password='12345')

        response = self.client.post(reverse('wordrelaygame:addword'),
                                    {'content': 'Once'}, follow=True)

        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, 'error')
        self.assertTrue(
            'You need to create a story to add a word.' in message.message
        )

    def test_adding_an_invalid_word(self):
        """
        Test adding an invalid word (e.g. two words at once).
        """
        get_user_model().objects.create_user(username='testuser',
                                             password='12345')
        self.client.login(username='testuser', password='12345')
        self.client.post(reverse('wordrelaygame:new_story'), follow=True)

        response = self.client.post(reverse('wordrelaygame:addword'),
                                    {'content': 'Once upon'}, follow=True)
        self.assertEqual(response.status_code, 200)
        form = str(response.context.get('form'))
        self.assertTrue('Enter a valid value.' in form)

    def test_adding_a_banned_word(self):
        """Test adding a word on the banned list."""
        get_user_model().objects.create_user(username='testuser',
                                             password='12345')
        self.client.login(username='testuser', password='12345')
        self.client.post(reverse('wordrelaygame:new_story'), follow=True)

        response = self.client.post(reverse('wordrelaygame:addword'),
                                    {'content': 'testbannedword'}, follow=True)
        self.assertEqual(response.status_code, 200)
        form = str(response.context.get('form'))
        self.assertTrue('Sorry. That word is or contains a banned' in form)


class AddStoryViewTests(TestCase):
    """Tests for the AddStoryView."""

    def test_adding_first_story(self):
        """
        Test that a user can add the first story.
        """
        get_user_model().objects.create_user(username='testuser',
                                             password='12345')
        self.client.login(username='testuser', password='12345')

        response = self.client.post(reverse('wordrelaygame:new_story'),
                                    follow=True)
        new_story = Story.objects.first()
        self.assertNotEqual(new_story, None)
        self.assertEqual(response.status_code, 200)

    def test_adding_second_story(self):
        """
        Make sure a second story can only be added after the first story has 64
        words.
        """
        get_user_model().objects.create_user(username='testuser',
                                             password='12345')
        get_user_model().objects.create_user(username='testuser2',
                                             password='12345')
        self.client.login(username='testuser', password='12345')
        self.client.post(reverse('wordrelaygame:new_story'), follow=True)

        # Try adding another new story straightaway
        response = self.client.post(reverse('wordrelaygame:new_story'),
                                    follow=True)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, 'error')
        self.assertTrue('Failed to create new story.' in message.message)
        self.client.logout()

        # Make the current story long enough
        for i in range(65):
            if i % 2:
                self.client.login(username='testuser', password='12345')
            else:
                self.client.login(username='testuser2', password='12345')
            self.client.post(reverse('wordrelaygame:addword'),
                             {'content': 'test'}, follow=True)
            self.client.logout()

        # Should now be able to add another story
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('wordrelaygame:new_story'),
                                    follow=True)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, 'success')
        self.assertTrue('A new story has been created.' in message.message)
        self.assertTrue(Story.objects.count(), 2)


class StoryListViewTests(TestCase):
    """Tests for StoryListView."""

    def test_story_list_view(self):
        """Test rendered of story list view."""
        get_user_model().objects.create_user(username='testuser',
                                             password='12345')
        get_user_model().objects.create_user(username='testuser2',
                                             password='12345')
        self.client.login(username='testuser', password='12345')
        self.client.post(reverse('wordrelaygame:new_story'), follow=True)

        for i in range(65):
            if i % 2:
                self.client.login(username='testuser', password='12345')
            else:
                self.client.login(username='testuser2', password='12345')
            self.client.post(reverse('wordrelaygame:addword'),
                             {'content': 'cricket'}, follow=True)
            self.client.logout()

        self.client.post(reverse('wordrelaygame:new_story'), follow=True)
        self.client.login(username='testuser', password='12345')
        self.client.post(reverse('wordrelaygame:addword'),
                         {'content': 'tennis'}, follow=True)

        response = self.client.get(reverse('wordrelaygame:story-list'))
        self.assertContains(response, 'cricket', count=65)
        self.assertContains(response, 'tennis')


class WordModelTests(TestCase):
    """Tests for the Word model."""

    def test_deleting_user(self):
        """
        Make sure a word is set to the 'deleted' user when a user is deleted.
        """
        test_user = get_user_model().objects.create_user(username='testuser',
                                                         password='12345')
        self.client.login(username='testuser', password='12345')
        self.client.post(reverse('wordrelaygame:new_story'), follow=True)

        self.client.post(reverse('wordrelaygame:addword'),
                         {'content': 'Once'}, follow=True)

        self.client.logout()
        test_user.delete()

        test_story = Story.objects.first()
        self.assertEqual(test_story.words.first().author.username, 'deleted')


class StoryModelTests(TestCase):
    """Tests for the Story model."""

    def test_string_representation(self):
        """Test the sting representation of the Story model."""
        get_user_model().objects.create_user(username='testuser',
                                             password='12345')
        self.client.login(username='testuser', password='12345')
        self.client.post(reverse('wordrelaygame:new_story'), follow=True)

        test_story = Story.objects.first()
        self.assertEqual(str(test_story), 'Story #' + str(test_story.id))
