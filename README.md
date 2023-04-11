# Telegram_Bot_Converter_Ru_Eng
DS-0 - Telegram bot - week_3



- Установите Docker: запустите терминал ->  в окне терминала -> `sudo snap install docker`
- запустите IDE;
- в окне терминала IDE введите `docker build .`
- проверьте создание images: в окне терминала -> `docker images`
- скопируйте идентификатор images 
- введите в терминале `docker run -d -p 80:80 < идентификотор images >`
- проверьте запущенный контейнер: в окне терминала -> `docker ps`
- остановите контейнер: в окне терминала -> `docker stop < номер контейнера >`
