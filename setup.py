from setuptools import setup

setup(name='pypeerassets',
      version='0.2.9',
      description='Python implementation of the PeerAssets protocol.',
      keywords=["blockchain", "digital asset", "protocol"],
      url='https://github.com/peerassets/pypeerassets',
      author='PeerAssets',
      author_email='peerchemist@protonmail.ch',
      license='GPL',
      packages=['pypeerassets', 'pypeerassets.provider', 'pypeerassets.crypto'],
      install_requires=['requests', 'protobuf', 'peercoin_rpc', 'cryptography'],
      zip_safe=True)
