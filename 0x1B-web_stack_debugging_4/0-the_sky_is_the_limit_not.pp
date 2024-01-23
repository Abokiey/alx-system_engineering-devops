# Increases the ULIMIT of default file

exec { 'nginx_fix':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

#restart Nginx

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
