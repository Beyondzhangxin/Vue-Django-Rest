export default {
    baseURL: process.env.NODE_ENV == 'production'?'':'http://'+location.hostname+':8000',
    ws:process.env.NODE_ENV == 'production'?'ws://'+location.host:'ws://'+location.hostname+':8050',
    // baseURL: process.env.NODE_ENV == 'production'?'':'https://'+location.hostname+':8070',
    // ws:process.env.NODE_ENV == 'production'?'wss://'+location.host:'wss://'+location.hostname+':8070',
    // ws:'ws://'+location.host,
    isDev: true
}
