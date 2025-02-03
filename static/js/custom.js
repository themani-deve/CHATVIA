function sendTextToPosNeg(uid, csrf) {
    const text = $('#input-field').val();
    const user_id = uid;

    if (!text.trim()) {
        alert('Please enter a message!');
        return;
    }

    $.ajax({
        url: '/main/ml-process-pos-neg/',
        type: 'POST',
        headers: {
            'X-CSRFToken': csrf
        },
        data: {
            user_id: user_id,
            text: text
        },
        success: function (response) {
            const chatContainer = $('.chat-conversation');
            chatContainer.scrollTop(chatContainer.prop("scrollHeight"));

            const predictedMessage = response.y_pred;

            const now = new Date();
            const hours = now.getHours().toString().padStart(2, '0');
            const minutes = now.getMinutes().toString().padStart(2, '0');
            const formattedTime = `${hours}:${minutes}`;

            const newMessage = `
        <li>
            <div class="conversation-list">
                <div class="chat-avatar">
                    <img src="/static/images/users/avatar-4.jpg" alt="">
                </div>
                <div class="user-chat-content">
                    <div class="ctext-wrap">
                        <div class="ctext-wrap-content">
                            <p class="mb-0">${text}</p>
                            <p class="chat-time mb-0">
                                <span class="align-middle">${formattedTime}</span>
                                <i class="ri-check-double-line align-middle"></i>
                            </p>
                        </div>
                    </div>
                    <div class="conversation-name"></div>
                </div>
            </div>
        </li>
        <li class="right">
            <div class="conversation-list">
                <div class="chat-avatar">
                    <img src="/static/images/users/avatar-4.jpg" alt="">
                </div>
                <div class="user-chat-content">
                    <div class="ctext-wrap">
                        <div class="ctext-wrap-content">
                            <p class="mb-0" id="bot">${predictedMessage}</p>
                            <p class="chat-time mb-0">
                                <span class="align-middle">${formattedTime}</span>
                                <i class="align-middle"></i>
                            </p>
                        </div>
                    </div>
                    <div class="conversation-name">Bot</div>
                </div>
            </div>
        </li>
    `;
            $('.chat-conversation ul').append(newMessage);
            setTimeout(scrollToBottom, 100);
            $('#input-field').val('');
            $('#empty-box').remove()
        },

        error: function (xhr, status, error) {
            console.error('Error:', error);
            alert('Failed to send the message.');
        }
    });
}

function sendTextToEncryption(csrf) {
    const text = $('#input-field').val();

    if (!text.trim()) {
        alert('Please enter a message!');
        return;
    }

    $.ajax({
        url: '/main/encryption-processing/',
        type: 'POST',
        headers: {
            'X-CSRFToken': csrf
        },
        data: {text: text},
        success: function (response) {
            const chatContainer = $('.chat-conversation');
            chatContainer.scrollTop(chatContainer.prop("scrollHeight"));

            const predictedMessage = response.y_pred;

            const now = new Date();
            const hours = now.getHours().toString().padStart(2, '0');
            const minutes = now.getMinutes().toString().padStart(2, '0');
            const formattedTime = `${hours}:${minutes}`;

            function breakText(text, maxLength = 80) {
                if (!text) return '';
                let result = '';
                for (let i = 0; i < text.length; i += maxLength) {
                    result += text.substring(i, i + maxLength) + '<br>';
                }
                return result;
            }

            const brokenUserMessage = breakText(text);
            const brokenServerMessage = breakText(predictedMessage);

            const newMessage = `
        <li>
            <div class="conversation-list">
                <div class="chat-avatar">
                    <img src="/static/images/users/avatar-4.jpg" alt="">
                </div>
                <div class="user-chat-content">
                    <div class="ctext-wrap">
                        <div class="ctext-wrap-content">
                            <p class="mb-0" style="word-wrap: break-word; overflow-wrap: break-word; white-space: normal; max-width: 100%; display: block;">${brokenUserMessage}</p>
                            <p class="chat-time mb-0">
                                <span class="align-middle">${formattedTime}</span>
                                <i class="ri-check-double-line align-middle"></i>
                            </p>
                        </div>
                    </div>
                    <div class="conversation-name">You</div>
                </div>
            </div>
        </li>
        <li class="right">
            <div class="conversation-list">
                <div class="chat-avatar">
                    <img src="/static/images/users/avatar-4.jpg" alt="">
                </div>
                <div class="user-chat-content">
                    <div class="ctext-wrap">
                        <div class="ctext-wrap-content">
                            <p class="mb-0" style="word-wrap: break-word; overflow-wrap: break-word; white-space: normal; max-width: 100%; display: block;" id="bot">${brokenServerMessage}</p>
                            <p class="chat-time mb-0">
                                <span class="align-middle">${formattedTime}</span>
                                <i class="align-middle"></i>
                            </p>
                        </div>
                    </div>
                    <div class="conversation-name">Encryption</div>
                </div>
            </div>
        </li>
    `;
            $('.chat-conversation ul').append(newMessage);
            setTimeout(scrollToBottom, 100);
            $('#input-field').val('');
            $('#empty-box').remove();
        },

        error: function (xhr, status, error) {
            console.error('Error:', error);
            alert('Failed to send the message.');
        }
    });
}


function sendTextToDecoder(csrf) {
    const numbers = $('#input-field').val();

    if (!numbers.trim()) {
        alert('Please enter a message!');
        return;
    }

    $.ajax({
        url: '/main/decoder-processing/',
        type: 'POST',
        headers: {
            'X-CSRFToken': csrf
        },
        data: {numbers: numbers},
        success: function (response) {
            const chatContainer = $('.chat-conversation');
            chatContainer.scrollTop(chatContainer.prop("scrollHeight"));

            const predictedMessage = response.y_pred;

            const now = new Date();
            const hours = now.getHours().toString().padStart(2, '0');
            const minutes = now.getMinutes().toString().padStart(2, '0');
            const formattedTime = `${hours}:${minutes}`;

            function breakText(text, maxLength = 80) {
                if (!text) return '';
                let result = '';
                for (let i = 0; i < text.length; i += maxLength) {
                    result += text.substring(i, i + maxLength) + '<br>';
                }
                return result;
            }

            const brokenUserMessage = breakText(numbers);
            const brokenServerMessage = breakText(predictedMessage);

            const newMessage = `
        <li>
            <div class="conversation-list">
                <div class="chat-avatar">
                    <img src="/static/images/users/avatar-4.jpg" alt="">
                </div>
                <div class="user-chat-content">
                    <div class="ctext-wrap">
                        <div class="ctext-wrap-content">
                            <p class="mb-0" style="word-wrap: break-word; overflow-wrap: break-word; white-space: normal; max-width: 100%; display: block;">${brokenUserMessage}</p>
                            <p class="chat-time mb-0">
                                <span class="align-middle">${formattedTime}</span>
                                <i class="ri-check-double-line align-middle"></i>
                            </p>
                        </div>
                    </div>
                    <div class="conversation-name">You</div>
                </div>
            </div>
        </li>
        <li class="right">
            <div class="conversation-list">
                <div class="chat-avatar">
                    <img src="/static/images/users/avatar-4.jpg" alt="">
                </div>
                <div class="user-chat-content">
                    <div class="ctext-wrap">
                        <div class="ctext-wrap-content">
                            <p class="mb-0" style="word-wrap: break-word; overflow-wrap: break-word; white-space: normal; max-width: 100%; display: block;" id="bot">${brokenServerMessage}</p>
                            <p class="chat-time mb-0">
                                <span class="align-middle">${formattedTime}</span>
                                <i class="align-middle"></i>
                            </p>
                        </div>
                    </div>
                    <div class="conversation-name">Decoder</div>
                </div>
            </div>
        </li>
    `;
            $('.chat-conversation ul').append(newMessage);
            setTimeout(scrollToBottom, 100);
            $('#input-field').val('');
            $('#empty-box').remove();
        },

        error: function (xhr, status, error) {
            console.error('Error:', error);
            alert('Failed to send the message.');
        }
    });
}


function scrollToBottom() {
    let botMessages = document.querySelectorAll("#bot");
    if (botMessages.length > 0) {
        botMessages[botMessages.length - 1].scrollIntoView({behavior: "smooth"});
    }
}
