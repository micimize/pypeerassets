from pypeerassets.networks import query
from pypeerassets.exceptions import UnsupportedNetwork
import requests


class Provider:

    @staticmethod
    def _netname(name: str) -> dict:
        '''resolute network name,
        required because some providers use shortnames and other use longnames.'''

        try:
            long = query(name).network_name
            short = query(name).network_shortname
        except AttributeError:
            raise UnsupportedNetwork('''This blockchain network is not supported by the pypeerassets, check networks.py for list of supported networks.''')

        return {'long': long,
                'short': short}

    @property
    def network(self) -> str:
        '''return network full name'''

        return self._netname(self.net)['long']

    @property
    def is_testnet(self) -> bool:
        """testnet or not?"""

        if "testnet" in self.network:
            return True
        else:
            return False

    @classmethod
    def sendrawtransaction(cls, rawtxn: str) -> dict:
        '''sendrawtransaction'''

        if cls.is_testnet:
            url = 'talk.peercoin.net:5555/pushapi/testnet/sendrawtransaction/'
        else:
            url = 'talk.peercoin.net:5555/pushapi/sendrawtransaction/'

        resp = requests.get(url + rawtxn)
        return resp
