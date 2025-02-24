(function() {
    let chatContainer = document.createElement("div");
    chatContainer.id = "danceProcessChatbot";
    document.body.appendChild(chatContainer);

    let script = document.createElement("script");
    script.src = "https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js";
    script.onload = function() {
        initChatbot();
    };
    document.body.appendChild(script);

    function initChatbot() {
        if (document.getElementById("chatbotWidget")) return; // Prevent duplicate instances

        let chatbot = document.createElement("div");
        chatbot.id = "chatbotWidget";
        chatbot.style.position = "fixed";
        chatbot.style.bottom = "20px";
        chatbot.style.right = "20px";
        chatbot.style.width = "360px";
        chatbot.style.height = "500px";
        chatbot.style.backgroundColor = "#B8E6C1";
        chatbot.style.borderRadius = "10px";
        chatbot.style.boxShadow = "0px 4px 10px rgba(0, 0, 0, 0.2)";
        chatbot.style.display = "flex";
        chatbot.style.flexDirection = "column";
        chatbot.innerHTML = `
            <div id='chatbot-header' style='background-color: #8AC9A1; color: #ffffff; padding: 10px; text-align: center; font-weight: bold; border-top-left-radius: 10px; border-top-right-radius: 10px;'>
                The Dance Process Chatbot <span id='chatbot-close' style='cursor: pointer;'>✖</span>
            </div>
            <div id='chatbot-messages' style='flex-grow: 1; padding: 10px; overflow-y: auto; color: black;'></div>
            <div id='chatbot-input-container' style='display: flex; padding: 10px; border-top: 1px solid #ddd; background-color: #f1f1f1;'>
                <input id='chatbot-input' type='text' placeholder='Type a message...' style='flex-grow: 1; padding: 8px; border: 1px solid #ccc; border-radius: 5px;'>
                <button id='chatbot-send' style='background-color: #8AC9A1; color: white; border: none; padding: 8px 12px; margin-left: 8px; border-radius: 5px; cursor: pointer;'>Send</button>
            </div>
        `;
        document.body.appendChild(chatbot);

        document.getElementById("chatbot-send").addEventListener("click", function () {
            sendMessage(document.getElementById("chatbot-input").value);
        });

        document.getElementById("chatbot-input").addEventListener("keypress", function (e) {
            if (e.key === "Enter") sendMessage(document.getElementById("chatbot-input").value);
        });

        document.getElementById("chatbot-close").addEventListener("click", function () {
            document.getElementById("chatbotWidget").style.display = "none";
        });
    }

    // **Make sure initChatbot is global**
    window.initChatbot = initChatbot;
})();
window.initChatbot = initChatbot;
