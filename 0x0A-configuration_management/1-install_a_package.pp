# install flask from pip3 using puppet

exec {'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => ['/usr/bin'],
  refreshonly => true,
}

package {'python3-pip':
  ensure => installed,
  before => Exec['install_flask'],
}
