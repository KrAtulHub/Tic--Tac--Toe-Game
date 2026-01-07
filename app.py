import streamlit as st
import numpy as np

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.winner = None

def check_winner(board):
    if 3 in np.sum(board, axis=1) or 3 in np.sum(board, axis=0):
        return "X"
    if -3 in np.sum(board, axis=1) or -3 in np.sum(board, axis=0):
        return "O"
    if np.trace(board) == 3 or np.trace(np.fliplr(board)) == 3:
        return "X"
    if np.trace(board) == -3 or np.trace(np.fliplr(board)) == -3:
        return "O"
    if not np.any(board == 0):
        return "Draw"
    return None

def reset_game():
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.winner = None

st.title("🎮 Tic Tac Toe (NumPy + Streamlit)")

player = "X" if st.session_state.current == 1 else "O"
st.subheader(f"Current Player: {player}")

# Draw board
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        symbol = ""
        if st.session_state.board[i, j] == 1:
            symbol = "❌"
        elif st.session_state.board[i, j] == -1:
            symbol = "⭕"

        if cols[j].button(symbol or " ", key=f"{i}-{j}", use_container_width=True):
            if st.session_state.board[i, j] == 0 and not st.session_state.winner:
                st.session_state.board[i, j] = st.session_state.current
                st.session_state.winner = check_winner(st.session_state.board)
                st.session_state.current *= -1
                st.rerun()

# Show result
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("🤝 It's a Draw!")
    else:
        st.success(f"🎉 Player {st.session_state.winner} Wins!")

    st.button("🔁 Restart Game", on_click=reset_game)
