import os
import sys


from splitio.factories import get_factory as get_splitio_factory
from splitio.exceptions import TimeoutException


class SplitSDK:

    def __init__(self):
        sdk_config = {
            'labelsEnabled': True
        }
        api_key = os.getenv('SPLIT_KEY')

        self.factory = get_splitio_factory(
            api_key,
            config=sdk_config,
        )
        self.client = None

    def get_client(self):
        if not self.client:
            try:
                self.factory.block_until_ready(5)
            except TimeoutException:
                # The SDK failed to initialize in 5 seconds. Abort!
                sys.exit()

            self.client = self.factory.client()

        return self.client

    def get_treatment(self, uid, treatment_name):
        client = self.client
        if not client:
            client = self.get_client()
        return client.get_treatment(uid, treatment_name)
