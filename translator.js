
function play() {
    const newSentence = [];
    event.preventDefault();
    const sentence = document.getElementById('search').value
    const result = document.getElementById('result_area')
    console.log(sentence)
    let sent = sentence.split(' ')
    console.log(sent)
        // check if in csv
        fetch('data.csv')
            .then(response => response.text())
            .then(text => {
                const rows = text.split('\n').map(row => row.split(','));

                sent.forEach(word => {
                    let wordFound = false;
                    rows.forEach(row => {
                        if (row.length === 2 && word === row[0].toLowerCase().trim()) {
                            let dec = row[1].trim();
                            console.log(dec)
                            newSentence.push(dec);
                            wordFound = true;
                        }
                    });
                    if (!wordFound) {
                        newSentence.push(word);
                    }
                });
                if (newSentence.length === 3) {
                    console.log('true')
                }
                console.log(newSentence.join(' '))
                result.innerHTML = `<span style='font-size:30px; font-family: "Madimi One", sans-serif'>${newSentence.join(' ')}</span>`;
            }) 
            .catch(error => console.error('Error fetching the CSV file:', error));
}