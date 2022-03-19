document.getElementById('post-date').innerHTML = Intl.DateTimeFormat('en-US', {
    dateStyle: 'long',
    timeStyle: 'short'
}).format()

async function sendLike(postId) {
    const url = await fetch(`http://127.0.0.1:5000/like/${postId}`)
}