import smtplib
import socks
from django.core.mail.backends.smtp import EmailBackend


class ProxyEmailBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False

        # Set up the proxy for SMTP
        socks.setdefaultproxy(
            socks.PROXY_TYPE_HTTP,
            "http://127.0.0.1:12345",
        )  # Replace with your proxy details
        socks.wrapmodule(smtplib)

        # Now call the original SMTP connection method
        return super().open()
