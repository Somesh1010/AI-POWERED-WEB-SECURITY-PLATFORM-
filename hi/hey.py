install nodejs: node --version
install tuffle: npm install -g truffle
save js code: truffle-config.js
manage the network: truffle migrate --network development
compile sm: truffle compile
run file: truffle init
compile: truffle compile
deploy: truffle migrate --network development
Arpan Bora
10:16
truffle-config.js: module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 7545, // Standard Ganache GUI port; adjust if using Ganache CLI (usually 8545)
      network_id: "*", // Match any network ID
    },
  },
  compilers: {
    solc: {
      version: "0.8.0", // Match your contract's pragma statement
    },
  },
};
module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 7545, // Standard Ganache GUI port; adjust if using Ganache CLI (usually 8545)
      network_id: "*", // Match any network ID
    },
  },
  compilers: {
    solc: {
      version: "0.8.0", // Match your contract's pragma statement
    },
  },
};