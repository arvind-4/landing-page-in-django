"""Views for the landing app."""

import os
import smtplib
import threading
from email.message import EmailMessage

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from landing.forms import RegisterForm


def send_email_in_thread(email_address: str) -> None:
    """Send a welcome email via SMTP in a background thread."""
    host = os.environ.get("SMTP_HOST", "localhost")
    port = int(os.environ.get("SMTP_PORT", "25"))
    user = os.environ.get("SMTP_USER", "")
    password = os.environ.get("SMTP_PASSWORD", "")
    from_email = os.environ.get("SMTP_FROM_EMAIL", "noreply@example.com")

    msg = EmailMessage()
    msg["Subject"] = "Thank you for registering!"
    msg["From"] = from_email
    msg["To"] = email_address
    msg.set_content(
        "Hola! Will Get to You as Soon as Possible!",
    )

    def _send() -> None:
        try:
            with smtplib.SMTP(host, port) as server:
                if user and password:
                    server.starttls()
                    server.login(user, password)
                server.send_message(msg)
        except OSError:
            pass

    t = threading.Thread(target=_send, daemon=True)
    t.start()


class HomeView(View):
    """Home page view with registration form."""

    def get(
        self,
        request: HttpRequest,
        *_args: object,
        **_kwargs: object,
    ) -> HttpResponse:
        """Render the home page with an empty registration form."""
        context = {
            "form": RegisterForm(),
        }
        return render(request, "home_view.html", context=context)

    def post(
        self,
        request: HttpRequest,
        *_args: object,
        **_kwargs: object,
    ) -> HttpResponse:
        """Handle registration form submission."""
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data["email"]
            send_email_in_thread(new_email)
            messages.success(request, "Hola! Will Get to You as Soon as Possible!")
            return redirect("/")
        context = {
            "form": form,
        }
        return render(request, "home_view.html", context=context)


def custom_404(
    request: HttpRequest,
    *_args: object,
    **_kwargs: object,
) -> HttpResponse:
    """Render the 404 error page."""
    return render(request=request, template_name="404.html", status=404)


def custom_500(
    request: HttpRequest,
    *_args: object,
    **_kwargs: object,
) -> HttpResponse:
    """Render the 500 error page."""
    return render(request=request, template_name="500.html", status=500)
