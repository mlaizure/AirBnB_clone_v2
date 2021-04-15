# sets up web servers for deployment of web_static
include stdlib


exec { 'apt-get-update':
  command => '/usr/bin/env apt-get -y update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get-update'],
}

file { 'make dirs':
  ensure => 'directory',
  path   => [ '/data/', 'data/web_static/', 'data/web_static/shared/',
            '/data/web_static/releases/', '/data/web_static/releases/test/'],
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'simple content',
  require => File['make dirs'],
}

file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  require => File['/data/web_static/releases/test/index.html'],
}

exec { 'chown':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data/',
  require => File['/data/web_static/current'],
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
