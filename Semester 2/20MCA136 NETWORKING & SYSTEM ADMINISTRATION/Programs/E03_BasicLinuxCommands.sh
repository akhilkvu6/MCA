#!/bin/bash

echo "===== BASIC LINUX COMMANDS ====="

echo "1. man – manual/help"
echo "Shows full documentation of a command"
echo "Command: man ls"

echo "------------------------"

echo "2. ls – list files"
ls -l

echo "------------------------"

echo "3. echo – print/write text"
echo "Hello World"
echo "Hello" > file.txt

echo "------------------------"

echo "4. read – take input"
read -p "Enter your name: " name
echo "$name"

echo "------------------------"

echo "5. cat – display file"
cat file.txt

echo "------------------------"

echo "6. cd – change directory"
echo "Command: cd /home/user/Documents"

echo "------------------------"

echo "7. mkdir – create directory"
mkdir myfolder

echo "------------------------"

echo "8. pwd – print working directory"
pwd

echo "------------------------"

echo "9. mv – move/rename"
mv file.txt newfile.txt

echo "------------------------"

echo "10. cp – copy file"
cp newfile.txt backup.txt

echo "------------------------"

echo "11. rm – delete file"
echo "Command: rm file.txt"

echo "------------------------"

echo "12. touch – create file"
touch new.txt

echo "------------------------"

echo "13. chmod – change permission"
chmod 755 new.txt

echo "------------------------"

echo "14. chown – change owner"
echo "Command: chown user file.txt"

echo "------------------------"

echo "15. more – view file"
more newfile.txt

echo "------------------------"

echo "16. less – advanced viewer"
echo "Command: less newfile.txt"

echo "------------------------"

echo "17. find – search files"
find . -name "newfile.txt"

echo "------------------------"

echo "18. wc – count"
wc newfile.txt

echo "------------------------"

echo "19. cut – extract data"
cut -d ":" -f1 /etc/passwd

echo "------------------------"

echo "20. paste – merge files"
paste newfile.txt backup.txt

echo "------------------------"

echo "21. head – first lines"
head -n 5 newfile.txt

echo "------------------------"

echo "22. tail – last lines"
tail -n 5 newfile.txt

echo "------------------------"

echo "23. useradd – add user"
echo "Command: sudo useradd user1"

echo "------------------------"

echo "24. userdel – delete user"
echo "Command: sudo userdel user1"

echo "------------------------"

echo "25. usermod – modify user"
echo "Command: sudo usermod -aG sudo user1"

echo "------------------------"

echo "26. passwd – change password"
echo "Command: passwd user1"

echo "------------------------"

echo "27. top – system monitor"
echo "Command: top"

echo "------------------------"

echo "28. ps – process status"
ps aux

echo "------------------------"

echo "29. ssh – remote login"
echo "Command: ssh user@192.168.1.100"

echo "------------------------"

echo "30. scp – copy remotely"
echo "Command: scp file.txt user@192.168.1.100:/home/user"