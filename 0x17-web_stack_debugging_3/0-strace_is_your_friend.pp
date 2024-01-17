# debug why apache is returning error 500 in a wordpress site

exec { 'fix_path':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin/', '/bin/']
}
