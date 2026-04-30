Vagrant.configure("2") do |config|
  # Folosim imaginea oficială de Ubuntu 22.04
  config.vm.box = "ubuntu/jammy64"
  
  # TUNELUL DE REȚEA:
  # Mapăm portul 8080 de pe Windows (Host) către portul 8000 din Ubuntu (Guest)
  # Portul 8000 este cel pe care rulează Gunicorn în interiorul Docker
  config.vm.network "forwarded_port", guest: 8000, host: 8080

  config.vm.provider "virtualbox" do |vb|
    vb.name = "Licenta-Cicd-VM"
    vb.memory = "2048"
    # Rezolvă eventuale probleme de conexiune DNS în VirtualBox
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end

  # SCRIPTUL DE CONFIGURARE AUTOMATĂ (Provisioning)
  config.vm.provision "shell", inline: <<-SHELL
    # 1. Actualizăm pachetele și instalăm Docker
    apt-get update -y
    apt-get install -y docker.io
    systemctl start docker
    systemctl enable docker

    # 2. Permitem utilizatorului vagrant să folosească docker fără sudo
    usermod -aG docker vagrant

    # 3. Curățăm orice container vechi pentru a evita conflictele de nume/porturi
    echo "Curatare containere vechi..."
    docker stop licenta-web || true
    docker rm licenta-web || true

    # 4. Descarcă cea mai nouă imagine de pe Docker Hub (Cea construită de GitHub Actions)
    echo "Descarcare imagine noua de pe Docker Hub..."
    docker pull claudiulatea2/licenta-app:final

    # 5. Pornirea aplicației
    # Mapăm portul 8000 al containerului la portul 8000 al mașinii Ubuntu
    echo "Pornire container nou..."
    docker run -d --name licenta-web -p 8000:8000 claudiulatea2/licenta-app:final

    echo "Gata! Aplicatia ar trebui sa fie accesibila la http://localhost:8080"
  SHELL
end