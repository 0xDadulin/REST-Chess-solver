class Figure:
    def __init__(self, position: str):
        self.position = position

    def list_available_moves(self):
        raise NotImplementedError("This method should be overridden by the subclass")

    def validate_move(self, dest_field: str):
        raise NotImplementedError("This method should be overridden by the subclass")
