# Using Puppet, create a manifest that kills a process named killmenow

exec { 'to kill':
  command  => 'pkill -f killmenow'
  provider => 'shell'
}
