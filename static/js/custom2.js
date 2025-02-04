function getUserName() {
    const user_name = $('#get_user_name').val().trim();

    if (!user_name) {
        alert('Please enter a username!');
        return;
    }

    $.ajax({
        url: '/find-user/',
        type: 'GET',
        data: {
            user_name: user_name
        },
        success: function (response) {
            if (response.status === "success") {
                if (!document.getElementById(response.username)) {
                    const newUser = `
                        <div class="user-list-item" id="${response.username}">
                            <img src="/static/images/users/avatar-1.jpg" alt="User" class="user-avatar">
                            <div class="user-info">
                                <div class="username">${response.first_name} ${response.last_name}</div>
                                <div class="text-muted"><a>${response.username}</a></div>
                            </div>
                            <button class="btn btn-outline-danger btn-remove"
                                    onclick="removeAccess('${response.csrf}', '${response.username}')">
                                Remove Access
                            </button>
                        </div>
                    `;
                    $('#no_permissions').remove()
                    $('.card.p-3').prepend(newUser);

                    if ($('.user-list-item').length > 3) {
                        $('.user-list-item').last().remove();
                    }

                    $('#get_user_name').val('');
                } else {
                    alert("User is already in the list!");
                }
            } else {
                alert(response.message);
            }
        },
        error: function (xhr, status, error) {
            console.error('Error:', error);
            alert('Failed to add access.');
        }
    });
}


function getUsernameFromURL() {
    const pathSegments = window.location.pathname.split('/');
    return pathSegments[pathSegments.length - 2];
}

function sendTextToOtherEncryption(csrf) {
    const username = getUsernameFromURL();
    if (!username) {
        alert('Username not found in URL!');
        return;
    }

    const text = $('#input-field').val();

    if (!text.trim()) {
        alert('Please enter a message!');
        return;
    }

    $.ajax({
        url: '/main/use-other-user-alphabet-encryption-processing/',
        type: 'POST',
        headers: {
            'X-CSRFToken': csrf
        },
        data: {text: text, username: username},
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


function removeAccess(csrf, username) {
    $.ajax({
        url: '/remove-access/',
        type: 'POST',
        headers: {
            'X-CSRFToken': csrf
        },
        data: {
            username: username,
        },

        success: function (response) {
            $(`[id="${username}"]`).remove();
            if ($('.user-list-item').length === 0) {
                $('.card.p-3').html('<p class="text-center text-muted" id="no_permissions">No Users Have Access.</p>');
            }
        },
        error: function (xhr, status, error) {
            console.error('Error:', error);
            alert('Failed to send the message.');
        },
    })
}
