# Installs puppet-lint
package { 'puppetlint':
  ensure   => '2.5.0',
  provider => 'gem',
}
