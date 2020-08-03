# using Puppet to create a manifest that kill a precess

exec { 'pkill':
  command  => 'pkill killmenow',
  path     => '/usr/bin:/usr/sbin:/bin',
}
