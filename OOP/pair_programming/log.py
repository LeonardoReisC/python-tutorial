from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:  # class is abstracted
    def _log(self, msg):
        # method must be implemented in child classes
        raise NotImplementedError("Implement log method")

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        formatted_msg = f'{msg} ({self.__class__.__name__})'
        print(f'Saving "{formatted_msg}" in log')
        with open(LOG_FILE, 'a') as file:
            file.write(formatted_msg)
            file.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


# will not be run if this module is imported
if __name__ == "__main__":
    lp = LogPrintMixin()
    lp.log_error("___")
    lp.log_success("___")
    print()

    lf = LogFileMixin()
    lf.log_error("___")
    lf.log_success("___")
