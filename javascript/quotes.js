const { isUtf8 } = require('node:buffer');
const fs = require('node:fs');

fs.readFile('thirukkural.json', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }

    try {
        const jsonData = JSON.parse(data);
        getRandomQuote(jsonData);
    } catch (error) {
        console.error('Error parsing JSON Data: ', parseError);
    }
    
});

/**
 * Function to return quotes at random from given array of quotes
 */

function getRandomQuote(jsonData) {

    const keys = Object.keys(jsonData);
    console.log(keys)

    let index = (Math.floor(Math.random() * keys.length))
    let quote = quotes[index].Number;

    document.getElementById("quote").innerHTML = quote

    console.log(quote)
    return quote;
}