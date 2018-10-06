FROM python:3.6-alpine

LABEL maintainer="Sudarsan Bhargavan"

WORKDIR /TicTacToe

ADD ./Game.py /TicTacToe/Game.py
ADD GameEngine /TicTacToe/GameEngine
ADD GamePlatform /TicTacToe/GamePlatform
ADD GameUI /TicTacToe/GameUI

ENV TERM xterm

CMD python3 /TicTacToe/Game.py
