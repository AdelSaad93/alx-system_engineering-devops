# installs and configs nginx server

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => template('nginx/default.erb'),
  notify  => Exec['restart_nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
}

exec { 'restart_nginx':
  command     => 'service nginx restart',
  refreshonly => true,
}

file { '/etc/nginx/sites-available/default':
  ensure => 'present',
  content => template('nginx/default.erb'),
}

# Template file to set up the site configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
  ensure  => 'file',
  content => @("END")
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        rewrite ^/redirect_me https://www.youtube.com/watch?v=TfgBHC5gvTI permanent;
    }
}
| END
}
