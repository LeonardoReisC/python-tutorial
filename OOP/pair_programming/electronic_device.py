from log import LogFileMixin


class ElectronicDevice:
    def __init__(self, name):
        self._name = name
        self._switched_on = False

    def switch_on(self):
        if not self._switched_on:
            self._switched_on = True

    def switch_off(self):
        if self._switched_on:
            self._switched_on = False

# good practice: prefer composition to inheritance


class SmartPhone(ElectronicDevice, LogFileMixin):  # not a good practice
    def switch_on(self):
        super().switch_on()

        if self._switched_on:
            msg = f'{self._name} is on'
            self.log_success(msg)

    def switch_off(self):
        super().switch_off()

        if not self._switched_on:
            msg = f'{self._name} is off'
            self.log_success(msg)
