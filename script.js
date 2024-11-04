document.addEventListener("DOMContentLoaded", function() {
    const noteForm = document.getElementById("noteForm");
    const notesList = document.getElementById("notesList");

    // Função para adicionar uma nova nota na lista
    function addNoteToList(title, content) {
        const card = document.createElement("div");
        card.classList.add("card");

        card.innerHTML = `
            <div class="card-body">
                <h5 class="card-title">${title}</h5>
                <p class="card-text">${content}</p>
                <button class="btn btn-danger btn-sm delete-btn">Excluir</button>
                <button class="btn btn-info btn-sm edit-btn">Editar</button>
            </div>
        `;
        notesList.appendChild(card);

        card.querySelector(".delete-btn").addEventListener("click", () => {
            card.remove();
        });

        card.querySelector(".edit-btn").addEventListener("click", () => {
            document.getElementById("title").value = title;
            document.getElementById("content").value = content;
            card.remove();
        });
    }

    noteForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const title = document.getElementById("title").value;
        const content = document.getElementById("content").value;
        
        addNoteToList(title, content);
        
        noteForm.reset();
    });
});
