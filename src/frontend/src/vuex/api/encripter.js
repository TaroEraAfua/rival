const crypto = require('crypto');
const algorithm = 'aes-256-cfb';
export default {
  /**
   * encrypt AES 256
   *
   * @param text
   * @return Object
   */
  encrypt: function (text, keyStr){
    console.log("encrypt");
    text = JSON.stringify(text);
    const hash = crypto.createHash('sha256');
    hash.update(keyStr);
    const keyBytes = hash.digest();

    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv(algorithm, keyBytes, iv);
    let enc = [iv, cipher.update(text, 'utf8')];
    enc.push(cipher.final());
    return Buffer.concat(enc).toString('base64');
  },

  /**
   * decrypt AES 256
   *
   * @param encText
   * @return
   */
  decrypt: function (text, keyStr) {
    console.log("decrypt");
    const hash = crypto.createHash('sha256');
    hash.update(keyStr);
    const keyBytes = hash.digest();

    const contents = Buffer.from(text, 'base64');
    const iv = contents.slice(0, 16);
    const textBytes = contents.slice(16);
    const decipher = crypto.createDecipheriv(algorithm, keyBytes, iv);
    let res = decipher.update(textBytes, '', 'utf8');
    res += decipher.final('utf8');
    res = JSON.parse(res);
    return res;
  },

};

