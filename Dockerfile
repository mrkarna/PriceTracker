FROM joyzoursky/python-chromedriver:3.7
COPY . /
RUN pip install selenium
RUN pip install telegram_send
# RUN printf "1782618485:AAGk6TxOkq0FyW7YWlpDu5lo3aAnszd_uDM\npub\nt.me/amazPT" | telegram-send --configure-channel
EXPOSE $PORT
CMD [ "python", "./main.py"]