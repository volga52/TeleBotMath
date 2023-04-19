from handlers.handler_com import HandlerCommands, HandlerEcho
from handlers.handler_fsm import HandlerFSM
from handlers.handler_inline import HandlerInline


class HandlerMain:
    """Класс компоновщик"""
    def __init__(self, dp):
        self.dp = dp
        self.handler_commands = HandlerCommands(self.dp)
        self.handler_echo_end = HandlerEcho(self.dp)
        self.handler_fsm = HandlerFSM(self.dp)
        self.handler_inline = HandlerInline(self.dp)

    def handle(self):
        """Инициация обработчиков"""
        self.handler_commands.handler()
        self.handler_fsm.handler()
        self.handler_inline.handler()

        # самый последний обработчик
        self.handler_echo_end.handler()
