from Client import Client
import requests


class ClientGet(Client):
    def __init__(self, parent):
        super().__init__(parent)

        self.setWindowTitle("GET Client")

    def add_variable(self):
        super().add_variable()
        self.rebuild_url()

    def rebuild_url(self):
        super().rebuild_url()
        if len(self.variables) > 0:
            self.url = self.url + '?'
            for var in self.variables.items():
                self.url = self.url + f"{var[0]}={var[1]}&"
            self.url = self.url[:-1]
        self.ui.urlText.setText(self.url)

    def run(self):
        self.return_data = requests.get(
            'http://127.0.0.1:8000' + self.url
        )

        super().run()
