import pygame
import sys
import time

from display import draw_initial_screen, draw_game_board, show_title, check_ai_move, check_user_move, draw_restart_button
from tictactoe import initial_state, X, O, terminal, result, player, winner, minimax
from constants import SIZE, BLACK, WHITE

pygame.init()
screen = pygame.display.set_mode(SIZE)

user = None
board = initial_state()
ai_turn = False

# Main game loop
while True:
    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLACK)

    # Let user choose a player.
    if user is None:
        user = draw_initial_screen(screen)
    else:
        # Draw game board
        draw_game_board(screen, board)

        game_over = terminal(board)
        current_player = player(board)

        # Show title based on game status
        if game_over:
            show_title(screen, user, game_over=True, winner=winner(board))
            # Draw the restart button if the game is over
            if draw_restart_button(screen):
                user = None
                board = initial_state()
                ai_turn = False
                continue  # Restart the game loop with a new game
        elif user == current_player:
            show_title(screen, user)
        else:
            show_title(screen, "Computer thinking...")

        # AI or user move
        if user != current_player and not game_over:
            ai_turn, board = check_ai_move(ai_turn, board)
        elif user == current_player and not game_over:
            board = check_user_move(screen, board)

    pygame.display.flip()

