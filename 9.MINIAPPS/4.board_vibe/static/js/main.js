document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const postForm = document.getElementById('post-form');
    const titleInput = document.getElementById('title');
    const messageInput = document.getElementById('message');
    const postsContainer = document.getElementById('posts-container');
    const postCountEl = document.getElementById('post-count');
    const emptyStateEl = document.getElementById('empty-state');
    const loadingStateEl = document.getElementById('loading-state');
    const submitBtn = document.getElementById('submit-btn');

    // Validation styling helpers
    const setInvalid = (inputEl) => {
        inputEl.parentElement.classList.add('invalid');
    };

    const clearInvalid = (inputEl) => {
        inputEl.parentElement.classList.remove('invalid');
    };

    // Live validation clearing on input
    titleInput.addEventListener('input', () => {
        if (titleInput.value.trim() !== '') {
            clearInvalid(titleInput);
        }
    });

    messageInput.addEventListener('input', () => {
        if (messageInput.value.trim() !== '') {
            clearInvalid(messageInput);
        }
    });

    // Format relative time or clean date
    const formatDate = (dateStr) => {
        try {
            // dateStr format: YYYY-MM-DD HH:MM:SS
            const t = dateStr.split(/[- :]/);
            const date = new Date(t[0], t[1] - 1, t[2], t[3], t[4], t[5]);
            const now = new Date();
            const diffMs = now - date;
            const diffMins = Math.floor(diffMs / 60000);
            const diffHours = Math.floor(diffMins / 60);
            
            if (diffMins < 1) return '방금 전';
            if (diffMins < 60) return `${diffMins}분 전`;
            if (diffHours < 24) return `${diffHours}시간 전`;
            
            // Default date string formatting
            return `${date.getFullYear()}년 ${date.getMonth() + 1}월 ${date.getDate()}일`;
        } catch (e) {
            return dateStr; // fallback to original string
        }
    };

    // Create a Post Card Element
    const createCardElement = (post) => {
        const card = document.createElement('div');
        card.className = 'glass-card post-card';
        card.dataset.id = post.id;
        
        card.innerHTML = `
            <div class="post-card-body">
                <h4 class="post-card-title">${escapeHtml(post.title)}</h4>
                <p class="post-card-text">${escapeHtml(post.message)}</p>
            </div>
            <div class="post-card-footer">
                <span class="post-card-badge">Vibe Log</span>
                <span class="post-card-time" title="${post.created_at}">
                    <i class="fa-regular fa-clock"></i> ${formatDate(post.created_at)}
                </span>
            </div>
        `;
        return card;
    };

    // Helper: Escape HTML to prevent XSS
    const escapeHtml = (text) => {
        const div = document.createElement('div');
        div.innerText = text;
        return div.innerHTML;
    };

    // Update Post Count
    const updatePostCount = (count) => {
        postCountEl.innerText = `게시글 ${count}개`;
        if (count === 0) {
            emptyStateEl.style.display = 'flex';
        } else {
            emptyStateEl.style.display = 'none';
        }
    };

    // Fetch existing posts
    const loadPosts = async () => {
        try {
            loadingStateEl.style.display = 'flex';
            emptyStateEl.style.display = 'none';
            postsContainer.innerHTML = '';
            
            const response = await fetch('/api/posts');
            const result = await response.json();
            
            loadingStateEl.style.display = 'none';
            
            if (result.status === 'success') {
                const posts = result.data;
                updatePostCount(posts.length);
                
                posts.forEach(post => {
                    const card = createCardElement(post);
                    postsContainer.appendChild(card);
                });
            } else {
                console.error('Failed to fetch posts:', result.message);
                showErrorMessage('게시글을 불러오는데 실패했습니다.');
            }
        } catch (error) {
            loadingStateEl.style.display = 'none';
            console.error('Error fetching posts:', error);
            showErrorMessage('서버와의 연결이 원활하지 않습니다.');
        }
    };

    // Handle Form Submit
    postForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const title = titleInput.value.trim();
        const message = messageInput.value.trim();
        let isValid = true;
        
        // Validation check
        if (!title) {
            setInvalid(titleInput);
            isValid = false;
        } else {
            clearInvalid(titleInput);
        }
        
        if (!message) {
            setInvalid(messageInput);
            isValid = false;
        } else {
            clearInvalid(messageInput);
        }
        
        if (!isValid) return;

        // Disable submit button during operation
        submitBtn.disabled = true;
        const origBtnHtml = submitBtn.innerHTML;
        submitBtn.innerHTML = `
            <span class="btn-text">게시 중...</span>
            <span class="btn-icon"><i class="fa-solid fa-spinner fa-spin"></i></span>
        `;

        try {
            const response = await fetch('/api/posts', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title, message })
            });
            
            const result = await response.json();
            
            submitBtn.disabled = false;
            submitBtn.innerHTML = origBtnHtml;
            
            if (response.ok && result.status === 'success') {
                // Clear inputs
                titleInput.value = '';
                messageInput.value = '';
                
                // Add card with entry animation
                const newCard = createCardElement(result.data);
                
                // Prepend to top of container
                postsContainer.insertBefore(newCard, postsContainer.firstChild);
                
                // Update total count
                const currentCount = postsContainer.children.length;
                updatePostCount(currentCount);
                
                // Trigger visual feedback (form card subtle glow)
                const formCard = document.querySelector('.form-card');
                formCard.style.boxShadow = '0 0 35px rgba(52, 211, 153, 0.4)';
                setTimeout(() => {
                    formCard.style.boxShadow = '';
                }, 1000);
            } else {
                showErrorMessage(result.message || '게시글 등록에 실패했습니다.');
            }
        } catch (error) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = origBtnHtml;
            console.error('Error posting data:', error);
            showErrorMessage('서버와의 통신 도중 에러가 발생했습니다.');
        }
    });

    // Display basic Toast error message
    const showErrorMessage = (msg) => {
        // Simple elegant alert fallback
        alert(msg);
    };

    // Load initial posts
    loadPosts();
});
