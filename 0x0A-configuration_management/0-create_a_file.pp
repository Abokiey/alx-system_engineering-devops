# creation of a file having a message and change permissions

file { '/tmp/school':
  content => 'I love Puppet',
  mode    => '0744',
  owner   => www-data,
  group   => www-data,
}
