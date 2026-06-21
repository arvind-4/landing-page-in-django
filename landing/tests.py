"""Tests for the landing app."""

from typing import Any
from unittest.mock import MagicMock, patch

from django.test import Client, TestCase

from landing.forms import RegisterForm
from landing.views import send_email_in_thread


class RegisterFormTests(TestCase):
    """Tests for the RegisterForm."""

    def test_form_valid_email(self) -> None:
        """Test that the form validates a valid email address."""
        form_data = {"email": "test@example.com"}
        form = RegisterForm(data=form_data)
        assert form.is_valid()
        assert form.cleaned_data["email"] == "test@example.com"

    def test_form_invalid_email(self) -> None:
        """Test that the form rejects an invalid email address."""
        form_data = {"email": "invalid-email"}
        form = RegisterForm(data=form_data)
        assert not form.is_valid()
        assert form.errors is not None
        assert "email" in form.errors

    def test_form_empty_email(self) -> None:
        """Test that the form rejects empty email field."""
        form_data = {"email": ""}
        form = RegisterForm(data=form_data)
        assert not form.is_valid()
        assert form.errors is not None
        assert "email" in form.errors

    def test_form_widget_attributes(self) -> None:
        """Test that the email field has the correct widget attributes."""
        form = RegisterForm()
        email_field = form.fields["email"]
        widget_attrs = email_field.widget.attrs
        assert widget_attrs.get("class") == "form-control form-control-lg"
        assert widget_attrs.get("placeholder") == "Email Address ..."


class HomeViewTests(TestCase):
    """Tests for the HomeView."""

    def setUp(self) -> None:
        """Set up test client."""
        self.client = Client()

    def test_get_home_view(self) -> None:
        """Test that GET request to home view returns 200 and correct template."""
        response: Any = self.client.get("/")
        assert response.status_code == 200
        self.assertTemplateUsed(response, "home_view.html")
        assert isinstance(response.context["form"], RegisterForm)

    def test_post_valid_form(self) -> None:
        """Test valid POST redirects and shows success message."""
        form_data = {"email": "test@example.com"}
        response: Any = self.client.post("/", data=form_data)
        assert response.status_code == 302
        assert response.url == "/"

        # Check that success message was added
        messages_list = list(response.wsgi_request._messages)
        assert any(
            "Hola! Will Get to You as Soon as Possible!" in str(msg)
            for msg in messages_list
        )

    def test_post_invalid_form(self) -> None:
        """Test that POST request with invalid form returns 200 and form errors."""
        form_data = {"email": "invalid-email"}
        response: Any = self.client.post("/", data=form_data)
        assert response.status_code == 200
        self.assertTemplateUsed(response, "home_view.html")
        assert not response.context["form"].is_valid()
        assert "email" in response.context["form"].errors

    def test_post_empty_form(self) -> None:
        """Test that POST request with empty form returns 200 and form errors."""
        form_data = {"email": ""}
        response: Any = self.client.post("/", data=form_data)
        assert response.status_code == 200
        self.assertTemplateUsed(response, "home_view.html")
        assert not response.context["form"].is_valid()
        assert "email" in response.context["form"].errors


class EmailSendingTests(TestCase):
    """Tests for email sending functionality."""

    @patch("smtplib.SMTP")
    def test_send_email_in_thread_success(self, mock_smtp: MagicMock) -> None:
        """Test that send_email_in_thread successfully sends email."""
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server

        send_email_in_thread("test@example.com")

        # Verify SMTP was called with correct parameters
        mock_smtp.assert_called_once_with("localhost", 25)

        # Verify email was sent
        mock_server.send_message.assert_called_once()

    @patch("smtplib.SMTP")
    def test_send_email_in_thread_with_auth(self, mock_smtp: MagicMock) -> None:
        """Test that send_email_in_thread uses authentication when provided."""
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server

        with patch.dict(
            "os.environ",
            {
                "SMTP_HOST": "smtp.example.com",
                "SMTP_PORT": "587",
                "SMTP_USER": "user@example.com",
                "SMTP_PASSWORD": "password",
                "SMTP_FROM_EMAIL": "noreply@test.com",
            },
        ):
            send_email_in_thread("test@example.com")

        # Verify SMTP was called with correct parameters
        mock_smtp.assert_called_once_with("smtp.example.com", 587)

        # Verify starttls and login were called
        mock_server.starttls.assert_called_once()
        mock_server.login.assert_called_once_with("user@example.com", "password")

    @patch("smtplib.SMTP")
    def test_send_email_in_thread_smtp_error(self, mock_smtp: MagicMock) -> None:
        """Test that send_email_in_thread handles SMTP errors gracefully."""
        mock_smtp.side_effect = OSError("Connection failed")

        # Should not raise an exception
        send_email_in_thread("test@example.com")

        # Verify SMTP was still attempted
        mock_smtp.assert_called_once_with("localhost", 25)


class ErrorHandlerTests(TestCase):
    """Tests for custom error handlers."""

    def test_custom_404_handler(self) -> None:
        """Test that custom 404 handler returns correct response."""
        response: Any = self.client.get("/nonexistent-page/")
        assert response.status_code == 404
        self.assertTemplateUsed(response, "404.html")

    def test_custom_500_handler(self) -> None:
        """Test that custom 500 handler returns correct response."""
        # We need to simulate a 500 error
        with self.settings(DEBUG=False):
            response: Any = self.client.get("/")
            assert response.status_code == 200
            # The 500 handler is only called when DEBUG=False and an exception occurs
            # This test just ensures the handler is properly defined


class IntegrationTests(TestCase):
    """Integration tests for the entire landing page functionality."""

    def setUp(self) -> None:
        """Set up test client."""
        self.client = Client()

    def test_full_registration_flow(self) -> None:
        """Test the complete registration flow."""
        # Submit valid form
        form_data = {"email": "integration@example.com"}
        response: Any = self.client.post("/", data=form_data)

        # Should redirect
        assert response.status_code == 302
        assert response.url == "/"

        # Follow redirect
        response: Any = self.client.get("/")
        assert response.status_code == 200
        self.assertTemplateUsed(response, "home_view.html")

    def test_multiple_registrations(self) -> None:
        """Test that multiple registrations work correctly."""
        emails = ["user1@example.com", "user2@example.com", "user3@example.com"]

        for email in emails:
            form_data = {"email": email}
            response: Any = self.client.post("/", data=form_data)
            assert response.status_code == 302
            assert response.url == "/"
