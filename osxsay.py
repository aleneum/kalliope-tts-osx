import os
import subprocess

from kalliope.core.TTS.TTSModule import TTSModule
import logging
import sys

logging.basicConfig()
logger = logging.getLogger("kalliope")


class Osxsay(TTSModule):

    def __init__(self, **kwargs):
        super(Osxsay, self).__init__(**kwargs)

        voice = kwargs.get('voice', None)
        rate = kwargs.get('rate', None)

        self.voice_options = []
        if voice is not None:
            self.voice_options.extend(['-v', voice])
        if rate is not None:
            self.voice_options.extend(['-r', str(rate)])

    def say(self, words):
        """
        :param words: The sentence to say
        """

        self.generate_and_play(words, self._generate_audio_file)

    def _generate_audio_file(self):
        """
        Generic method used as a Callback in TTSModule
            - must provided the audio file and write it on the disk

        .. raises:: FailToLoadSoundFile
        """

        exec_path = ["/usr/bin/say"]
        options_file = ["-o", self.file_path]

        final_command = list()
        final_command.extend(exec_path)
        final_command.extend(options_file)
        final_command.extend(self.voice_options)
        final_command.append(self.words)

        logger.debug("osx 'say' command: %s" % final_command)

        subprocess.check_call(final_command)
