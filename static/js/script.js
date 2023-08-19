// Example POST method implementation:
async function postData(url = "", data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: "POST", // *GET, POST, PUT, DELETE, etc.
      headers: {
        "Content-Type": "application/json",
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: JSON.stringify(data), // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
  }
  
  

sendButton.addEventListener('click', async () => {
    questioninput = document.getElementById('questioninput').value;
    document.getElementById('questioninput').value = '';
    document.querySelector('.right2').style.display = 'block';
    document.querySelector('.right-section').style.display = 'none';
    document.querySelector('#question').innerHTML = questioninput;

    let result = await postData("/api", { "question": questioninput })
    document.querySelector('#solution').innerHTML = result.answer;

}
)