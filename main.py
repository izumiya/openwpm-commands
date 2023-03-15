#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "OpenWPM"))

from pathlib import Path
from openwpm.config import ManagerParams, BrowserParams
from openwpm.task_manager import TaskManager
from openwpm.storage.sql_provider import SQLiteStorageProvider
from openwpm.command_sequence import CommandSequence
from custom_command import ManualOperationCommand

# Loads the default ManagerParams
manager_params = ManagerParams()
browser_params = [BrowserParams(display_mode="native")]

# Update browser configuration (use this for per-browser settings)
for browser_param in browser_params:
    # Record HTTP Requests and Responses
    browser_param.http_instrument = True
    # Record cookie changes
    browser_param.cookie_instrument = True
    # Record Navigations
    browser_param.navigation_instrument = True
    # Record JS Web API calls
    browser_param.js_instrument = True
    # Record the callstack of all WebRequests made
    browser_param.callstack_instrument = True
    # Record DNS resolution
    browser_param.dns_instrument = True

# Update TaskManager configuration (use this for crawl-wide settings)
manager_params.data_directory = Path(os.path.join(os.path.dirname(__file__), "datadir"))
manager_params.log_path = Path(os.path.join(os.path.dirname(__file__), "datadir/openwpm.log"))

# Commands time out by default after 600 seconds
with TaskManager(
        manager_params,
        browser_params,
        SQLiteStorageProvider(Path(os.path.join(os.path.dirname(__file__), "./datadir/crawl-data.sqlite"))),
        None,
) as manager:
    site = "about:blank"


    def callback(success: bool, val: str = site) -> None:
        print(
            f"CommandSequence for {val} ran {'successfully' if success else 'unsuccessfully'}"
        )


    command_sequence = CommandSequence(
        site,
        callback=callback,
    )
    command_sequence.append_command(ManualOperationCommand(timeout=600))
    manager.execute_command_sequence(command_sequence)
