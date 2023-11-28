# nginx_config.pp

# Install Nginx
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

#config files
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx_config/nginx.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Template 
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx_config/nginx.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Notify service restart if configuration file changes
File['/etc/nginx/sites-available/default'] ~> Service['nginx']

