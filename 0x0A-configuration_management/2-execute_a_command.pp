# using Puppet to create a manifest that kill a precess

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin',],
}
