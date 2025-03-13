import os

def install_k3s():
    print("Installing k3s...")
    os.system("curl -sfL https://get.k3s.io | sh -")
    print("k3s installation completed.")

if __name__ == "__main__":
    install_k3s()

