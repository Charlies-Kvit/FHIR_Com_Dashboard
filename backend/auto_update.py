import datetime
import time
import requests
import logging

logging.basicConfig(filename="logs/update_parse.log", filemode="w", level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
while True:
    delta = datetime.timedelta(hours=3, minutes=0)
    date = (datetime.datetime.now(datetime.timezone.utc) + delta).strftime('%H:%M')
    hours = int(date[:date.find(":")])
    minutes = int(date[date.find(":") + 1:])
    logging.info("Проверяю время")
    if hours == 23 and 58 <= minutes <= 59:
        logging.info("Начало обновления")
        try:
           requests.get("http://49.13.48.163/update_parsing")
           logging.info("Успешно!")
        except Exception as error:
            logging.error(f"Ошибка! {error}")
        time.sleep(72000)
    time.sleep(60)
