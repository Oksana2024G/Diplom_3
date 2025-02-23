import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент")
    def find_element(self, locator, timeout=10):
       WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
       return self.driver.find_element(*locator)

    @allure.step("Ожидание появления элемента")
    def wait_for_element_presence(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Подождать кликабельности элемента")
    def wait_for_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=17):
        element = self.wait_for_clickable_element(locator, timeout)
        element.click()

    @allure.step("ВВести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    def check_text_on_page(self):
        return self.driver.page_source

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить значение аттрибута элемента")
    def get_attribute(self, locator, attribute):
        element = self.driver.find_element(*locator)
        return element.get_attribute(attribute)

    @allure.step("Подождать пока элемент не станет невидимым")
    def wait_for_element_hide(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Drop ingredient into basket')
    def drag_and_drop_element(self, source_locator, target_locator, timeout=10):
        source = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(source_locator))
        target = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(target_locator))

        # JavaScript для имитации drag and drop. Обычный метод drag and drop в браузере Firefox не работает.

        self.driver.execute_script("""
            function simulateDragAndDrop(sourceNode, destinationNode) {
                var EVENT_TYPES = {
                    DRAG_END:   'dragend',
                    DRAG_START: 'dragstart',
                    DROP:       'drop'
                };

                function createEvent(type, properties) {
                    var event = document.createEvent("HTMLEvents");
                    event.initEvent(type, true, true);
                    for (var property in properties) {
                        event[property] = properties[property];
                    }
                    return event;
                }

                var dragStartEvent = createEvent('dragstart', { clientX: 1, clientY: 1, dataTransfer: { effectAllowed: 'move', setData: function() {} }});
                sourceNode.dispatchEvent(dragStartEvent);

                var dropEvent = createEvent('drop', { clientX: 1, clientY: 1, dataTransfer: dragStartEvent.dataTransfer });
                destinationNode.dispatchEvent(dropEvent);

                var dragEndEvent = createEvent('dragend', { clientX: 1, clientY: 1, dataTransfer: dropEvent.dataTransfer });
                sourceNode.dispatchEvent(dragEndEvent);
            }

            var source = arguments[0];
            var target = arguments[1];
            simulateDragAndDrop(source, target);
            """, source, target)
