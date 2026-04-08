function initAutocomplete(inputId, resultadosId, url) {
    const input = document.getElementById(inputId);
    const resultados = document.getElementById(resultadosId);

    if (!input || !resultados) return;

    input.addEventListener("input", async () => {
        const query = input.value;

        if (query.length < 2) {
            resultados.innerHTML = "";
            return;
        }

        try {
            const response = await fetch(`${url}?q=${query}`);

            if (!response.ok) {
                throw new Error("Error en servidor");
            }

            const data = await response.json();

            resultados.innerHTML = "";

            if (data.length === 0) {
                resultados.innerHTML = "<li>No se encontraron resultados</li>";
                return;
            }

            data.forEach(item => {
                const li = document.createElement("li");
                li.textContent = item.nombre;

                li.onclick = () => {
                    input.value = item.nombre;
                    resultados.innerHTML = "";

                    // opcional: guardar ID si existe input hidden
                    const hidden = document.querySelector(`#${inputId}_id`);
                    if (hidden) hidden.value = item.id;
                };

                resultados.appendChild(li);
            });

        } catch (error) {
            console.error("Error:", error);
            resultados.innerHTML = "<li>Error al buscar</li>";
        }
    });

    // cerrar dropdown
    document.addEventListener("click", (e) => {
        if (!e.target.closest(".autocomplete-container")) {
            resultados.innerHTML = "";
        }
    });
}