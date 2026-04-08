function initAutocomplete(inputId, resultadosId, url, redirect = false) {
    const input = document.getElementById(inputId);
    const resultados = document.getElementById(resultadosId);

    if (!input || !resultados) return;

    input.addEventListener("input", async () => {
        const query = input.value.trim();

        if (query.length < 2) {
            resultados.innerHTML = "";
            return;
        }

        try {
            const response = await fetch(`${url}?q=${encodeURIComponent(query)}`);

            if (!response.ok) throw new Error("Error en servidor");

            const data = await response.json();
            resultados.innerHTML = "";

            if (!data.length) {
                resultados.innerHTML = "<li>No se encontraron resultados</li>";
                return;
            }

            data.forEach(item => {
                const li = document.createElement("li");
                // Mostrar nombre + apellido
                li.textContent = `${item.nombre} ${item.apellido || ""}`.trim();

                li.onclick = () => {
                    input.value = `${item.nombre} ${item.apellido || ""}`.trim(); // ya viene como "nombre apellido"
                    resultados.innerHTML = "";

                    // Guardar ID en input hidden si existe
                    const hidden = document.querySelector(`#${inputId}_id`);
                    if (hidden) hidden.value = item.id;

                    // Si redirect es true, recargar la lista de pacientes
                    if (redirect) {
                        window.location.href = `${window.location.pathname}?q=${encodeURIComponent(input.value)}`;
                    }
                };

                resultados.appendChild(li);
            });

        } catch (error) {
            console.error("Error:", error);
            resultados.innerHTML = "<li>Error al buscar</li>";
        }
    });

    // Cerrar dropdown al hacer click fuera
    document.addEventListener("click", (e) => {
        if (!e.target.closest(".autocomplete-container")) {
            resultados.innerHTML = "";
        }
    });
}