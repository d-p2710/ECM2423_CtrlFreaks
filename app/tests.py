from django.test import TestCase, RequestFactory
from unittest.mock import patch, MagicMock
from app.views import crossword_game, question_amount, get_crossword_questions

class CrosswordGameViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch('yourapp.views.get_crossword_questions')
    @patch('yourapp.views.question_amount')
    def test_crossword_game(self, mock_question_amount, mock_get_crossword_questions):
        # Mock the return values for the functions
        mock_question_amount.return_value = (1, 1, 1)
        mock_get_crossword_questions.return_value = ([], [], [])

        # Create a request object
        request = self.factory.get('/crossword_game/')
        request.COOKIES['level'] = 1  # Set the level in cookies

        # Call the view function
        response = crossword_game(request)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/crosswordGame.html')

        # Additional assertions to test the context passed to the template
        self.assertIn('easy_questions', response.context)
        self.assertIn('medium_questions', response.context)
        self.assertIn('hard_questions', response.context)
        self.assertIn('easy_answers', response.context)
        self.assertIn('medium_answers', response.context)
        self.assertIn('hard_answers', response.context)

        # Check if the mocked functions were called
        mock_question_amount.assert_called_once_with(1)
        mock_get_crossword_questions.assert_called_once_with(1, 1, 1)
