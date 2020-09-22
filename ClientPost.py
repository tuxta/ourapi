from Client import Client
import requests


class ClientPost(Client):
    def __init__(self, parent):
        super().__init__(parent)

        self.setWindowTitle("POST Client")

    def rebuild_url(self):
        super().rebuild_url()
        self.ui.urlText.setText(self.url)

    def run(self):
        self.return_data = requests.post(
            'http://127.0.0.1:8000' + self.url,
            data=self.variables
        )

        super().run()
