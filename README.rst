nose-audio
----------

.. split here

Add audio to your test suite.

Simply ``$ pip install nose-audio`` and your ``nosetests`` come alive!

Options
-------

- ``--no-audio``
  Turn off musical tests; disable the plugin.
- ``--audio-busy``
  The path to an audio file to play while tests are running.
- ``--audio-success``
  The path to an audio file to play when tests succeed.
- ``--audio-failure``
  Ruh-roh.  Path to an audio file to play when tests fail.

Those options can also be set in a ``setup.cfg`` file::

    [nosetests]
    audio-busy='~/music/alt/elevator.ogg'
    audio-success='~/music/alt/yes.wav'
    audio-failure='~/music/alt/sad-trombone.wav'

License
-------

.. note:: This tarball includes audio assets for which the author does not
   hold copyright.
