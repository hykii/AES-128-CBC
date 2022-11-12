const crypto = require("crypto");

const iv = "1234567890abcdef";
const key = "@ABCDEFGHI12345!";

// Encrypt  -  Result : wP3XthWbuBMvNsDab2RHZQ==
console.log(AES_128_CBC_Encrypt("encrypt text", key, iv));

// Decrypt  -  Result : encrypt text
console.log(AES_128_CBC_Decrypt("wP3XthWbuBMvNsDab2RHZQ==", key, iv));

function AES_128_CBC_Encrypt(text, key, iv) {
    var cipher = crypto.createCipheriv("AES-128-CBC", Buffer.from(key), Buffer.from(iv));
    var crypted = cipher.update(Buffer.from(text), "utf-8", "binary");
    crypted += cipher.final("binary");
    return Buffer.from(crypted, "binary").toString("base64");
}
function AES_128_CBC_Decrypt(text, key, iv) {
    text = Buffer.from(text, "base64").toString("binary");
    var decipher = crypto.createDecipheriv("AES-128-CBC", Buffer.from(key), Buffer.from(iv));
    decipher.setAutoPadding(false);    
    var decoded = decipher.update(text, "binary", "utf8");
    decoded += decipher.final("utf8");
    return decoded;
}
