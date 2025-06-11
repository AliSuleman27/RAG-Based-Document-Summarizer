document.getElementById('summarizeForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData();
    formData.append('document', document.getElementById('document').files[0]);
    
    try {
        const response = await fetch('/summarize', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        // Display results
        document.getElementById('summary').innerHTML = data.summary;
        
        const contextContainer = document.getElementById('context');
        contextContainer.innerHTML = data.context_chunks.map(chunk => `
            <div class="p-4 border border-gray-200 rounded-md">
                <p>${chunk}</p>
            </div>
        `).join('');
        
        document.getElementById('results').classList.remove('hidden');
    } catch (error) {
        console.error('Error:', error);
        alert('Error generating summary');
    }
});