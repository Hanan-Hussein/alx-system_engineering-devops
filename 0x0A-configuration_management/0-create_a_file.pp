file {'school':
ensure  => 'present',c
content => 'I love Puppet',
group   => 'www-data',
mode    => '0744',
owner   => 'www-data',
path    => '/tmp/school',
}