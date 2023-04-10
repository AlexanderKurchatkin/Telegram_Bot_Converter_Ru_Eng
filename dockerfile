FROM python:slim
ENV TOKEN='здесь должен быть TOKEN'
COPY . .
RUN pip install -r req.txt
CMD python converter_bot.py
