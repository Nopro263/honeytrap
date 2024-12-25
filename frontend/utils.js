async function sha256(message) {
    // encode as UTF-8
    const msgBuffer = new TextEncoder().encode(message);                    

    // hash the message
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);

    // convert ArrayBuffer to Array
    const hashArray = Array.from(new Uint8Array(hashBuffer));

    // convert bytes to hex string                  
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    return hashHex;
}

export async function proof(start, hash, length) {
    const options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

    let v;

    const p = Math.pow(options.length, length - start.length);

    for(let i = 0; i < p; i++) {
        v = start;

        let vi = i;
    
        while(vi > 0) {
            v += options[vi % options.length];
            vi = Math.floor(vi / options.length);
        }

        v = v.padEnd(length, "a");
        
        if(await sha256(await sha256(v)) == hash) {
            return v;
        }
    }
}