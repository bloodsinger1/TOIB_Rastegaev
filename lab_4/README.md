# Лабораторная работа №4
## Растегаев Илья Геннадьевич ББМО-01-23
### Создание ключевой пары GPG

`gpg --full-generate-key`

![enter image description here](https://i.imgur.com/USk48f3.png)
![enter image description here](https://i.imgur.com/5YwMst1.png)


### Просмотр созданных ключей, подписей, секретных ключей, отпечатков

`gpg --list-keys rastegaev.i.g@edu.mirea.ru`

`gpg --list-signatures rastegaev.i.g@edu.mirea.ru`

`gpg --list-secret-keys rastegaev.i.g@edu.mirea.ru`

`gpg --fingerprint rastegaev.i.g@edu.mirea.ru`

![enter image description here](https://i.imgur.com/ySeWu0U.png)
### Создание отзывающего сертификата
Вывод сертификата в консоль | Запись сертификата в файл
--- | ---
`gpg --gen-revoke rastegaev.i.g@edu.mirea.ru` | `gpg --output revoke.asc --gen-revoke rastegaev.i.g@edu.mirea.ru`
![enter image description here](https://i.imgur.com/CIrql60.png) | ![enter image description here](https://i.imgur.com/CjtV45a.png)
### Экспорт публичного ключа в бинарном и текстовом виде
![enter image description here](https://i.imgur.com/4FZgeIM.png)
В бинарном виде | В текстовом виде
--- | ---
`gpg --output rastegaev-pub.gpg` | `gpg --armor --output rastegaev-pub.asc --export rastegaev.i.g@edu.mirea.ru`
![enter image description here](https://i.imgur.com/ttYd4Ad.png) | ![enter image description here](https://i.imgur.com/Tz8Jpt0.png)
### Создание файла для подписи
![enter image description here](https://i.imgur.com/n0t7SH4.png)
### Создание цифровой подписи в бинарном виде

`gpg --local-user rastegaev.i.g@edu.mirea.ru --sign file.txt`

![](https://i.imgur.com/XUcxQbw.png)
### Проверка подписи

`gpg --verity file.txt.gpg`

![enter image description here](https://i.imgur.com/DQBxDfv.png)
### Создание цифровой подписи в формате ASCII

`gpg --local-user rastegaev.i.g@edu.mirea.ru --armor --sign file.txt`

![enter image description here](https://i.imgur.com/nH3RI0N.png)
### Создание цифровой подписи, вставленной в содержимое файла

`gpg --local-user rastegaev.i.g@edu.mirea.ru --clearsign file.txt`

`gpg --verify file.txt.asc`

![enter image description here](https://i.imgur.com/UzJC6zP.png)

