function sendText(uid) {
    const text = $('#input-field').val();
    const user_id = uid;

    if (!text.trim()) {
        alert('Please enter a message!');
        return;
    }

    $.ajax({
        url: '/main/ml-process-pos-neg/',
        type: 'GET',
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
                                <i class="ri-time-line align-middle"></i>
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
                            <p class="mb-0">${predictedMessage}</p>
                            <p class="chat-time mb-0">
                                <span class="align-middle">${formattedTime}</span>
                                <i class="ri-time-line align-middle"></i>
                            </p>
                        </div>
                    </div>
                    <div class="conversation-name">Bot</div>
                </div>
            </div>
        </li>
    `;
            $('.chat-conversation ul').append(newMessage);
            $('#input-field').val(''); // Clear input field
            $('#empty-box').remove()
        },

        error: function (xhr, status, error) {
            console.error('Error:', error);
            alert('Failed to send the message.');
        }
    });
}
