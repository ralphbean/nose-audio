import os
import subprocess

from nose.plugins import Plugin


assets = "/".join([os.path.dirname(__file__), "assets"])
default_busy = "/".join([assets, "the-price-is-right-busy.ogg"])
default_success = "/".join([assets, "the-price-is-right-success.ogg"])
default_failure = "/".join([assets, "the-price-is-right-failure.ogg"])


def play(filename, repeat=False):
    if not os.path.exists(filename):
        return
    cmd = "ogg123" + (" -r " if repeat else " ") + filename
    process = subprocess.Popen(
        [cmd],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    return process


class NoseAudioPlugin(Plugin):
    """ Play audio files during test execution for fun and profit. """
    enabled = True
    name = 'naudio'

    def options(self, parser, env=os.environ):
        super(NoseAudioPlugin, self).options(parser, env=env)
        parser.add_option(
            '--no-audio', dest='silence', action='store_true',
            help='Turn off musical tests; disable the plugin.')
        parser.add_option(
            '--audio-busy', default=default_busy, dest='audio_busy',
            help='The path to an audio file to play while tests are running.')
        parser.add_option(
            '--audio-success', default=default_success, dest='audio_success',
            help='The path to an audio file to play when tests succeed.')
        parser.add_option(
            '--audio-failure', default=default_failure, dest='audio_failure',
            help='Ruh-roh.  Path to an audio file to play when tests fail.')

    def configure(self, options, conf):
        super(NoseAudioPlugin, self).configure(options, conf)
        self.enabled = not options.silence
        self.options = options

    def begin(self):
        if self.enabled:
            self.busy_process = play(self.options.audio_busy, repeat=True)
        else:
            self.busy_process = None

    def finalize(self, result):
        if not (result.errors or result.failures):
            print("-" * 70)
            print("Success!")
            outro = play(self.options.audio_success)
        else:
            print("-" * 70)
            print("Uh-oh...")
            outro = play(self.options.audio_failure)

        if self.busy_process:
            self.busy_process.kill()
            self.busy_process = None

        outro.wait()
        return False
