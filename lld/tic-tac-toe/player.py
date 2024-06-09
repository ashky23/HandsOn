class Player:
    name = None
    age = None
    piece = None
    
    def __init__(self, name = None, age = None, piece = None) -> None:
        self.name = name 
        self.age = age
        self.piece = piece
        
    def __str__(self):
        return f"Player {self.piece.value}"