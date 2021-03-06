#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 CERN
# Author: Pawel Szostek (pawel.szostek@cern.ch)
#
# This file is part of Hdlmake.
#
# Hdlmake is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hdlmake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hdlmake.  If not, see <http://www.gnu.org/licenses/>.

from action import Action
import global_mod
import logging


class GenerateFetchMakefile(Action):
    def run(self):
        pool = self.modules_pool
        logging.info("Generating makefile for fetching modules.")
        if pool.get_fetchable_modules() == []:
            logging.error("There are no fetchable modules. "
                          "No fetch makefile is produced")
            quit()

        self._check_all_fetched_or_quit()
        global_mod.makefile_writer.generate_fetch_makefile(pool)
        logging.info("Makefile for fetching modules generated.")