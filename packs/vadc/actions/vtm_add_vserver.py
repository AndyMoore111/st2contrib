#! /usr/bin/python

import requests
import sys
from st2actions.runners.pythonrunner import Action

from lib.vadc import Vtm

class VtmAddVserver(Action):

    def run(self, vtm, name, pool, tip):

		vtm = Vtm(self.config, self.logger, vtm)
		vtm.addVserver(name, pool, tip)
