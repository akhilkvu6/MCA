# 📘 README

<div align="center">

# 🖥️ E24_InstallationOfLAMP

### NSA Lab – Installation of LAMP Stack

</div>

---

# 🎯 Aim

To install and configure the LAMP stack (Linux, Apache, MySQL, PHP) for hosting dynamic websites and web applications.

---

# 📘 Introduction

LAMP is a popular open-source web development platform used to host websites and web applications.

LAMP stands for:

| Letter | Component | Description                    |
| ------ | --------- | ------------------------------ |
| L      | Linux     | Operating System               |
| A      | Apache    | Web Server                     |
| M      | MySQL     | Database Management System     |
| P      | PHP       | Server-side Scripting Language |

The LAMP stack allows:

* hosting websites
* running PHP applications
* storing data in MySQL databases
* managing dynamic web content

LAMP is widely used because it is:

* free and open-source
* reliable
* secure
* scalable
* easy to configure

---

# 🧠 Components of LAMP Stack

---

# 🐧 1. Linux

Linux is the operating system on which the web server runs.

## 📌 Features

* Open-source
* Secure
* Multi-user
* Stable
* Efficient resource management

## 📌 Examples

* Ubuntu
* Debian
* CentOS
* Fedora

---

# 🌐 2. Apache Web Server

Apache is one of the most widely used web servers.

## 📌 Functions

* Serves web pages to clients
* Handles HTTP requests
* Supports virtual hosting
* Processes static content

## 📌 Features

* Open-source
* Highly configurable
* Module support
* SSL support

---

# 🗄️ 3. MySQL

MySQL is a relational database management system (RDBMS).

## 📌 Functions

* Stores website data
* Manages databases
* Executes SQL queries

## 📌 Features

* Multi-user database
* High performance
* Secure authentication
* Structured data storage

---

# 🧩 4. PHP

PHP is a server-side scripting language.

## 📌 Functions

* Generates dynamic web pages
* Connects with MySQL database
* Processes forms
* Executes backend logic

## 📌 Features

* Open-source
* Platform independent
* Easy integration with HTML

---

# ⚙️ System Requirements

Before installing LAMP stack, ensure:

* Ubuntu/Linux installed
* Internet connection available
* Sudo/root access available
* Minimum 2 GB RAM recommended

---

# 🧠 Architecture of LAMP Stack

```text id="x7m2qp"
Client Browser
       ↓
Apache Web Server
       ↓
PHP Processing
       ↓
MySQL Database
```

---

# 🪜 Step 1: Updating Package Repository

Update package manager cache before installation.

## 📌 Command

```bash id="v4n8zk"
sudo apt update
```

## 📌 Purpose

* Refreshes package list
* Downloads latest repository information

---

# 🌐 Step 2: Installing Apache Web Server

Install Apache using apt package manager.

## 📌 Command

```bash id="m4x8qp"
sudo apt install apache2
```

## 📌 Functions of Apache

* Hosts websites
* Handles client requests
* Serves web pages

---

# 🔥 Step 3: Configuring Firewall

Ubuntu uses UFW (Uncomplicated Firewall).

---

# 📌 List Available UFW Profiles

```bash id="q9p1wr"
sudo ufw app list
```

---

# 📌 Common Apache Firewall Profiles

| Profile       | Description            |
| ------------- | ---------------------- |
| Apache        | Opens Port 80          |
| Apache Full   | Opens Ports 80 and 443 |
| Apache Secure | Opens Port 443         |

---

# 📌 Allow HTTP Traffic

```bash id="x5m2vq"
sudo ufw allow in "Apache"
```

---

# 📌 Verify Firewall Status

```bash id="k3v8zp"
sudo ufw status
```

---

# 📌 Test Apache Installation

Open browser and enter:

```text id="p7n1wr"
http://your_server_ip
```

If Apache is installed correctly, Apache default page appears.

---

# 🗄️ Step 4: Installing MySQL

Install MySQL database server.

## 📌 Command

```bash id="t4m9qx"
sudo apt install mysql-server
```

---

# 📌 Login to MySQL Console

```bash id="v8x2zk"
sudo mysql
```

---

# 📌 Functions of MySQL

* Stores website data
* Creates databases
* Executes SQL commands

---

# 🧩 Step 5: Installing PHP

Install PHP and required modules.

## 📌 Command

```bash id="m2q7vp"
sudo apt install php libapache2-mod-php php-mysql
```

---

# 📌 Packages Installed

| Package            | Purpose                |
| ------------------ | ---------------------- |
| php                | Core PHP               |
| libapache2-mod-php | Apache PHP module      |
| php-mysql          | PHP-MySQL connectivity |

---

# 🖥️ Step 6: Creating Virtual Host

Virtual hosts allow hosting multiple websites on a single server.

---

# 📌 Create Website Directory

```bash id="x9p4wr"
sudo mkdir /var/www/your_domain
```

---

# 📌 Change Ownership

```bash id="q5n8zk"
sudo chown -R $USER:$USER /var/www/your_domain
```

---

# 📌 Create Virtual Host Configuration File

```bash id="u4m7xp"
sudo nano /etc/apache2/sites-available/your_domain.conf
```

---

# 📌 Sample Virtual Host Configuration

```apache id="p8x2vq"
<VirtualHost *:80>
    ServerName your_domain
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/your_domain

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

---

# 📌 Enable Virtual Host

```bash id="v3n7zk"
sudo a2ensite your_domain.conf
```

---

# 📌 Disable Default Site

```bash id="m6q1wr"
sudo a2dissite 000-default.conf
```

---

# 📌 Restart Apache

```bash id="x2v8qp"
sudo systemctl reload apache2
```

---

# 📄 Step 7: Creating Test Web Page

Create test HTML file.

## 📌 Command

```bash id="k7m4zx"
nano /var/www/your_domain/index.html
```

---

# 📌 Sample HTML File

```html id="q3x9vp"
<html>
<head>
    <title>LAMP Test</title>
</head>
<body>
    <h1>LAMP Stack Installed Successfully</h1>
</body>
</html>
```

---

# 🌐 Step 8: Testing Website

Open browser and enter:

```text id="v5m2qw"
http://server_domain_or_IP
```

If configuration is correct, webpage displays successfully.

---

# 🧪 Testing PHP

Create PHP test file.

## 📌 Command

```bash id="p4x7zn"
nano /var/www/your_domain/info.php
```

---

# 📌 PHP Test Program

```php id="t9m1qp"
<?php
phpinfo();
?>
```

---

# 📌 Open in Browser

```text id="x6v3wr"
http://server_domain_or_IP/info.php
```

Displays PHP configuration page.

---

# 📂 Directory Structure

```text id="m8q2vx"
/var/www/
    ├── html
    └── your_domain
```

---

# 🔍 Important Commands Summary

| Command                    | Purpose             |
| -------------------------- | ------------------- |
| `apt update`               | Update package list |
| `apt install apache2`      | Install Apache      |
| `apt install mysql-server` | Install MySQL       |
| `apt install php`          | Install PHP         |
| `ufw allow`                | Configure firewall  |
| `systemctl reload apache2` | Restart Apache      |
| `mysql`                    | Open MySQL console  |

---

# ✅ Advantages of LAMP Stack

* Open-source and free
* Highly secure
* Stable platform
* Supports dynamic websites
* Easy to configure
* Large community support

---

# ❌ Limitations

* Requires Linux knowledge
* Manual configuration needed
* High traffic may require optimization

---

# 📚 Viva Questions

## 1️⃣ What is LAMP stack?

LAMP is a web development platform consisting of Linux, Apache, MySQL, and PHP.

---

## 2️⃣ What is Apache?

Apache is a web server used to host websites.

---

## 3️⃣ What is MySQL?

MySQL is a relational database management system.

---

## 4️⃣ What is PHP?

PHP is a server-side scripting language.

---

## 5️⃣ What is a virtual host?

A virtual host allows multiple websites on one server.

---

## 6️⃣ What is UFW?

UFW is Ubuntu’s firewall management tool.

---

## 7️⃣ What is the use of php-mysql package?

It connects PHP with MySQL databases.

---

## 8️⃣ What is localhost?

Localhost refers to the local computer/server itself.

---

## 9️⃣ What is the purpose of Apache ports 80 and 443?

* Port 80 → HTTP
* Port 443 → HTTPS

---

## 🔟 Why is LAMP widely used?

Because it is free, stable, secure, and easy to deploy.

---

# 🎓 Result

Thus, the LAMP stack consisting of Linux, Apache, MySQL, and PHP was installed and configured successfully for hosting dynamic web applications.
