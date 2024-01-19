
# Идентификация и аутентификация 

### 1. Создать виртуальную машину на базе ОС Debian 12
![enter image description here](https://i.imgur.com/zf6ODKa.png)

### 2. Создать пользователя super-rastegaev_i_g, наделить его привилегиями суперпользователя 
```bash
sudo useradd super-rastegaev_i_g
sudo usermod -a -G sudo super-rastegaev_i_g
```
![enter image description here](https://i.imgur.com/g1BTVeD.png)

### 3. Зайти под созданным пользователем и создать группу group-rastegaev-i-g
```bash
su super-rastegaev_i_g
```
![enter image description here](https://i.imgur.com/aKOKVPC.png)
```bash
sudo groupadd group-rastegaev-i-g
```
![enter image description here](https://i.imgur.com/sxnBtbK.png)

### 4. Добавить пользователя super-rastegaev_i_g в группу group-rastegaev-i-g
```bash
sudo usermod -a -G group-rastegaev-i-g super-rastegaev_i_g
```
![enter image description here](https://i.imgur.com/LOab8zh.png)

### 5. Продемонстрировать наличие пользователя в группе
```bash
groups super-rastegaev_i_g
```
![enter image description here](https://i.imgur.com/81LWTsQ.png)

### 6. Создать пользователя user-rastegaev_i_g, добавить его в группу group-rastegaev-i-g
```bash
sudo useradd user-rastegaev_i_g
sudo usermod -a -G group-rastegaev-i-g user-rastegaev_i_g
```
![enter image description here](https://i.imgur.com/FqgpiqE.png)

### 7. Наделить полномочиями (с использованием механизмов дискреционного управления доступом chmod)  пользователя user-rastegaev_i_g по созданию и удалению файлов в домашнем каталоге пользователя super-rastegaev_i_g
![enter image description here](https://i.imgur.com/qfK5Wmd.png)
![enter image description here](https://i.imgur.com/bJrWxWG.png)
```bash
sudo chmod 770 ~
sudo chown super-rastegaev_i_g:group-rastegaev-i-g
```
### 8. Продемонстрировать работу механизмов разграничения доступа
```bash
whoami
cd /home/super-rastegaev_i_g
touch 1.txt
rm 1.txt
```
ДО выполнения 7 шага:

![enter image description here](https://i.imgur.com/DDhGuoM.png)

ПОСЛЕ выполнения 7 шага:

![enter image description here](https://i.imgur.com/N8ZP2t2.png)
