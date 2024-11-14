import pygame
import time
from constants import WHITE, BLACK, TILE_SIZE, TILE_ORIGIN, MOVE_FONT, LARGE_FONT, MEDIUM_FONT
from tictactoe import X, O, EMPTY, result, minimax, terminal, player

def draw_initial_screen(screen):
    """
    Draws the initial screen where the user can choose to play as X or O.
    """
    title = LARGE_FONT.render("Play Tic-Tac-Toe", True, WHITE)
    title_rect = title.get_rect(center=(300, 50))
    screen.blit(title, title_rect)

    # Play as X Button
    playX_button = pygame.Rect(75, 200, 150, 50)
    pygame.draw.rect(screen, WHITE, playX_button)
    playX_text = MEDIUM_FONT.render("Play as X", True, BLACK)
    playX_text_rect = playX_text.get_rect(center=playX_button.center)
    screen.blit(playX_text, playX_text_rect)

    # Play as O Button
    playO_button = pygame.Rect(375, 200, 150, 50)
    pygame.draw.rect(screen, WHITE, playO_button)
    playO_text = MEDIUM_FONT.render("Play as O", True, BLACK)
    playO_text_rect = playO_text.get_rect(center=playO_button.center)
    screen.blit(playO_text, playO_text_rect)

    # Check if button is clicked
    if pygame.mouse.get_pressed()[0]:
        mouse = pygame.mouse.get_pos()
        if playX_button.collidepoint(mouse):
            time.sleep(0.2)
            return X
        elif playO_button.collidepoint(mouse):
            time.sleep(0.2)
            return O

def draw_game_board(screen, board):
    """
    Draws the Tic-Tac-Toe game board.
    """
    for i in range(3):
        for j in range(3):
            # Ensure board has valid dimensions before accessing elements
            if i < len(board) and j < len(board[i]):
                rect = pygame.Rect(
                    TILE_ORIGIN[0] + j * TILE_SIZE,
                    TILE_ORIGIN[1] + i * TILE_SIZE,
                    TILE_SIZE, TILE_SIZE
                )
                pygame.draw.rect(screen, WHITE, rect, 3)
                
                # Render the X or O move if present on the board
                if board[i][j] != EMPTY:
                    move = MOVE_FONT.render(board[i][j], True, WHITE)
                    move_rect = move.get_rect(center=rect.center)
                    screen.blit(move, move_rect)

def show_title(screen, text, game_over=False, winner=None):
    """
    Shows the title text based on the game status.
    """
    title_text = f"Game Over: {winner} wins." if game_over and winner else f"Game Over: Tie." if game_over else f"Play as {text}"
    title = LARGE_FONT.render(title_text, True, WHITE)
    title_rect = title.get_rect(center=(300, 30))
    screen.blit(title, title_rect)

def check_ai_move(ai_turn, board):
    """
    Checks and performs the AI's move using minimax.
    """
    if ai_turn:
        time.sleep(0.5)
        board = result(board, minimax(board))
        return False, board
    return True, board

def check_user_move(screen, board):
    """
    Checks and performs the user's move based on mouse clicks.
    """
    if pygame.mouse.get_pressed()[0]:
        mouse = pygame.mouse.get_pos()
        for i in range(3):
            for j in range(3):
                rect = pygame.Rect(TILE_ORIGIN[0] + j * TILE_SIZE, TILE_ORIGIN[1] + i * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if board[i][j] == EMPTY and rect.collidepoint(mouse):
                    return result(board, (i, j))
    return board

def draw_restart_button(screen):
    """
    Draws the "Restart" button on the screen and checks if it was clicked.
    Returns True if the button was clicked, signaling a game restart.
    """
    restart_button = pygame.Rect(225, 320, 150, 50)  # Position and size for the restart button
    pygame.draw.rect(screen, WHITE, restart_button)

    # Center the text in the button
    restart_text = MEDIUM_FONT.render("Restart", True, BLACK)
    restart_text_rect = restart_text.get_rect(center=restart_button.center)
    screen.blit(restart_text, restart_text_rect)

    # Check if the restart button is clicked
    if pygame.mouse.get_pressed()[0]:
        mouse = pygame.mouse.get_pos()
        if restart_button.collidepoint(mouse):
            time.sleep(0.2)
            return True  # Signal to restart the game
    return False  # No restart triggered

