package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/sha256"
	"encoding/base64"
	"fmt"
	"os"
)

var secretKey = "keynest_secret_salt" // replace with stronger key in production

func createHash(key string) []byte {
	hash := sha256.Sum256([]byte(key))
	return hash[:]
}

func encrypt(text string) string {
	block, _ := aes.NewCipher(createHash(secretKey))
	plainText := []byte(text)
	cfb := cipher.NewCFBEncrypter(block, createHash(secretKey)[:block.BlockSize()])
	cipherText := make([]byte, len(plainText))
	cfb.XORKeyStream(cipherText, plainText)
	return base64.StdEncoding.EncodeToString(cipherText)
}

func decrypt(text string) string {
	block, _ := aes.NewCipher(createHash(secretKey))
	cipherText, _ := base64.StdEncoding.DecodeString(text)
	cfb := cipher.NewCFBDecrypter(block, createHash(secretKey)[:block.BlockSize()])
	plainText := make([]byte, len(cipherText))
	cfb.XORKeyStream(plainText, cipherText)
	return string(plainText)
}

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Usage: keynest_encryptor encrypt|decrypt <text>")
		return
	}

	command := os.Args[1]
	text := os.Args[2]

	if command == "encrypt" {
		fmt.Println(encrypt(text))
	} else if command == "decrypt" {
		fmt.Println(decrypt(text))
	} else {
		fmt.Println("Unknown command.")
	}
}
