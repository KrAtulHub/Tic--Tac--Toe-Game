# 🎮 Tic Tac Toe (NumPy + Streamlit)

A classic Tic Tac Toe game built using **Python**. This project demonstrates how to combine **Streamlit** for the interactive frontend and **NumPy** for efficient game logic and state management.

## 📸 Screenshots

<img width="934" height="751" alt="Screenshot 2026-01-07 101618" src="https://github.com/user-attachments/assets/3aa6ef01-75a0-4205-9f01-dab0128c402c" />


## 🚀 Features

* **Interactive UI:** Built with Streamlit for a clean, web-based interface.
* **NumPy Logic:** Uses 3x3 NumPy arrays to handle the game board.
* **Mathematical Win Check:** instead of complex if-statements, it uses array sums and traces to determine the winner (Row/Col/Diagonal sums of `3` or `-3`).
* **Session State:** Maintains game history and turns without reloading the page.
* **Instant Reset:** One-click button to clear the board and restart.

## 🛠️ Tech Stack

* [Python 3.x](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [NumPy](https://numpy.org/)

## ⚙️ Installation & Run

1.  **Clone the repository** (or download the `app.py` file):
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install dependencies:**
    ```bash
    pip install streamlit numpy
    ```

3.  **Run the app:**
    ```bash
    streamlit run app.py
    ```

4.  **Open in Browser:**
    The app will typically run at `http://localhost:8501`.

## 🧠 How it Works

The game logic relies on a mathematical approach using values assigned to players:

* **Player X** = `1`
* **Player O** = `-1`
* **Empty Space** = `0`

**Winning Condition:**
The code checks the sum of rows, columns, and diagonals (trace).
* If the sum is **3**, Player **X** wins.
* If the sum is **-3**, Player **O** wins.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests. You can add features like:
* An AI opponent (Minimax algorithm).
* Score tracking across multiple games.
* Custom themes.
