document.getElementById("translateButton").addEventListener("click", async () => {
    const inputText = document.getElementById("inputText").value;
    const outputTextArea = document.getElementById("outputText");
    const selectedLanguage = document.getElementById("languageSelect").value;
  
    // Check if input text is empty
    if (!inputText) {
      outputTextArea.value = "Please enter some text.";
      return;
    }
  
    // Azure API Details
    const apiKey = "BxJ6dxXEjnWo5oOI7UOEKD9Utla6GuGTTw26FE5cIYtXBWuUxl3tJQQJ99BAACGhslBXJ3w3AAAbACOGH0Ou"; // API Key 1
    const endpoint = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0";
    const region = "centralindia";  // Central India region
  
    try {
      // Sending the request to Azure Translator API
      const response = await fetch(`${endpoint}&to=${selectedLanguage}`, {
        method: "POST",
        headers: {
          "Ocp-Apim-Subscription-Key": apiKey,
          "Content-Type": "application/json",
          "Ocp-Apim-Subscription-Region": region,
        },
        body: JSON.stringify([{ Text: inputText }]),
      });
  
      // If the response is not OK, throw an error
      if (!response.ok) {
        throw new Error("Translation failed.");
      }
  
      // Parse the response JSON
      const data = await response.json();
  
      // Display the translated text
      outputTextArea.value = data[0].translations[0].text;
  
    } catch (error) {
      // Handle error
      console.error("Error details:", error); // Logs error in browser console
      outputTextArea.value = `Error: ${error.message}`;
    }
  });
  