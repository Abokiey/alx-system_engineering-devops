# install flask from pip3 using puppet

exec {'apt-get update':
  command => 'apt-get update',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
