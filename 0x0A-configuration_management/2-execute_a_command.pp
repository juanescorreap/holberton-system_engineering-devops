# Manifest that kills a process named killmenow
exec { 'killmenow':
  command => 'pkill -f',
  path    => '/usr/bin/',
}
