import warnings
from pypeerassets.kutil import Kutil
from pypeerassets.protocol import Deck
from pypeerassets import pavoteproto
from hashlib import sha256
from binascii import unhexlify


def deck_vote_tag(deck):
    '''deck vote tag address'''

    deck_vote_tag_privkey = sha256(deck.asset_id + b"vote_init").hexdigest()
    deck_vote_tag_address = Kutil(deck.network, privkey=deck_vote_tag_privkey)
    return deck_vote_tag_address.address


class Vote:

    def __init__(self, version: int, description: str, count_mode: str,
                 choices=[], metainfo=None):
        '''initialize vote object'''

        self.version = version
        self.description = description
        self.choices = choices
        self.count_mode = count_mode
        self.metainfo = metainfo

    @property
    def vote_info_to_protobuf(self):
        '''encode vote into protobuf'''

        vote = pavoteproto.Vote()
        vote.version = self.version
        vote.description = self.description
        vote.count_mode = vote.MODE.Value(self.count_mode)
        vote.choices.extend(self.choices)

        if not isinstance(self.asset_specific_data, bytes):
            vote.metainfo = self.metainfo.encode()
        else:
            vote.metainfo = self.metainfo

        proto = vote.SerializeToString()

        if len(proto) > 80:
            warnings.warn('\nMetainfo size exceeds maximum of 80 bytes allowed by OP_RETURN.')

        return proto

    @property
    def vote_info_to_dict(self):
        '''vote info as dict'''

        return {
            "version": self.version,
            "description": self.description,
            "count_mode": self.count_mode,
            "choices": self.choices
        }


def vote_init(self):
    '''initialize vote transaction'''
    pass


def vote_cast(deck: Deck, deck_vote_tag: str, vote: Vote, inputs: list,
              change_address: str) -> bytes:
    '''vote cast transaction'''
    pass
