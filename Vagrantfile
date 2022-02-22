# -*- mode: ruby -*-
# vi: set ft=ruby :

servers=[
  {
    :hostname => "controller-0.eqnx",
    :ipin => "10.200.0.10",
    :ipout => "10.202.0.10",
    :mem => "2048",
    :cpu => "4"
  },
  {
    :hostname => "controller-1.eqnx",
    :ipin => "10.200.0.11",
    :ipout => "10.202.0.11",
    :ip => "10.200.0.11",
    :mem => "2048",
    :cpu => "4"
  },
  {
    :hostname => "controller-2.eqnx",
    :ipin => "10.200.0.12",
    :ipout => "10.202.0.12",
    :ip => "10.200.0.12",
    :mem => "2048",
    :cpu => "4"
  },
  {
    :hostname => "worker-0.eqnx",
    :ipin => "10.200.0.20",
    :ipout => "10.202.0.20",
    :mem => "768",
    :cpu => "2"
  },
  # {
  #   :hostname => "worker-1.eqnx",
  #   :ip => "10.200.0.21",
  #   :mem => "768",
  #   :cpu => "2"
  # }
]

Vagrant.configure("2") do |config|
  config.vm.synced_folder ".", "/vagrant", disabled: true

  servers.each do |machine|
    config.vm.define machine[:hostname] do |node|
      node.vm.box = "ubuntu/focal64"
      node.vm.hostname = machine[:hostname]
      node.vm.network "private_network", ip: machine[:ipin]
      node.vm.network "private_network", ip: machine[:ipout]

      node.vm.provider "virtualbox" do |vb|
        vb.gui = false
        vb.cpus = machine[:cpu]
        vb.memory = machine[:mem]
      end
    end
  end
end
