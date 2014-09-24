#!/bin/bash
set -e

# Add 'wordpress' to /etc/hosts
echo "===== Adding ${HOSTNAME} to the /etc/hosts file"
sudo -- sh -c "echo 127.0.1.1 ${HOSTNAME} >> /etc/hosts"
echo "----- hostname added to hosts file"

echo "===== Updating apt"
sudo apt-get update
echo "----- apt updated"

echo "===== Installing apache 2 and php 5..."
sudo apt-get install -y apache2 libapache2-mod-php5 php5-cli php5-gd libssh2-php php5-curl
echo "----- Installed apache2."

echo "===== Adding ServerName to apache2 config"
sudo -- sh -c "echo ServerName ${HOSTNAME} >> /etc/apache2/apache2.conf"
echo "----- ServerName added to apache2 config"

echo "===== Installing mysql..."
mysql_root_pass="root"
mysql_wordpress_pass="stack"
sudo debconf-set-selections <<< "mysql-server-5.5 mysql-server/root_password password ${mysql_root_pass}"
sudo debconf-set-selections <<< "mysql-server-5.5 mysql-server/root_password_again password ${mysql_root_pass}"
sudo apt-get -y install mysql-server php5-mysql
echo "----- Installed mysql."

echo "===== Reconfiguring and reinstalling apache..."
sudo ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/
sudo apachectl restart
echo "----- Restarted apache2."

echo "===== Creating mysql wordpress database..."
mysqladmin -u root --password=${mysql_root_pass} create wordpress
echo "----- Database created."

echo "===== Creating wordpress mysql user..."
mysql -u root --password=${mysql_root_pass} wordpress -e "GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpress'@'localhost' IDENTIFIED BY '${mysql_wordpress_pass}';FLUSH PRIVILEGES;"
echo "----- Created wordpress mysql user."

echo "===== Downloading and installing wordpress..."
wget http://wordpress.org/latest.tar.gz
echo "----- Downloaded wordpress."

echo "===== Expanding and configuring wordpress..."
sudo rm -f /var/www/html/index.html
sudo tar fxvz latest.tar.gz -C /var/www/html/ --strip-components=1
sudo mkdir /var/www/html/wp-content/uploads
sudo chown -R ubuntu:www-data /var/www/html
sudo chmod g+w /var/www/html/wp-content/uploads
sudo touch /var/www/html/.htaccess
sudo chown ubuntu:www-data /var/www/html/.htaccess
sudo chmod g+w /var/www/html/.htaccess
cp /var/www/html/wp-config-sample.php /var/www/html/wp-config.php
sed -i 's/database_name_here/wordpress/g' /var/www/html/wp-config.php
sed -i 's/username_here/wordpress/g' /var/www/html/wp-config.php
sed -i 's/password_here/'${mysql_wordpress_pass}'/g' /var/www/html/wp-config.php
echo "----- Configured wordpress."

echo "Wordpress up at http://[floating_ip_address]/wp-admin/install.php"
