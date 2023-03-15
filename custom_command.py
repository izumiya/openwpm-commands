import logging

from selenium.common import WebDriverException, NoSuchElementException, TimeoutException
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from openwpm.commands.types import BaseCommand
from openwpm.config import BrowserParams, ManagerParams
from openwpm.socket_interface import ClientSocket


class ElementLocatedOrBrowserClosedOrUrlChanged:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            current_url = driver.current_url
            if current_url == "about:finish":
                return "url_changed"
            element = driver.find_element(*self.locator)
            return element if element.is_displayed() else None
        except NoSuchElementException:
            return None
        except WebDriverException:
            return "browser_closed"


class ManualOperationCommand(BaseCommand):

    def __init__(self, timeout) -> None:
        self.logger = logging.getLogger("openwpm")
        self.timeout = timeout

    # While this is not strictly necessary, we use the repr of a command for logging
    # So not having a proper repr will make your logs a lot less useful
    def __repr__(self) -> str:
        return "ManualOperationCommand"

    # Have a look at openwpm.commands.types.BaseCommand.execute to see
    # an explanation of each parameter
    def execute(
            self,
            webdriver: Firefox,
            browser_params: BrowserParams,
            manager_params: ManagerParams,
            extension_socket: ClientSocket,
    ) -> None:
        # WebDriverWaitを使って、要素が表示されるか、ブラウザが閉じられるか、URLがabout:finishに変わるまで待ちます
        wait = WebDriverWait(webdriver, timeout=self.timeout)
        try:
            result = wait.until(ElementLocatedOrBrowserClosedOrUrlChanged((By.ID, "element_id")))
            if isinstance(result, str) and result == "browser_closed":
                print("ブラウザが閉じられました")
            elif isinstance(result, str) and result == "url_changed":
                print("URLがabout:finishに変更されました")
            else:
                print("要素が表示されました")
        except TimeoutException:
            print("タイムアウトしました")
