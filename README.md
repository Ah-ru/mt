# Quiz app


## Краткое описание

Веб-приложение позволяет сохранять вопросы викторины со следующего <b>API: https://jservice.io/api/random?count=1</b>.
  
### Маршруты:
  - http://host:5050/api/quiz - POST. В качестве параметров принимается JSON вида {"questions_num": integer}, где questions_num - кол-во вопросов к викторине. В качестве ответа - результат **предыдущего запроса**.
  - http://host:5050/api/quiz - GET. Посмотреть все сохраненные вопросы.
  - http://host:5050/api/quiz/testexisted - POST. Точка входа для тестирования отправки запроса с уже существующим вопросом (неуникальный id).

### Используемые технологии:
  - Python
  - Flask
  - SqlAlchemy
  - Postgres
  - Docker 🐳
  - Docker-compose 🐋
  - Postman
  - Gunicorn

## Инструкция по развертыванию
  1. Склонируйте текущий репозиторий при помощи команды:
  
  ```
    git clone https://github.com/777boeing777/FlaskQuiz.git
  ```
  
  2. Перейдите в папку FlaskQuiz:
  
  ```
  cd FlaskQuiz
  ```
  
  3. Убедитесь, что вы находитесь в директории с файлами из репозитория. Запустите сборку образов при помощи команды:
  
  ```
  docker-compose run app flask db upgrade
  ```
  
  4. Запустите контейнеры:
  
  ```
  docker-compose up
  ```
  
## Тестирование в POSTMAN:
  В репозитории находится специальный файл под названием **FlaskQuiz.postman_collection.json**.
  Импортируйте данный файл:
  
  ![image](https://github.com/777boeing777/FlaskQuiz/assets/92817776/352a997b-b623-47a7-8bde-56b63d7137e1)

  В данном файле перечислены все необходимые виды запросов для тестирования работы приложения. **Не забудьте изменить значение переменной {{ host }} в POSTMAN!**
  


