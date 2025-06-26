import subprocess

def encrypt(password: str) -> str:
    """Encrypt a plaintext password using keynest_encryptor Go binary."""
    result = subprocess.run(["./keynest_encryptor", "encrypt", password], capture_output=True, text=True)
    return result.stdout.strip()

def decrypt(encrypted: str) -> str:
    """Decrypt an encrypted password using keynest_encryptor Go binary."""
    result = subprocess.run(["./keynest_encryptor", "decrypt", encrypted], capture_output=True, text=True)
    return result.stdout.strip()
