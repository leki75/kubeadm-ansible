# -*- mode: ruby -*-
# vi: set ft=ruby :

servers=[
  {
    :hostname => "controller-0",
    :ip => "10.240.0.10",
    :mem => "2048",
    :cpu => "4"
  },
  # {
  #   :hostname => "controller-1",
  #   :ip => "10.240.0.11",
  #   :mem => "2048"
  #   :cpu => "4"
  # },
  # {
  #   :hostname => "controller-2",
  #   :ip => "10.240.0.12",
  #   :mem => "2048"
  #   :cpu => "4"
  # },
  {
    :hostname => "worker-0",
    :ip => "10.240.0.20",
    :mem => "768",
    :cpu => "2"
  },
  # {
  #   :hostname => "worker-1",
  #   :ip => "10.240.0.21",
  #   :mem => "768",
  #   :cpu => "2"
  # }
]

Vagrant.configure("2") do |config|
  config.vm.synced_folder ".", "/vagrant", disabled: true

  servers.each do |machine|
    config.vm.define machine[:hostname] do |node|
      #node.vm.box = "debian/buster64"
      node.vm.box = "ubuntu/focal64"
      node.vm.hostname = machine[:hostname]
      node.vm.network "private_network", ip: machine[:ip]

      node.vm.provider "virtualbox" do |vb|
        vb.gui = false
        vb.cpus = machine[:cpu]
        vb.memory = machine[:mem]
      end
    end
  end
end
