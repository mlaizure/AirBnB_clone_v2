# sets up web servers for deployment of web_static
include stdlib

exec { 'apt-get-update':
  command => '/usr/bin/env apt-get -y update',
}

-> package { 'nginx':
  ensure  => 'installed',
}

-> file { [ '/data/', 'data/web_static/', 'data/web_static/shared/',
            '/data/web_static/releases/', '/data/web_static/releases/test/' ]:
              ensure => 'directory',
}

-> file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'simple content',
}

-> file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

-> exec { 'chown':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data/',
}

file_line { 'hbnb page config':
  path    => '/etc/nginx/sites-available/default',
  after   => '^\s+server_name .+;',
  line    => "\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}",
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  restart => 'service nginx restart',
  require => Package['nginx']
}
