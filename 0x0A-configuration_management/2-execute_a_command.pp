# kills killmenow manifest

exec {'pkill killmenow':
  path => '/usr/bin:/usr/sbin:/bin'
}
