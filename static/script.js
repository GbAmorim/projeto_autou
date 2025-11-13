document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("emailForm");
    const resultadoDiv = document.getElementById("resultado");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const formData = new FormData();
        const texto = document.getElementById("textoEmail").value;
        const arquivo = document.getElementById("arquivoEmail").files[0];

        if (texto) formData.append("texto", texto);
        if (arquivo) formData.append("arquivo", arquivo);

        try {
            const res = await fetch("/processar", {
                method: "POST",
                body: formData,
            });

            const data = await res.json();
            resultadoDiv.innerHTML = `
                <p><strong>Categoria:</strong> ${data.categoria}</p>
                <p><strong>Resposta sugerida:</strong> ${data.resposta_sugerida}</p>
            `;
        } catch (err) {
            console.error(err);
            resultadoDiv.innerHTML =
                "<p>Ocorreu um erro ao processar o e-mail.</p>";
        }
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const themeToggle = document.getElementById("themeToggle");
    const body = document.body;

    const applyTheme = (isDarkMode) => {
        if (isDarkMode) {
            body.classList.add("dark-mode");
            localStorage.setItem("theme", "dark");
        } else {
            body.classList.remove("dark-mode");
            localStorage.setItem("theme", "light");
        }
    };

    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        applyTheme(true);
    }

    themeToggle.addEventListener("click", () => {
        const isDarkModeCurrently = body.classList.contains("dark-mode");

        applyTheme(!isDarkModeCurrently);
    });
});
