<script>
    let userInput = "";
    let response = "";
  
  async function sendMessage() {
    if (!userInput.trim()) return;

    const res = await fetch("http://127.0.0.1:5000/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_input: userInput }),
    });

    const data = await res.json();
    response = data.response; // Extract 'response' field from JSON
  }
</script>

<style>
  body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 50px;
  }
  textarea {
    width: 80%;
    height: 100px;
    padding: 10px;
    margin-bottom: 10px;
  }
  button {
    padding: 10px 15px;
    cursor: pointer;
  }
</style>
  
  <h2>Simple GPT Wrapper</h2>
  
  <textarea bind:value={userInput} placeholder="Enter text..."></textarea>
  <br />
  <button on:click={sendMessage}>Submit</button>
  
  {#if response}
    <h3>GPT Response:</h3>
    <p>{response}</p>
  {/if}
  