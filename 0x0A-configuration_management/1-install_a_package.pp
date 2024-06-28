# Install puppet-lint package
package {'python3-pip':
  ensure => installed,
}

python::pip { 'flask':
  ensure   => '2.1.0',
  pip_provider => 'pip3'
  require => Package['python3-pip'],
}
