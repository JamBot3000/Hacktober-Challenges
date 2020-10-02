const https = require('https')
const API_URL = 'https://api.chucknorris.io/jokes/random'

function GET_JOKES() {
    const req = https.get(API_URL, (res) => {
        console.log(`statusCode: ${res.statusCode}`)

        res.on('data', (d) => {
            console.log(JSON.parse(d.toString()).value)
        })
    })

    req.on('error', (error) => {
        console.error(error)
    })

    req.end()
}

GET_JOKES()
