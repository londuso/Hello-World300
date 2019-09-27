# Hello-World300
NTI 300 class
 1. yum -y install httpd   mod_ssl
 2. systemctl start httpd
 3 sed -I  's/^/#/g '  / etc/httpd/conf.d/welcome.conf
 4 ech "<html><body><h1> Hi there NT1 300</h1></body></html>"  /var/www/html/index
systmctl restart httpd
4 . 
