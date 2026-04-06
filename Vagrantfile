Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  
  config.vm.network "forwarded_port", guest: 8080, host: 8080

  # REPARATIE: Fortam VirtualBox sa foloseasca internetul laptopului (DNS)
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end

  config.vm.provision "shell", inline: <<-SHELL
    echo "1. Instalez Docker pe server..."
    apt-get update
    apt-get install -y docker.io
    systemctl start docker

    echo "2. Descarc si pornesc aplicatia ta din Docker Hub..."
    docker stop licenta-web || true
    docker rm licenta-web || true
    docker pull claudiulatea2/licenta-app:latest
    docker run -d --name licenta-web -p 8080:5000 claudiulatea2/licenta-app:latest
  SHELL
end