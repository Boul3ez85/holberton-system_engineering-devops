# install puppet-lint using Pappet
#Requirements:
#Install puppet-lint
#Version must be 2.1.1


Package {'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
