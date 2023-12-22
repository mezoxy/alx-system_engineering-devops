# Using Puppet, create a manifest that kills a process named killmenow

file { './to_kill':
  file    => 'file',
  mode    => '0777',
  content => 'pkill -f killmenow',
  ensure  => 'present'
}

exec { 'to kill':
  require  => File['./to kill'],
  command => './to_kill'
}
