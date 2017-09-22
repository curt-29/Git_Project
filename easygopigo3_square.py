#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
import time
import easygopigo3

gpg3_obj = easygopigo3.EasyGoPiGo3()

gpg3_obj.backward()
time.sleep(2.0)
gpg3_obj.stop()
gpg3_obj.turn_degrees (-90.0)
time.sleep(2.0)

gpg3_obj.backward()
time.sleep(2.0)
gpg3_obj.stop()
gpg3_obj.turn_degrees (-90.0)
time.sleep(2.0)

gpg3_obj.backward()
time.sleep(2.0)
gpg3_obj.stop()
gpg3_obj.turn_degrees (-90.0)
time.sleep(2.0)

gpg3_obj.backward()
time.sleep(2.0)
gpg3_obj.stop()
gpg3_obj.turn_degrees (-90.0)
time.sleep(2.0)
gpg3_obj.stop()
