import random

def handle_response(message: str) -> str:
    p_message = message.lower()
    
    if p_message == 'hello':
        return 'hello there!'
    
    if p_message == 'roll':
        return str(random.randint(1, 99))
    
    if p_message == '!help':
        return " 'help message' "
    