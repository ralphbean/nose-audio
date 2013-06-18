import os
import subprocess

from nose.plugins import Plugin


default_busy = os.path.expanduser("~/.local/the-price-is-right-busy.ogg")
default_success = os.path.expanduser("~/.local/the-price-is-right-success.ogg")
default_failure = os.path.expanduser("~/.local/the-price-is-right-failure.ogg")


def play(filename):
    if not os.path.exists(filename):
        return
    cmd = "mplayer " + filename
    process = subprocess.Popen(
        [cmd],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    return process


class NoseAudioPlugin(Plugin):
    enalbed = True
    name = 'naudio'

    def options(self, parser, env=os.environ):
        super(NoseAudioPlugin, self).options(parser, env=env)
        parser.add_option('', '--no-audio',
                          help='turn off musical tests',
                          dest='silence',
                          action='store_true')
        parser.add_option('', '--audio-busy',
                          help='path to busy audio file',
                          default=default_busy,
                          dest='audio_busy')
        parser.add_option('', '--audio-success',
                          help='path to success audio file',
                          default=default_success,
                          dest='audio_success')
        parser.add_option('', '--audio-failure',
                          help='path to failure audio file',
                          default=default_failure,
                          dest='audio_failure')

    def configure(self, options, conf):
        super(NoseAudioPlugin, self).configure(options, conf)
        self.enabled = not options.silence
        self.options = options

    def begin(self):
        if self.enabled:
            self.busy_process = play(self.options.audio_busy)
        else:
            self.busy_process = None

    def finalize(self, result):
        result.printErrors()

        print "-" * 70
        print "Ran %i tests." % result.testsRun

        if result:
            print
            print "OK"

        if self.busy_process:
            self.busy_process.kill()
            self.busy_process = None

        if result:
            outro = play(self.options.audio_success)
        else:
            outro = play(self.options.audio_failure)

        outro.wait()
        return False
