# This puppet will instal flask from pip3

exec { 'insall flask':
  command => '/usr/bin/pip3 install flask',
  path    => '/usr/bin',
  unless  => '/usr/bin/pip3 show flask',
  require => Package['python3-pip']
}
