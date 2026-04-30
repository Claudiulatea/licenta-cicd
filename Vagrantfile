Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  
  config.vm.network "forwarded_port", guest: 8080, host: 8080

  config.vm.provider "virtualbox" do |vb|
    vb.name = "Licenta-Cicd-VM"
    vb.memory = "2048"
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update -y
    apt-get install -y docker.io
    systemctl start docker
    systemctl enable docker
    usermod -aG docker vagrant

    docker stop licenta-web || true
    docker rm licenta-web || true
    docker pull claudiulatea2/licenta-app:v6.1
    docker run -d --name licenta-web -p 8080:5000 claudiulatea2/licenta-app:v6.1
  SHELL
end