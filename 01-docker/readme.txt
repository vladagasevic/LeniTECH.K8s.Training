U ovom folderu nalazi se docker fajlovi za prakticnu vezbu pokretanja php aplikacije pomocu docker init alata.

1. preuzeti aplikaciju: git clone https://github.com/docker/docker-php-sample
2. docker init
? What application platform does your project use? PHP with Apache
? What version of PHP do you want to use? 8.2
? What's the relative directory (with a leading .) for your app? ./src
? What local port do you want to use to access your server? 9000
3. docker compose up --build
docker compose up --build -d / pokretanje aplikaciju u pozadini
4. docker compose down / brisanje aplikacije

Test aplikacije: 
- http://localhost:9000/hello.php
- http://localhost:9000/database.php

Za vise detalja: https://docs.docker.com/guides/php/develop/
