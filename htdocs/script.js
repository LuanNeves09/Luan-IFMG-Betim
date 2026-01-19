function fetchData(file, elementId) {
    const display = document.getElementById(elementId);
    display.innerHTML = "⏳ Solicitando via TCP...";
    
    // Adiciona um timestamp para evitar cache do navegador e forçar nova requisição TCP
    const url = file + '?t=' + new Date().getTime();

    if (file.endsWith('.jpg')) {
        const img = new Image();
        img.onload = () => { display.innerHTML = ""; display.appendChild(img); };
        img.onerror = () => { display.innerHTML = "❌ Erro ao carregar (Verifique o servidor)"; };
        img.src = url;
    } else {
        fetch(url)
            .then(response => {
                if (!response.ok) throw new Error("Erro HTTP: " + response.status);
                return response.text();
            })
            .then(text => {
                display.innerHTML = "✅ Recebido! Tamanho: " + text.length + " bytes";
            })
            .catch(err => {
                display.innerHTML = "❌ Falha na conexão: " + err.message;
            });
    }
}
